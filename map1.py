import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])


def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 30000:
        return "orange"
    else:
        return "red"

map = folium.Map(lacation=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")
 
for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lt, ln], popup=str(el)+" m", icon=folium.Icon(color=color_producer(el))))

map.add_child(fg)

map.save("map1.html")