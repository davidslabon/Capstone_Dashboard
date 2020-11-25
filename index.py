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

cs = ['#46039f', '#7201a8', '#9c179e', '#bd3786', '#d8576b', '#ed7953', '#fb9f3a']#, '#fdca26', '#f0f921']
# ----------------------------------
# load and manipulate data for index page

df = pd.read_pickle("datasets/complete_score.pkl")
gob = df.groupby(["alpha3code", "country"])["account_number"].count()
gob = gob.reset_index()
gob = gob.sort_values("account_number", ascending=False)
gob = gob.reset_index(drop=True)

gob['text'] = gob['country'] + '<br>Count ' + (gob['account_number']).astype(str)
fig = go.Figure(data=go.Choropleth(locations=gob['alpha3code'],z=gob["account_number"],
                text=gob["text"],
                hoverinfo="text",
                marker_line_color='white',
                #autocolorscale=True,
                reversescale=True,
                showscale=False,
                colorscale=cs))

fig.update_layout(
                height=500,
                geo={
                    'showframe': False,
                    'showcoastlines': False,
                    'projection': {'type': "miller"}, 
                    "lataxis":dict(range = [-45, 90])
                    },
                margin=
                {"t":0,
                "b":0,
                "r":0,
                "l":0}
                )


# ----------------------------------
# creating cards

card_content_kaggle = [
    dbc.CardHeader("Competition"),
    html.Br(),
    dbc.Row(
        dbc.CardImg(src="/assets/kaggle.png", top=True, bottom=False,
                        title="kaggle", alt='Loading Error', style={'height':'50%', 'width':'50%', },),
        justify="center"),
    dbc.CardBody([
        html.P("This Capstone project is based on a Kaggle Competition launched on 2020/10/14 by the Carbon Disclosure Project. The aim is to promote collaboration between cities and businesses for a socially equitable climate risk mitigation. Through the development of KPIs, actors are to be enabled to optimise their climate protection strategy."),
        dbc.Row([
                dbc.Button("kaggle", href='https://www.kaggle.com/c/cdp-unlocking-climate-solutions', color="primary", className="mr-1", size="lg",
                    style={"font-size": "larger", "text-decoration": "none"}),
                ],
                justify="center"
                )
    ])
]
card_content_neuefische = [
    dbc.CardHeader("Data Science Bootcamp"),
    html.Br(),
    dbc.Row(
        dbc.CardImg(src="/assets/neuefische.svg", top=True, bottom=False,
                            title="bootcamp", alt='Loading Error', style={'height':'70%', 'width':'70%', },),
    justify="center"),
    html.Br(),
    dbc.CardBody([
        html.P("From Sep to Nov 2020,  the project team participated together in a Data Science Coding Bootcamp at Neue Fische. In 720 intensive lessons we learned about the application of machine learning algorithms, neural networks, the Data Science Lifecycle and many other aspects of Date Science. This dashboard serves to present the results of our final Capstone project.  "),
        html.Br(),
        dbc.Row([
                    dbc.Button("neue fische", href='https://www.neuefische.de/', color="primary", className="mr-1", size="lg",
                    style={"font-size": "larger", "text-decoration": "none"}),
                ],
                justify="center"
                )
        ]
    )
]


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
    dbc.CardDeck([
        dbc.Card([
            dbc.CardBody([
                html.H3("Unlocking Climate Solutions", style={"textAlign":"center", "fontWeight":"bold"}),
                html.H5("Indentification of Collaboration opportunities between cities and businesses for socially equitable climate risk mitigation", style={"textAlign":"center"}),
                dcc.Graph(figure=fig),
                html.P("CDP Survey Participants per Country 2018-2020", style={"textAlign":"center"}),
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
        dbc.Col(
            [
            dbc.Card(card_content_neuefische, inverse=False), #color="primary", inverse=True),
            html.Br(),
            dbc.Card(card_content_kaggle), #color="secondary", inverse=True),
            ]
        )

    ])
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
