import streamlit as st
import leafmap.kepler as leafmap
import datetime
#import modules 
from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt
from datetime import date
import pandas as pd
from shapely import wkt
import geopandas

# api = SentinelAPI('omni4geo',  'F55skL7dm3MQc$6' , 'https://apihub.copernicus.eu/apihub')
#     # search by polygon, time, and Hub query keywords
# footprint = geojson_to_wkt(read_geojson('map.geojson'))
# products = api.query(footprint,
#                         date = '[NOW-1DAY TO NOW]', 
#                         platformname = 'Sentinel-1')
   


# products_df = api.to_dataframe(products)
# #rename fotprint column to geometry 
# df2 = products_df.rename({'footprint': 'geometry'}, axis=1)
# # apply wkt
# df2['geometry'] = df2['geometry'].apply(wkt.loads)
# #add to geopandas
# gdf = geopandas.GeoDataFrame(df2, geometry='geometry', crs = "EPSG:4326")
# dropped=gdf.drop(columns=['beginposition', 'endposition','ingestiondate'])






def app():
    api = SentinelAPI('omni4geo',  'F55skL7dm3MQc$6' , 'https://apihub.copernicus.eu/apihub')
    # search by polygon, time, and Hub query keywords
    footprint = geojson_to_wkt(read_geojson('map.geojson'))
    products = api.query(date = '[NOW-1DAY TO NOW]' ,platformname = 'Sentinel-1', producttype= 'GRD')
    
    products_df = api.to_dataframe(products)

    #rename fotprint column to geometry 
    df2 = products_df.rename({'footprint': 'geometry'}, axis=1)
    df2['ingestiondate']=df2['ingestiondate'].dt.strftime('%H%M')
    # apply wkt
    df2['geometry'] = df2['geometry'].apply(wkt.loads)
    #add to geopandas
    gdf = geopandas.GeoDataFrame(df2, geometry='geometry', crs = "EPSG:4326")
    dropped=gdf.drop(columns=['beginposition', 'endposition','link_icon','title','identifier', 'format',
                              'link_alternative', 'ondemand', 'link', 'instrumentname', 'gmlfootprint','gmlfootprint', 'filename'])


    st.title("Sentinel 1")
    
    m = leafmap.Map(center=[54, -2], zoom=1)
    m.add_gdf(dropped, layer_name="Data")
    m.to_streamlit(height=800)
    
    
    
  
    
    
    
    
  



    





    
    
    
    
    # omni4geo
    
    # F55skL7dm3MQc$6