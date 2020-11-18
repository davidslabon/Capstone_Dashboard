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
])

