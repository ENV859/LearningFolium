#Import the module
import folium

#Specify the tileset
myTileset=r'http://{s}.tiles.wmflabs.org/bw-mapnik/{z}/{x}/{y}.png'
myAttr='ENV 859'

#Create a map object, centered at the coordinates we provide
m = folium.Map(location=[36.0010, -78.9400],
               zoom_start=12,
               tiles=myTileset,
               attr=myAttr)

#Save the map to a file
m.save('myMap.html')
