import geopandas as gpd
from dash import dcc
import dash_bootstrap_components as dbc


resultado = dbc.Container(
    [
        dcc.Graph(
            id="mapa",
            style={
                'width': '100%', 
                "height": "700px"
                }
        )
       
            ]
        )
