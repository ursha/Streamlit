import streamlit as st
import leafmap.kepler as leafmap



def app():

    st.title("Sentinel 1")

    m = leafmap.Map(center=[54, -2], zoom=1)
    m.to_streamlit(height=700)