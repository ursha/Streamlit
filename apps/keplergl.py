
import streamlit as st
import leafmap.kepler as leafmap
#import modules 
from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt
from datetime import date
import pandas as pd
from shapely import wkt
import geopandas

api = SentinelAPI('omni4geo',  'F55skL7dm3MQc$6' , 'https://apihub.copernicus.eu/apihub')
    # search by polygon, time, and Hub query keywords
footprint = geojson_to_wkt(read_geojson('map.geojson'))
products = api.query(footprint,
                        date = '[NOW-1DAY TO NOW]', 
                        platformname = 'Sentinel-1')
   

print(products)



def app():

    st.title("keplergl")
    st.write(products)

    m = leafmap.Map(center=[54, -2], zoom=4)
    #gdf = gpd.read_file("/home/ursha/Documents/streamlit/apps/UK_Hex.geojson")
    in_geojson = "https://raw.githubusercontent.com/ursha/streamlit/master/map.geojson"
    m.add_geojson(in_geojson, layer_name="Uk HEX")
    
    



    m.to_streamlit(height=700)



#"https://raw.githubusercontent.com/ursha/streamlit/master/map.geojson"


#"https://raw.githubusercontent.com/ursha/streamlit/master/UK_HEX.geojson"