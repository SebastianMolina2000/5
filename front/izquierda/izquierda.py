import geopandas as gpd
from dash import dcc
import dash_bootstrap_components as dbc


from backend.siniestros import comunas

buscador = dbc.Container(
    [
        dcc.Dropdown(comunas['IDENTIFICA'].unique(), 'Comuna 1' , id='comuna_consultada')
       
            ]
        )
