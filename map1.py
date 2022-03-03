import folium

map = folium.Map(lacation=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")

for coordinates in [[38.58, -99.1],[37.58, -98.2]]:
    fg.add_child(folium.Marker(location=coordinates, popup="Hi I am a Marker", icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("map1.html")