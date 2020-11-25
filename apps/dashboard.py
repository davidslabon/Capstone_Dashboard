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

country_list = df.country.sort_values().unique()
region_list = df.region.sort_values().unique()

# dashtable dataframe 
tdf = pd.read_pickle(DATA_PATH.joinpath("complete_score.pkl"))
tdf = tdf.loc[:,["entity", "s_score_total", "c_score_total", "o_score_total", "r_score_total", "e_score_total", "em_score_total", "year", "country", "type"]]

# radar dataframe
rdf = pd.read_pickle(DATA_PATH.joinpath("complete_score.pkl")) 

# score definition

all_sub_scores = [
    ['s_score_1', 's_score_2'], # social
    ['c_score_1', 'c_score_2', 'c_score_3', 'c_score_4', 'c_score_5', 'c_score_6'], # collab
    ['o_score_1', 'o_score_2', 'o_score_3', 'o_score_4', 'o_score_5', 'o_score_6', 'o_score_7'], # opportunity 
    ['r_score_1', 'r_score_2', 'r_score_3', 'r_score_5', 'r_score_6', 'r_score_7'],  # risk
    ['e_score_1', 'e_score_2', 'e_score_3', 'e_score_4', 'e_score_6', 'e_score_7', 'e_score_8', 'e_score_9', 'e_score_10', 'e_score_11'], # engagement
    ['em_score_1', 'em_score_2', 'em_score_3', 'em_score_4'] # emissions
    ]

def plot_subscore(data, score_number):
    cols = ["type"] + all_sub_scores[score_number] 
    data = data.loc[:, cols]

    fig = px.bar(data, x="type", y=cols[1:], barmode="group", color_discrete_sequence=cs_new_6)
    fig.update_layout(legend=dict(
        title_text='',
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ),
    xaxis_title = "")

    return fig

# ------------------------------------------------------------------------------
# prepare contents

row1_cards = dbc.CardDeck([
    dbc.Card([
        dbc.CardHeader("Settings"),
        dbc.CardBody([
            dcc.Dropdown(
                id='slct_type', 
                placeholder='Select a type',
                options=[{'label': 'Cities', 'value': 'cities'},
                        {'label': 'Corporates', 'value': 'corporates'}],
                multi=True
            ),
            html.Br(),
            dcc.Dropdown(
                id="slct_region", 
                placeholder='Select a region',
                options=[{"label":x, "value":x} for x in region_list],
                multi=True,
                value="",
            ),
            html.Br(),
            dcc.Dropdown(
                id="slct_country", 
                placeholder='Select a country',
                options=[{"label":x, "value":x} for x in country_list],
                multi=True,
                value="",
            ),
            html.Br(),
            dcc.Dropdown(
                id="slct_year", 
                placeholder='Select a year',
                options=[{"label": "2018", "value": "2018"},
                        {"label": "2019", "value": "2019"},
                        {"label": "2020", "value": "2020"}],
                multi=True,
                value="",
            )
        ])
    ]),
    dbc.Card([
        dbc.CardHeader("Score Dimensions"),
        dcc.Graph(id='score_bar', figure={})
    ]),
    dbc.Card([
        dbc.CardHeader("Total Score Distribution"),
        dcc.Graph(id="total_score", figure={})
    ]),
    dbc.Card([
        dbc.CardHeader("Summary"),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Div(id="avg_score", children=[], style={'fontWeight': 'bold', 'fontSize': 40, "vertical-align": "middle", "text-align":"center"}),
        html.Div("Average Total Score", style={'fontWeight': 'bold', 'fontSize': 20, "vertical-align": "middle", "text-align":"center"}),
        html.Br(),
        html.Br(),
        html.Div(id="no_scores", children=[], style={'fontWeight': 'bold', 'fontSize': 40, "vertical-align": "middle", "text-align":"center"}),
        html.Div("Responses",style={'fontWeight': 'bold', 'fontSize': 20, "vertical-align": "middle", "text-align":"center"}),

    ])
])

row2_cards = dbc.CardDeck([
    dbc.Card([
        dbc.CardHeader("Average Total Score per Country"),
        dbc.CardBody([
            dcc.Graph(id='avg_score_map', figure={})
        ]),        
    ],
    className="w-75"),
    dbc.Card([
        dbc.CardHeader("Highlights / Lowlights"),
        html.Br(),
        html.Div(id="table", children=[]),
        html.Br(),  
    ],
    className="w-25")
])

row3_cards = dbc.CardDeck([
    dbc.Card([
        dbc.CardHeader("Score Radar"),
        dcc.Graph(id="score_radar", figure={})
    ]),
    dbc.Card([
        dbc.CardHeader("Sliders"),
        dbc.CardBody([
            html.P("Social Equity"),
            dcc.RangeSlider(
                id="slct_s_score",
                count=1,
                min=1,
                max=5,
                step=0.5,
                value=[1, 5],
                marks={
                    1: "1",
                    2: "2",
                    3: "3",
                    4: "4",
                    5: "5"
                }
            ),
            html.P("Collaboration"), 
            dcc.RangeSlider(
                id="slct_c_score",
                count=1,
                min=1,
                max=5,
                step=0.5,
                value=[1, 5],
                marks={
                    1: "1",
                    2: "2",
                    3: "3",
                    4: "4",
                    5: "5"
                }
            ),
            html.P("Opportunities"), 
            dcc.RangeSlider(
                id="slct_o_score",
                count=1,
                min=1,
                max=5,
                step=0.5,
                value=[1, 5],
                marks={
                    1: "1",
                    2: "2",
                    3: "3",
                    4: "4",
                    5: "5"
                }
            ),
            html.P("Risks"), 
            dcc.RangeSlider(
                id="slct_r_score",
                count=1,
                min=1,
                max=5,
                step=0.5,
                value=[1, 5],
                marks={
                    1: "1",
                    2: "2",
                    3: "3",
                    4: "4",
                    5: "5"
                }
            ),
            html.P("Engagement"), 
            dcc.RangeSlider(
                id="slct_e_score",
                count=1,
                min=1,
                max=5,
                step=0.5,
                value=[1, 5],
                marks={
                    1: "1",
                    2: "2",
                    3: "3",
                    4: "4",
                    5: "5"
                }   
            ),
            html.P("Emissions"), 
            dcc.RangeSlider(
                id="slct_em_score",
                count=1,
                min=1,
                max=5,
                step=0.5,
                value=[1, 5],
                marks={
                    1: "1",
                    2: "2",
                    3: "3",
                    4: "4",
                    5: "5"
                }
            )
        ])
    ]),
    dbc.Card([
        dbc.CardHeader("No of results"),
        html.P("Cities:"),
        html.Div(id="city_results", children=[]),
        html.P("Corporates:"),
        html.Div(id="corporate_results", children=[])
    ]),
])

row4_cards = dbc.CardGroup([
    dbc.Card([
        dbc.CardHeader("Social"),
        dcc.Graph(id="s_score", figure={})
    ]),
        dbc.Card([
        dbc.CardHeader("Collaboration"),
        dcc.Graph(id="c_score", figure={})
    ]),
        dbc.Card([
        dbc.CardHeader("Opportunities"),
        dcc.Graph(id="o_score", figure={})
    ]),
        dbc.Card([
        dbc.CardHeader("Risks"),
        dcc.Graph(id="r_score", figure={})
    ]),
        dbc.Card([
        dbc.CardHeader("Engagement"),
        dcc.Graph(id="e_score", figure={})
    ]),
        dbc.Card([
        dbc.CardHeader("Emissions"),
        dcc.Graph(id="em_score", figure={})
    ])
])






# ------------------------------------------------------------------------------
# App layout

layout = html.Div([
    navbar.navbar(),
    html.Br(),
    html.H1("Overview"),
    row1_cards,
    html.Br(),
    row2_cards,
    html.Br(),
    html.H1("Dependencies"),
    row3_cards,
    html.Br(),
    row4_cards,
    html.Br(),
    html.H1("Detailed Comparison"),
])





# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    [Output(component_id='score_bar', component_property='figure'),
     Output(component_id='total_score', component_property='figure'),
     Output(component_id='avg_score', component_property='children'),
     Output(component_id='no_scores', component_property='children'),
     Output(component_id='avg_score_map', component_property='figure'),
     Output(component_id='table', component_property='children')],
    [Input(component_id='slct_type', component_property='value'),
     Input(component_id='slct_country', component_property='value'),
     Input(component_id='slct_year', component_property='value'),
     Input(component_id='slct_region', component_property='value')]
)

def update_graphs(*option_slctd):
   
    dff = df.copy()
    if option_slctd[2]:
        dff = dff[dff["year"].isin( option_slctd[2])] 
    if option_slctd[1]:
        dff = dff[dff["country"].isin(option_slctd[1])] 
    if option_slctd[0]:
        dff = dff[dff["type"].isin(option_slctd[0])]
    if option_slctd[3]:
        dff = dff[dff["region"].isin(option_slctd[3])]

    gob = dff.groupby(["year"])[[
                            's_score_total', 
                            'c_score_total', 
                            'o_score_total', 
                            'r_score_total', 
                            'e_score_total', 
                            'em_score_total']
                            ].mean()
    gob.reset_index(inplace=True)
    
    # id: 'score_bar' -> plot bar_chart
    fig_bar = go.Figure(
        data=[
            go.Bar(name="S", x=gob["year"], y=gob["s_score_total"], marker_color=cs_new_6[0]),
            go.Bar(name="C",x=gob["year"], y=gob["c_score_total"], marker_color=cs_new_6[1]),
            go.Bar(name="O",x=gob["year"], y=gob["o_score_total"], marker_color=cs_new_6[2]),
            go.Bar(name="R",x=gob["year"], y=gob["r_score_total"], marker_color=cs_new_6[3]),
            go.Bar(name="E",x=gob["year"], y=gob["e_score_total"], marker_color=cs_new_6[4]),
            go.Bar(name="E2", x=gob["year"], y=gob["em_score_total"], marker_color=cs_new_6[5]),
        ],
    )

    fig_bar.update_layout(
        barmode="group",
        margin=dict(
                    l=10,
                    r=0,
                    b=70,
                    t=50,
                    pad=10
                    ),
        #paper_bgcolor="#f1f5eb",
        template="simple_white",
        )
    

    # id: 'total_score' -> plot donut pie
    dff["score_total"] = dff.loc[:,"s_score_total":"em_score_total"].mean(axis=1)
    score_bins = pd.cut(x = dff.score_total, bins=[0,1.5,2.5,3.5,4.5,6], labels=["1","2","3","4","5"])
    score_bins = round((score_bins.value_counts(normalize=True)*100),1)
    score_bins = score_bins.sort_index()
  
    labels = ['1','2','3','4','5']
    values = score_bins.values

    
    fig_donut = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3, sort=False, marker={"colors":cs_new_5})])
    #fig_donut.update_layout(color_discrete_sequence=px.colors.sequential.RdBu)
    


    # id: 'avg_score' -> plot stacked missings
    avg_score = round(dff.score_total.mean(),2)
    no_scores = dff.score_total.dropna()
    no_scores = len(no_scores)


    # id: 'avg_score_map' -> plot map viz


    fig_map = go.Figure(data=go.Choropleth(locations=dff['alpha3code'],z=dff["score_total"],
                #hoverinfo="text",
                marker_line_color='white',
                autocolorscale=True,
                reversescale=False,
                showscale=False,
                colorscale="agsunset"))

    fig_map.update_layout(
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


    
    # id="top_table, flop_table" -> create simple data_table

    tdff = tdf.copy()
    if option_slctd[2]:
        tdff = tdff[tdff["year"].isin(option_slctd[2])] 
    if option_slctd[1]:
        tdff = tdff[tdff["country"].isin(option_slctd[1])] 
    if option_slctd[0]:
        tdff = tdff[tdff["type"].isin(option_slctd[0])] 

    tdff["score_total"] = round(tdff.loc[:,"s_score_total":"em_score_total"].mean(axis=1), 2)
    tdff = tdff.dropna(axis="rows", subset=["score_total"])
    tdff.sort_values(by="score_total", ascending=False, inplace=True)
    top_df = tdff.head(3).loc[:, ["entity", "country", "year", "score_total"]]
    top_df.rename(columns={"entity":"Entity", "score_total":"Total Score", "country":"Country", "year":"Year"}, inplace=True)
    
    line = pd.DataFrame({"Entity":"...", "Country":"...", "Year":"...", "Total Score":"..."}, index =[3])
    
    flop_df = tdff.tail(3).loc[:, ["entity", "country", "year", "score_total"]]
    flop_df.rename(columns={"entity":"Entity", "score_total":"Total Score", "country":"Country", "year":"Year"}, inplace=True)
    
    result_df = pd.concat([top_df, line, flop_df])
    table = dbc.Table.from_dataframe(result_df, striped=True, bordered=True, hover=True, size="sm")

    return fig_bar, fig_donut, avg_score, no_scores, fig_map, table


    

@app.callback([Output(component_id='score_radar', component_property='figure'),
    Output(component_id='city_results', component_property='children'),
    Output(component_id='corporate_results', component_property='children'),
    Output(component_id='s_score', component_property='figure'),
    Output(component_id='c_score', component_property='figure'),
    Output(component_id='o_score', component_property='figure'),
    Output(component_id='r_score', component_property='figure'),
    Output(component_id='e_score', component_property='figure'),
    Output(component_id='em_score', component_property='figure')],   
    [Input(component_id='slct_s_score', component_property='value'),
    Input(component_id='slct_c_score', component_property='value'),
    Input(component_id='slct_o_score', component_property='value'),
    Input(component_id='slct_r_score', component_property='value'),
    Input(component_id='slct_e_score', component_property='value'),
    Input(component_id='slct_em_score', component_property='value')]

)

def update_radar(*option_slctd):
    
    rdff = rdf.copy() 
    rdff = rdff.query(
        "(type=='cities'\
        &s_score_total >= @option_slctd[0][0] & s_score_total <= @option_slctd[0][1]\
        & c_score_total >= @option_slctd[1][0] & c_score_total <= @option_slctd[1][1]\
        & o_score_total >= @option_slctd[2][0] & o_score_total <= @option_slctd[2][1]\
        & r_score_total >= @option_slctd[3][0] & r_score_total <= @option_slctd[3][1]\
        & e_score_total >= @option_slctd[4][0] & e_score_total <= @option_slctd[4][1]\
        & em_score_total >= @option_slctd[5][0] & em_score_total <= @option_slctd[5][1])|\
        (type=='corporates'\
        &c_score_total >= @option_slctd[1][0] & c_score_total <= @option_slctd[1][1]\
        & o_score_total >= @option_slctd[2][0] & o_score_total <= @option_slctd[2][1]\
        & r_score_total >= @option_slctd[3][0] & r_score_total <= @option_slctd[3][1]\
        & e_score_total >= @option_slctd[4][0] & e_score_total <= @option_slctd[4][1]\
        & em_score_total >= @option_slctd[5][0] & em_score_total <= @option_slctd[5][1])"
        )

    ci_gob = rdff.query("type=='cities'").loc[:, "s_score_total":"em_score_total"]
    ci_results = len(ci_gob)
    ci_gob = ci_gob.mean()

    co_gob = rdff.query("type=='corporates'").loc[:, "s_score_total":"em_score_total"]
    co_results = len(co_gob)
    co_gob = co_gob.fillna(0)
    co_gob = co_gob.mean()

    fig_radar = go.Figure()
    
    fig_radar.add_trace(go.Scatterpolar(
        r = ci_gob.values.flatten(),
        theta=['Social Equity', 'Collaboration', 'Opportunities', 'Risks',
                'Engagement', 'Emissions'],
        fill='toself',
        name='cities',
        marker_color=cs_new_6[0]
        ))

    fig_radar.add_trace(go.Scatterpolar(
        r = co_gob.values.flatten(),
        theta=['Social Equity', 'Collaboration', 'Opportunities', 'Risks',
                'Engagement', 'Emissions'],
        fill='toself',
        name='corporates',
        marker_color=cs_new_6[4]
        ))
    

    fig_radar.update_layout(
    polar=dict(
        radialaxis=dict(
        visible=True,
        range=[1,5]
        ),
    ),
    showlegend=True
    )


# group df for subscore plotting

    gob = rdff.groupby("type").mean()
    gob = gob.reset_index()

# id: "s_score:em_score" -> plot sub_scores
    fig_s_score = plot_subscore(gob, 0)
    fig_c_score = plot_subscore(gob, 1)
    fig_o_score = plot_subscore(gob, 2)
    fig_r_score = plot_subscore(gob, 3)
    fig_e_score = plot_subscore(gob, 4)
    fig_em_score = plot_subscore(gob, 5)




    return fig_radar, ci_results, co_results, fig_s_score, fig_c_score, fig_o_score, fig_r_score, fig_e_score, fig_em_score