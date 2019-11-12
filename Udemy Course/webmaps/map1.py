import folium
map = folium.Map(location=[38.59, -99.09], zoom_start=6)

fg = folium.FeatureGroup(name="basemap")
fg.add_child(folium.Marker(
    location=[38.2, -99.1], popup="Marker", icon=folium.Icon(color='green')))

map.add_child(fg)
map.save("Map1.html")
