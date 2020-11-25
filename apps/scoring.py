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
                        title="David Slabon", alt='Loading Error'),
            dbc.CardBody(
                [
                    dbc.CardLink("GitHub", href="https://github.com/davidslabon", target="_blank"),
                    dbc.CardLink("LinkedIn", href="https://www.linkedin.com/in/dslabon", target="_blank"),
                    dbc.CardLink("TalentApp", href="https://talents.neuefische.com/student/0ec00874-a6c0-4b9a-bf84-f51223318cb1", target="_blank")
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
                    dbc.CardLink("GitHub", href="https://github.com/Felixxxxxxxxxxx", target="_blank"),
                    dbc.CardLink("LinkedIn", href="https://www.linkedin.com/in/felixseeliger/", target="_blank"),
                    dbc.CardLink("TalentApp", href="https://talents.neuefische.com/student/3b74bfdb-7709-4cd9-977a-faa2ae9c4cfd", target="_blank")
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
                    dbc.CardLink("GitHub", href="https://github.com/osteenbeck", target="_blank"),
                    dbc.CardLink("LinkedIn", href="https://www.linkedin.com/in/olaf-steenbeck-9349751b5/", target="_blank"),
                    dbc.CardLink("TalentApp", href="https://talents.neuefische.com/student/628f1f4f-efb4-4d2a-b54b-4fc11e60a615", target="_blank")
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
                    dbc.CardLink("GitHub", href="https://github.com/Toseidel", target="_blank"),
                    dbc.CardLink("LinkedIn", href="https://www.linkedin.com/in/tobias-seidel/", target="_blank"),
                    dbc.CardLink("TalentApp", href="https://talents.neuefische.com/student/656fb95c-f3ed-4892-9561-6fc58f6b0aca", target="_blank")
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

card_content_4 = [
    dbc.CardHeader("Data Science Bootcamp"),
    html.Br(),
    dbc.CardImg(src="/assets/neuefische.svg", top=True, bottom=False,
                        title="bootcamp", alt='Loading Error', style={'height':'100%', 'width':'100%', },),
    dbc.CardBody(
        html.P("bla, bla, bla")
    )
]

card_content_6 = [
    dbc.CardHeader("Tools & Packages"),
    html.Br(),
    dbc.CardImg(src="/assets/tools.png", top=True, bottom=False,
                        title="tools", alt='Loading Error', style={'height':'100%', 'width':'100%', },),
    dbc.CardBody(
        html.P("bla, bla, bla")
    )
]

cards = dbc.CardColumns(
    [
        dbc.Card(card_content_1, inverse=False), #color="primary", inverse=True),
        dbc.Card(card_content_3), #color="secondary", inverse=True),
        dbc.Card(card_content_4),
        dbc.Card(card_content_6, style={"width": "100%"}),
        
    ]
)
#=======================
# ------------------------------------------------------------------------------

# App layout

layout = html.Div([
    navbar.navbar(),
    html.Br(),
    html.H1("Background Information"),
    html.Br(),
    cards,
    html.Br(),
    html.H1("Project Team"),
    html.Br(),
    dbc.Row(cards_team),
])

