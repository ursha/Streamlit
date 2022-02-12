
import streamlit as st
import leafmap.kepler as leafmap
import geopandas as gpd


def app():

    st.title("keplergl")

    m = leafmap.Map(center=[50, -2], zoom=5)
    gdf = gpd.read_file("https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/world_cities.geojson")

    m.add_gdf(gdf, layer_name="Countries")
    m.to_streamlit(height=700)



    
    # read geojson
    #df = gpd.read_file('/home/ursha/Documents/kepler.gl\Hex_GlocationFull_UK.geojson')
    
   