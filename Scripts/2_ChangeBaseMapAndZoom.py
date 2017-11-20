#Import the module
import folium

#Create a map object, centered at the coordinates we provide
m = folium.Map(location=[36.0010, -78.9400],
               tiles='Stamen Terrain',
               zoom_start=15)

#Save the map to a file
m.save('myMap.html')