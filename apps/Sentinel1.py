import streamlit as st
import leafmap.kepler as leafmap
import datetime



def app():
    st.title("Sentinel 1")
    d = st.date_input(
        "Select the Date",
        datetime.date(2016, 7, 6))
    st.write('Date Selected:', d)
    m = leafmap.Map(center=[54, -2], zoom=1)
    m.to_streamlit(height=700)
    




# def app():

#     st.title("Sentinel 1")

#     m = leafmap.Map(center=[54, -2], zoom=1)
#     m.to_streamlit(height=700)
    
    
    
    #st.write('Date Selected:', d)