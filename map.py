import folium
import pandas

data=pandas.read_csv("Volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return "#4AA02C"
    elif 1000 <= elevation < 3000:
        return "#FBB917"
    else:
        return "#FF0000"
map=folium.Map(location=[28.439769, 77.053106], width='100%', height='100%', left='0%', top='0%', position='relative', 
tiles='OpenStreetMap', attr=None, min_zoom=0, max_zoom=18, zoom_start=10, min_lat=-90, max_lat=90, min_lon=-180, 
max_lon=180, max_bounds=False, crs='EPSG3857', 
control_scale=False, prefer_canvas=False, no_touch=False, disable_3d=False, png_enabled=False, zoom_control=True)

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el in zip(lat,lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln],radius=6, popup=str(el) +" m", 
    fill_color=color_producer(el), color='grey',fill_opacity=0.5, tooltip='Tip' ))

fgp = folium.FeatureGroup(name="Populations")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'#0000ff' if x['properties']['POP2005'] < 10000000
else '#808000' if 10000000 <= x['properties']['POP2005'] < 20000000 else '#00FF00'}))


map.add_child(fgp)
map.add_child(fgv)
map.add_child(folium.LayerControl(position='bottomright', collapsed=True, autoZIndex=True))

map.save("SampleMap.html")

