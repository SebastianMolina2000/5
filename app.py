import geopandas as gpd
from dash import Dash, html,dcc, callback, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

#importamos back
from backend.siniestros import consultarcomuna
from front.principal.principal import navegador
from front.izquierda.izquierda import buscador
from front.derecha.derecha import resultado

#App layout
app.layout = dbc.Container(
    [
          dbc.Row(
            [
                dbc.Col(navegador, md=12 ),
                dbc.Col(buscador, md=4),
                dbc.Col(resultado, md=8),
                
            ]
        ),
        
    ],
    fluid=True
)

@callback(
    Output("mapa", "figure"),
    Input("comuna_consultada", "value")
)

def update_map(comuna_consultada):
    return consultarcomuna(comuna_consultada)


if __name__ == "__main__":
    app.run_server(debug=True)