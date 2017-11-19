import folium

map_3 = folium.Map(
    location=[46.1991, -122.1889],
    tiles='Stamen Terrain',
    zoom_start=13)
map_3.add_child(folium.LatLngPopup())
map_3.save("map3.html")