import folium
from folium.plugins import MarkerCluster
import pandas as pd

west = pd.read_csv('311datawesterleigh500.csv', encoding = 'latin-1')

map10314 = folium.Map(location=[40.6,-74.2], tiles='Stamen Toner')

for index, row in west.iterrows():
    complaint = row["Complaint Type"]
    lat=row['Latitude']
    lon=row['Longitude']
    map10314.simple_marker([lat,lon], popup=complaint)
    

map10314.create_map(path='mapwesterleigh4.html')
