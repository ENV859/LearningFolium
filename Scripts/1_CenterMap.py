#Import the module
import folium

#Create a map object, centered at the coordinates we provide
m = folium.Map(location=[45.5236, -122.6750])

#Save the map to a file
m.save('myMap.html')