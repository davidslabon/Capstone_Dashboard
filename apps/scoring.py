import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import pathlib
from app import app
from apps import navbar

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()


layout = html.Div([
    navbar.navbar(),
    html.H1('Unlocking Climate Solutions', style={"textAlign": "center"}),
    dbc.Row([
        html.Br(),
        html.Div(
            children = """This interaktiv dashboards allows users to explore the 
                            capstone results of Felix, Olaf, Tobi and David. For further 
                            information please visit us on GitHub: 
                            https://github.com/davidslabon/Capstone_UnlockingClimateSolutions.""",
            style = {"padding-left": "3%"}       
        ),
        html.Br()
    ]),
])

