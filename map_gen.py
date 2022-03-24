import folium
import pandas as pd

data = pd.read_csv("data.csv")
lat = data['LAT']
lon = data['LON']
info = data['INFO']
color = data['COL']

map = folium.Map(location=[55.2802307,86.1141404], zoom_start = 15)

for lat, lon, info,color in zip(lat, lon, info,color):
    folium.Marker(location=[lat, lon], popup=str(info), icon=folium.Icon(color = str(color))).add_to(map)

map.save("map1.html")