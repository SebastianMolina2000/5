import geopandas as gpd
from dash import Dash, html,dcc, callback, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px

#importamos el archivo de vias en antioquia
amenazas = gpd.read_file('data/amenazas.zip')

#agrupamos y solucionamos el error que se tiene 
amenazas["amenzas_naturales"] = amenazas["TIPO_AMENA"].replace(['Inundaciones','Avenidas Torrenciales'], 'Movimientos en masa')

#nuestra base de datos tomara 'TIPO_AMENA' == 'Movimientos en masa'
movimientos_en_masa=amenazas.query("amenzas_naturales == 'Movimientos en masa'") 


