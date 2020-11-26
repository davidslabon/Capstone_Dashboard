import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import dash_table
import pathlib
from app import app
from apps import navbar

# -----------------------------------------------------------------------------
# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()
cs = [[0, "rgb(207, 219, 206)"],[1, "rgb(53, 66, 52)"]]
cs_new_6 = ['#0d0887', '#7201a8', '#bd3786', '#ed7953', '#fb9f3a', '#f0f921']
cs_new_5 = ['#0d0887', '#7201a8', '#bd3786', '#ed7953', '#f0f921']

df = pd.read_pickle(DATA_PATH.joinpath("complete_score.pkl")) 
empty_gob = pd.read_csv(DATA_PATH.joinpath("empty_gob.csv"), delimiter=";")

country_list = df.country.sort_values().unique()
region_list = df.region.sort_values().unique()
entity_list = df.entity.sort_values().unique()

# -----------------------------------------------------------------------------
# create contentt

row1_cards = dbc.CardDeck([
    dbc.Card([
        dbc.CardHeader("Left"),
        dbc.CardBody([
            html.P("Please select ONE option!"),
            dcc.Dropdown(
                id="slct_region_l", 
                placeholder='Select a region',
                options=[{"label":x, "value":x} for x in region_list],
                multi=False,
                value="",
            ),
            html.Br(),
            dcc.Dropdown(
                id="slct_country_l", 
                placeholder='Select a country',
                options=[{"label":x, "value":x} for x in country_list],
                multi=False,
                value="",
            ),
            html.Br(),
            dcc.Dropdown(
                id="slct_entity_l", 
                placeholder='Select an entity',
                options=[{"label":x, "value":x} for x in entity_list],
                multi=False,
                value="",
            ),
        ])
    ]),
    dbc.Card([
        dbc.CardHeader("Right"),
        dbc.CardBody([
            html.P("Please select ONE option!"),
            dcc.Dropdown(
                id="slct_region_r", 
                placeholder='Select a region',
                options=[{"label":x, "value":x} for x in region_list],
                multi=False,
                value="",
            ),
            html.Br(),
            dcc.Dropdown(
                id="slct_country_r", 
                placeholder='Select a country',
                options=[{"label":x, "value":x} for x in country_list],
                multi=False,
                value="",
            ),
            html.Br(),
            dcc.Dropdown(
                id="slct_entity_r", 
                placeholder='Select an entity',
                options=[{"label":x, "value":x} for x in entity_list],
                multi=False,
                value="",
            ),
        ])
    ]),
 dbc.Card([
        dbc.CardHeader("Period"),
        dbc.CardBody([
            html.Br(),
            dcc.Checklist(
                id="slct_year",
                options=[
                    {'label': '2018', 'value': '2018'},
                    {'label': '2019', 'value': '2019'},
                    {'label': '2020', 'value': '2020'}
                ],
                value=['2018', '2019', '2020'],
                #labelStyle={'display': 'inline-block'}
            )  
        
        ])
    ]),
])


row2_cards = dbc.CardDeck([
    dbc.Card([
        dbc.CardHeader("Comparison"),
        dbc.CardBody([
            html.Br(),
            dcc.Graph(id='h2h_bar', figure={})
        ])
    ]),
])
# -----------------------------------------------------------------------------
# app_layout

layout = html.Div([
    navbar.navbar(),
    html.Br(),
    html.H3("Head-to-head", style={'fontWeight': 'bold'}),
    row1_cards,
    html.Br(),
    row2_cards
])

# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    Output(component_id='h2h_bar', component_property='figure'),
    [Input(component_id='slct_region_l', component_property='value'),
    Input(component_id='slct_country_l', component_property='value'),
    Input(component_id='slct_entity_l', component_property='value'),
    Input(component_id='slct_region_r', component_property='value'),
    Input(component_id='slct_country_r', component_property='value'),
    Input(component_id='slct_entity_r', component_property='value'),
    Input(component_id='slct_year', component_property='value')])

def update_graphs(*option_slctd):

    dff = df.copy()

    if option_slctd[6]:
        dff = dff[dff["year"].isin( option_slctd[6])] 

    ldf = dff.copy()
    rdf = dff.copy()

    if option_slctd[0]:
        ldf = ldf[ldf["region"] == option_slctd[0]]
        ldf = ldf.groupby("region").mean()
        ldf["head"] =  option_slctd[0]
    if option_slctd[1]:
        ldf = ldf[ldf["country"] == option_slctd[1]] 
        ldf = ldf.groupby("country").mean()
        ldf["head"] =  option_slctd[1]
    if option_slctd[2]:
        ldf = ldf[ldf["entity"] == option_slctd[2]]
        ldf = ldf.groupby("entity").mean() 
        ldf["head"] =  option_slctd[2]
    ldf = ldf.reset_index()
    

    if option_slctd[3]:
        rdf = rdf[rdf["region"] == option_slctd[3]]
        rdf = rdf.groupby("region").mean()
        rdf["head"] =  option_slctd[3] 
    if option_slctd[4]:
        rdf = rdf[rdf["country"] == option_slctd[4]] 
        rdf = rdf.groupby("country").mean()
        rdf["head"] =  option_slctd[4] 
    if option_slctd[5]:
        rdf = rdf[rdf["entity"] == option_slctd[5]]
        rdf = rdf.groupby("entity").mean() 
        rdf["head"] =  option_slctd[5] 
    rdf = rdf.reset_index()



    data = pd.concat([ldf, rdf])
    
    if len(data) > 3:
        data = empty_gob
        data["head"] = "tbd"

   
    fig = px.bar(
        data, 
        x="head", 
        y=["s_score_total", "c_score_total", "o_score_total", "r_score_total", "e_score_total", "em_score_total"], 
        barmode="group",
        color_discrete_sequence=cs_new_6, 
        range_y=(0,5))

    fig.update_layout(legend=dict(
        title_text='',
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ),
    xaxis_title = None,
    yaxis_title = None,
    margin={
        "l":0,
        "r":5,
        "b":0
    },
    template="simple_white")
    return fig

   
  
