
import streamlit as st
import leafmap.kepler as leafmap



def app():

    st.title("keplergl")

    m = leafmap.Map(center=[54, -2], zoom=4)
    #gdf = gpd.read_file("/home/ursha/Documents/streamlit/apps/UK_Hex.geojson")
    in_geojson = "https://raw.githubusercontent.com/ursha/streamlit/master/UK_HEX.geojson"
    m.add_geojson(in_geojson, layer_name="Uk HEX")



    m.to_streamlit(height=700)


   
