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

df = pd.read_pickle(DATA_PATH.joinpath("dummy_df.pkl"))  
print(df.columns)
# ------------------------------------------------------------------------------
# create page content

cards_team = dbc.CardDeck([
    dbc.Card(
        [
            dbc.CardImg(src="/assets/picture_david.jpeg", top=True, bottom=False,
                        title="David Slabon", alt='Loading Error'),
            dbc.CardBody(
                [
                    html.H5("David Slabon", className="card-title"),
                    dbc.CardLink("GitHub", href="https://github.com/davidslabon", target="_blank"),
                    dbc.CardLink("LinkedIn", href="https://www.linkedin.com/in/dslabon", target="_blank"),
                    dbc.CardLink("TalentApp", href="https://talents.neuefische.com/student/0ec00874-a6c0-4b9a-bf84-f51223318cb1", target="_blank")
                                ],
            ),
        ],
            #color="grey",   # https://bootswatch.com/default/ for more card colors
            #inverse=True,   # change color of text (black or white)
            #outline=False,  # True = remove the block colors from the background and header
            className="card text-white bg-primary mb-3"
    ),
    dbc.Card(
        [
            dbc.CardImg(src="/assets/picture_felix.jpeg", top=True, bottom=False,
                        title="Felix Seeliger", alt='Loading Error'),
            dbc.CardBody(
                [
                    html.H5("Felix Seeliger", className="card-title"),
                    dbc.CardLink("GitHub", href="https://github.com/Felixxxxxxxxxxx", target="_blank"),
                    dbc.CardLink("LinkedIn", href="https://www.linkedin.com/in/felixseeliger/", target="_blank"),
                    dbc.CardLink("TalentApp", href="https://talents.neuefische.com/student/3b74bfdb-7709-4cd9-977a-faa2ae9c4cfd", target="_blank")
                                ]
            ),
        ],
            className="card text-white bg-primary mb-3"
    ),     
    dbc.Card(
        [
            dbc.CardImg(src="/assets/picture_olaf.jpeg", top=True, bottom=False,
                        title="Olaf Steenbeck", alt='Loading Error'),
            dbc.CardBody(
                [
                    html.H5("Olaf Steenbeck", className="card-title"),
                    dbc.CardLink("GitHub", href="https://github.com/osteenbeck", target="_blank"),
                    dbc.CardLink("LinkedIn", href="https://www.linkedin.com/in/olaf-steenbeck-9349751b5/", target="_blank"),
                    dbc.CardLink("TalentApp", href="https://talents.neuefische.com/student/628f1f4f-efb4-4d2a-b54b-4fc11e60a615", target="_blank")
                                ]
            ),
        ],
        className="card text-white bg-primary mb-3"
    ),
    dbc.Card(
        [
            dbc.CardImg(src="/assets/picture_tobias.jpeg", top=True, bottom=False,
                        title="Tobias Seidel", alt='Loading Error'),
            dbc.CardBody(
                [
                    html.H5("Tobias Seidel", className="card-title"),
                    dbc.CardLink("GitHub", href="https://github.com/Toseidel", target="_blank"),
                    dbc.CardLink("LinkedIn", href="https://www.linkedin.com/in/tobias-seidel/", target="_blank"),
                    dbc.CardLink("TalentApp", href="https://talents.neuefische.com/student/656fb95c-f3ed-4892-9561-6fc58f6b0aca", target="_blank")
                                ]
            ),
        ],
        className="card text-white bg-primary mb-3"
        ),
    ],
    #color="dark",   # https://bootswatch.com/default/ for more card colors
    #inverse=False,   # change color of text (black or white)
    #outline=True,  # True = remove the block colors from the background and header
)

# ------------------------------------------------------------------------------

# App layout

layout = html.Div([
    navbar.navbar(),
    html.Br(),
    dbc.Row([
        html.Div(
            children = """This interaktiv dashboards allows users to explore the 
                            capstone results of Felix, Olaf, Tobi and David. For further 
                            information please visit us on GitHub: 
                            https://github.com/davidslabon/Capstone_UnlockingClimateSolutions.""",
            style = {"padding-left": "3%"}       
        ),
    ]),
    html.Br(),
    dbc.Row(
        dbc.Col(
            html.Div([
                dash_table.DataTable(
                    id='datatable-interactivity',
                    columns=[
                        {"name": i, "id": i, "deletable": False, "selectable": True, "hideable": True}
                        if i == "alpha3code" or i == "year" or i == "type"
                        else {"name": i.title().replace("_"," "), "id": i, "deletable": True, "selectable": True}
                        for i in ['theme', 'account_number', 'public', 'entity',
                        'country', 'region', 'population', 'city', 
                        'authority_types', 'activities','s_score',
                        'c_score', 'o_score', 'r_score', 'e_score', 'e2_score', 'total']
                    ],
                    data=df.to_dict('records'),  # the contents of the table
                    editable=True,              # allow editing of data inside all cells
                    #filter_action="native",     # allow filtering of data by user ('native') or not ('none')
                    sort_action="native",       # enables data to be sorted per-column by user or not ('none')
                    #sort_mode="single",         # sort across 'multi' or 'single' columns
                    column_selectable="multi",  # allow users to select 'multi' or 'single' columns
                    #row_selectable="multi",     # allow users to select 'multi' or 'single' rows
                    #row_deletable=True,         # choose if user can delete a row (True) or not (False)
                    selected_columns=[],        # ids of columns that user selects
                    selected_rows=[],           # indices of rows that user selects
                    page_action="native",       # all data is passed to the table up-front or not ('none')
                    page_current=0,             # page number that user is on
                    page_size=10,                # number of rows visible per page
                    style_cell={                # ensure adequate header width when text is shorter than cell's text
                        #'minWidth': 10, 
                        'maxWidth': 95, 
                        'width': "auto", 
                        "textAlign": "left",
                        'font-family':'sans-serif'
                    },
                    style_cell_conditional=[    # align text columns to left. By default they are aligned to right
                        {
                        'if': {'column_id': c},
                        #'minWidth': 10, 
                        'maxWidth': 95, 
                        'width': "auto", 
                        'textAlign': 'left'
                        } for c in ['entity']
                    ],
                    style_data={                # overflow cells' content into multiple lines
                        'whiteSpace': 'normal',
                        'height': 'auto',
                        'width': 'auto',
                        'margin':
                        {"l":10, "r":10}
                    },
                    style_as_list_view=False, 
                    style_table={'overflowX': 'auto', "padding":"10px 20px 20px 20px"} 
                ),
            ]),
        #width={"size": 10, "offset": 1}
        )
    ),
    dbc.Row(cards_team),
])

