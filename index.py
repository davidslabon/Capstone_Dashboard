import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd


# Connect to main app.py file
from app import app
from app import server

# Connect to your app pages
from apps import dashboard, scoring, navbar

# ----------------------------------
# load and manipulate data for index page

df = pd.read_pickle("datasets/dummy_df.pkl")
gob = df.groupby(["region", "country", "alpha3code","year"])[["account_number"]].count()
gob = gob.reset_index().sort_values(by="year")

fig = px.scatter_geo(
    gob, 
    locations="alpha3code", 
    color="region",
    hover_name="country", size="account_number",
    animation_frame="year",
    projection="natural earth"
    )

fig.update_layout(
    title_text = "Participants per year",
    title_xanchor= "center",
    title_x = 0.5,
    margin=dict(l=0, r=0, b=0,t=30 ,pad=0),
    legend_xanchor="center",
    legend_x = 0.5,
    legend_orientation = "h",
    height = 600
    )


# ----------------------------------

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content', children=[])
])

# ---------------------

index_page = html.Div([
    navbar.navbar(),
    html.H1('SCORE2 Landingpage', style={"textAlign": "center"}),
    dcc.Graph(figure=fig)
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/dashboard':
        return dashboard.layout
    if pathname == '/apps/scoring':
        return scoring.layout
    else:
        return index_page



if __name__ == '__main__':
    app.run_server(debug=True)
