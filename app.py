import dash
import dash_bootstrap_components as dbc
import pathlib


# meta_tags are required for the app layout to be mobile responsive

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("./assets").resolve()


app = dash.Dash(__name__, suppress_callback_exceptions=True,
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}],
                external_stylesheets=[dbc.themes.FLATLY]
                            
                )
server = app.server
