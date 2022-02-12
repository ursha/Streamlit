import streamlit as st
import leafmap.foliumap as leafmap


def app():

    st.title("Vector")

    m = leafmap.Map(center=[0, 0], zoom=2)

    in_geojson = '/home/ursha/Documents/streamlit/Hex_GlocationFull_UK.geojson'
    m.add_geojson(in_geojson, layer_name="Cable lines")
    m.to_streamlit(height=700)
