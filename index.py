import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go


# Connect to main app.py file
from app import app
from app import server

# Connect to your app pages
from apps import dashboard, scoring, navbar

# ----------------------------------
# load and manipulate data for index page

df = pd.read_pickle("datasets/complete_score.pkl")
gob = df.groupby(["alpha3code", "country"])["account_number"].count()
gob = gob.reset_index()
gob = gob.sort_values("account_number", ascending=False)
gob = gob.reset_index(drop=True)

gob['text'] = gob['country'] + '<br>Count ' + (gob['account_number']).astype(str)
limits = [(0,1),(2,5),(6,20),(21,50),(51,96)]
colors = ["royalblue","crimson","lightseagreen","orange","lightgrey"]
cities = []
scale = 4

fig = go.Figure()

for i in range(len(limits)):
    lim = limits[i]
    df_sub = gob[lim[0]:lim[1]]
    fig.add_trace(go.Scattergeo(
        locationmode = 'ISO-3',
        locations = df_sub["alpha3code"],
        text = df_sub['text'],
        marker = dict(
            size = df_sub['account_number']*scale,
            color = colors[i],
            line_color='rgb(40,40,40)',
            line_width=0.5,
            sizemode = 'area'
        ),
        name = '{0} - {1}'.format(lim[0],lim[1])))
    
fig.update_geos(projection_type="orthographic")

fig.update_layout(
        #title = {"text":"CDP Survey Participation per Country", "x":0.5, "xanchor":"center", "font_dict:{weight":"bold"},
        showlegend = False,
        geo = dict(
            scope = 'world',
            landcolor = 'rgb(217, 217, 217)',
        ),
        height=500, 
        margin={"r":0,"t":15,"l":0,"b":0}
    )

fig.update_geos(
    resolution=50,
    showcountries=True,
    showland=True, landcolor="#FFFFF0",
    showocean=True, oceancolor="LightBlue",
)


# ----------------------------------
# creating cards

# ------------------------------------------------------------
# app layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content', children=[])
])

# -------------------------------------------------------------
# index page 
index_page = html.Div([
    navbar.navbar(),
    html.Br(),
    dbc.Row(
    dbc.Card([
        dbc.CardHeader("Unlocking Climate Solutions"),
        dbc.CardBody([
            html.P("Indentification of Collaboration opportunities between cities and businesses for socially equitable climate risk mitigation", style={"textAlign":"center"}),
            dcc.Graph(figure=fig),
            html.P("CDP Survey Participants per Country 2018-2020", style={"textAlign":"center"}),
            html.Br(),
            html.Br(),
            html.P("Find out more about our project and our interactive dashboard!", style={"textAlign":"center"}),
            dbc.Row([
                dbc.Button("Dashboard", href='/apps/dashboard', color="primary", className="mr-1", size="lg",
                style={"font-size": "larger", "text-decoration": "none"}),
                dbc.Button("Project", href='/apps/scoring', color="primary", className="mr-1", size="lg",
                style={"font-size": "larger", "text-decoration": "none"}),
            ],
            justify="center"
            )
        ])
    ],
    className="w-75",
    ),
    justify="center")      
])

# -------------------------------------------------------------


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
