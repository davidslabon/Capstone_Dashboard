import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import dash_table

import plotly.express as px
import pandas as pd
import pathlib
from app import app
from apps import navbar

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

df = pd.read_csv(DATA_PATH.joinpath("score_descriptions.csv")) 
df = df.loc[:, ["score", "s_type", "score_short_desc"]]
df.rename(columns={"score":"Score", "score_short_desc":"Short Description"}, inplace=True)

ciq = df.query("s_type == 'cities'").loc[:,["Score", "Short Description"]]
coq = df.query("s_type == 'corporates'").loc[:,["Score", "Short Description"]]



# ------------------------------------------------------------------------------
# create page content

cards_team = dbc.CardDeck([
    dbc.Card(
        [   dbc.CardHeader("David Slabon"),
            dbc.CardImg(src="/assets/picture_david.jpeg", top=True, bottom=False,
                        title="David Slabon", alt='Loading Error', ),
            dbc.CardBody(
                [
            dbc.Row([
                    dbc.Button("GitHub", href='https://github.com/davidslabon', color="primary", className="mr-1", size="lg",
                    style={"font-size": "larger", "text-decoration": "none"}),
                    dbc.Button("LinkedIn", href='https://www.linkedin.com/in/dslabon', color="primary", className="mr-1", size="lg",
                    style={"font-size": "larger", "text-decoration": "none"}),
                    dbc.Button("TalentApp", href="https://talents.neuefische.com/student/0ec00874-a6c0-4b9a-bf84-f51223318cb1", color="primary", className="mr-1", size="lg",
                    style={"font-size": "larger", "text-decoration": "none"}),
                ],
                justify="center"
                ),
            ],
            ),
        ],
            #color="grey",   # https://bootswatch.com/default/ for more card colors
            #inverse=True,   # change color of text (black or white)
            #outline=False,  # True = remove the block colors from the background and header
    ),
    dbc.Card(
        [   dbc.CardHeader("Felix Seeliger"),
            dbc.CardImg(src="/assets/picture_felix.jpeg", top=True, bottom=False,
                        title="Felix Seeliger", alt='Loading Error'),
            dbc.CardBody(
                [
                dbc.Row([
                    dbc.Button("GitHub", href='https://github.com/Felixxxxxxxxxxx', color="primary", className="mr-1", size="lg",
                    style={"font-size": "larger", "text-decoration": "none"}),
                    dbc.Button("LinkedIn", href='https://www.linkedin.com/in/felixseeliger/', color="primary", className="mr-1", size="lg",
                    style={"font-size": "larger", "text-decoration": "none"}),
                    dbc.Button("TalentApp", href="https://talents.neuefische.com/student/3b74bfdb-7709-4cd9-977a-faa2ae9c4cfd", color="primary", className="mr-1", size="lg",
                    style={"font-size": "larger", "text-decoration": "none"}),
                ],
                justify="center"
                ),
                ]
            ),
        ],
    ),     
    dbc.Card(
        [   dbc.CardHeader("Olaf Steenbeck"),
            dbc.CardImg(src="/assets/picture_olaf.jpeg", top=True, bottom=False,
                        title="Olaf Steenbeck", alt='Loading Error'),
            dbc.CardBody(
                [
                dbc.Row([
                    dbc.Button("GitHub", href='https://github.com/osteenbeck', color="primary", className="mr-1", size="lg",
                    style={"font-size": "larger", "text-decoration": "none"}),
                    dbc.Button("LinkedIn", href='https://www.linkedin.com/in/olaf-steenbeck-9349751b5//', color="primary", className="mr-1", size="lg",
                    style={"font-size": "larger", "text-decoration": "none"}),
                    dbc.Button("TalentApp", href="https://talents.neuefische.com/student/628f1f4f-efb4-4d2a-b54b-4fc11e60a615", color="primary", className="mr-1", size="lg",
                    style={"font-size": "larger", "text-decoration": "none"}),
                ],
                justify="center"
                ),
                ]
            ),
        ],
    ),
    dbc.Card(
        [   dbc.CardHeader("Tobias Seidel"),
            dbc.CardImg(src="/assets/picture_tobias.jpeg", top=True, bottom=False,
                        title="Tobias Seidel", alt='Loading Error'),
            dbc.CardBody(
                [
                dbc.Row([
                    dbc.Button("GitHub", href='https://github.com/Toseidel', color="primary", className="mr-1", size="lg",
                    style={"font-size": "larger", "text-decoration": "none"}),
                    dbc.Button("LinkedIn", href='https://www.linkedin.com/in/tobias-seidel/', color="primary", className="mr-1", size="lg",
                    style={"font-size": "larger", "text-decoration": "none"}),
                    dbc.Button("TalentApp", href="https://talents.neuefische.com/student/656fb95c-f3ed-4892-9561-6fc58f6b0aca", color="primary", className="mr-1", size="lg",
                    style={"font-size": "larger", "text-decoration": "none"}),
                ],
                justify="center"
                ),
                ]
            ),
        ],
        ),
    ],
    #color="dark",   # https://bootswatch.com/default/ for more card colors
    #inverse=False,   # change color of text (black or white)
    #outline=True,  # True = remove the block colors from the background and header
)
# ======================

card_content_1 = [
    dbc.CardHeader("City Scoring"),
    dbc.CardBody(
        [   
            dbc.Table.from_dataframe(ciq, striped=True, bordered=True, hover=True, size="sm", dark=False),
        ]
    ),
]


card_content_3 = [
    dbc.CardHeader("Corporate Scoring"),
    dbc.CardBody(   
            dbc.Table.from_dataframe(coq, striped=True, bordered=True, hover=True, size="sm")
            )
]

card_content_cdp = [
    dbc.CardHeader("The Dataset"),
    dbc.Row(
        dbc.CardImg(src="/assets/cdp.png", top=True, bottom=False,
                            title="bootcamp", alt='Loading Error', style={'height':'70%', 'width':'70%', },),
    justify="center"),
    dbc.CardBody([
        html.P("The Carbon Disclosure Project(CDP) is a non-profit charity that runs a global disclosure system for investors, companies and cities to manage their environmental impact. We've worked on the world's largest survey on environemtal actions. The provided data sets contain approximately 4 million survey responses."),
        dbc.Row([
                    dbc.Button("CDP", href='https://www.cdp.net/en', color="primary", className="mr-1", size="lg",
                    style={"font-size": "larger", "text-decoration": "none"}),
                ],
                justify="center"
                )
        ]
    )
]

card_content_tools = [
    dbc.CardHeader("Tools & Packages"),
    html.Br(),
    dbc.CardImg(src="/assets/tools.png", top=True, bottom=False,
                        title="tools", alt='Loading Error', style={'height':'100%', 'width':'100%', },)
]

cards = dbc.CardColumns(
    [
        dbc.Card(card_content_1, inverse=False), #color="primary", inverse=True),
        dbc.Card(card_content_3), #color="secondary", inverse=True),
        dbc.Card(card_content_tools),
        dbc.Card(card_content_cdp, style={"width": "100%"}),
        
    ]
)
#=======================
# ------------------------------------------------------------------------------

# App layout

layout = html.Div([
    navbar.navbar(),
    html.Br(),
    html.H3("Background Information", style={'fontWeight': 'bold'}),
    cards,
    html.Br(),
    html.H3("Project Team", style={'fontWeight': 'bold'}),
    dbc.Row(cards_team),
])

