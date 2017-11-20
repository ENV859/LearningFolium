#Import the module
import folium

#Create a map object, centered at the coordinates we provide
m = folium.Map(
    location=[45.372, -121.6972],
    zoom_start=12,
    tiles='Stamen Terrain'
)

tooltip = 'Click me!'

folium.Marker([45.3288, -121.6625], popup='<i>Mt. Hood Meadows</i>').add_to(m)
folium.Marker([45.3311, -121.7113], popup='<b>Timberline Lodge</b>').add_to(m)

#Save the map to a file
m.save('myMarkerMap.html')
