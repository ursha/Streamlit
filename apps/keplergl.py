import pandas as pd 
import geopandas as gpd
import keplergl

def app():

    st.title("Kepler.gl")

    Kmap = keplergl.KeplerGl(height=600)
    # read geojson
    df = gpd.read_file('https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/cable-geo.geojson')

    in_geojson = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/cable-geo.geojson'
    Kmap.add_data(data=df, name='HEX')
    #Plot Kmap
    Kmap
    Kmap.to_streamlit(height=700)
