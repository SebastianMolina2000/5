import geopandas as gpd
import plotly.express as px
import plotly.graph_objects as go

#importamos el archivo de amenazas en antioquia
amenazas = gpd.read_file('data/amenazas.zip')

#importamos el archivo de divicon politica en antioquia
comunas = gpd.read_file('data/antioquia_divicion.zip')

#importamos el archivo de vias en antioquia
colegios = gpd.read_file('data/colegios.zip')

from backend.col import movimientos_en_masa

def consultarcomuna(comuna_consultada):

    #hacemos consulta de la comuna buscada
    comuna_buscada = comunas.query(f"IDENTIFICA == '{comuna_consultada}'")
    #hacemos la intersección
    incidentes_comuna = gpd.overlay(comuna_buscada , movimientos_en_masa, how='intersection')
    #hacemos busqueda colegio por departamento buscado
    colegios_comuna = colegios
        

    #hacemos un buffer de los rios
    incidentes_comuna["buffer"] = incidentes_comuna.buffer(0.0001)

    #hacemos otra intersección
    colegios_afectados = gpd.overlay(
        colegios_comuna,
        incidentes_comuna.set_geometry("buffer"),
        how='intersection')

    incidentes_comuna_4326= incidentes_comuna.to_crs(epsg=4326)
    incidentes_comuna_4326['buffer'] = incidentes_comuna_4326['buffer'].to_crs(epsg=4326)
    colegios_comuna_4326 = colegios_afectados.to_crs(epsg=4326)


    # Genera mapa de vias
    fig = px.choropleth_mapbox(
        geojson=incidentes_comuna_4326['buffer'].geometry,
        locations=incidentes_comuna_4326.index
    )

    # Agregar rios al mapa
    fig.add_trace(
        go.Scattermapbox(
            lat=colegios_comuna_4326.geometry.y,
            lon=colegios_comuna_4326.geometry.x,
            mode='markers',
            marker=go.scattermapbox.Marker(
                size=9,
                color='red'
            ),
            text=colegios_comuna_4326['NOMBRE_EST'],
            hoverinfo='text'
        )
    )

    # agregamos el mapa
    fig.update_layout(
        mapbox_style="open-street-map",
        mapbox_zoom=11,
        mapbox_center = {"lat": 6.217, "lon": -75.567},
    )
    
    return fig