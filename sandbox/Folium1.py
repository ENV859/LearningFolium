#FoliumDemo.py
#
# Requires installation of the folium package
# At the windows command line, navigate to
# C:\\python27\ArcGIS10.4\Scripts and run:
#   pip install folium
#
# Folium documentation is located at:
#  https://folium.readthedocs.io/en/latest/


import sys, os, folium
import webbrowser

#Some coordinates
myXY = (36.0010,-78.9400)

##Hello World! Basic map
map_osm = folium.Map(location=myXY)  #Creates the map object
map_osm.save("map.html")                #Saves it to a file
#webbrowser.open("map.html")             #Shows it

##Change the zoom
map_osm = folium.Map(location=myXY, zoom_start=15)
map_osm.save("map.html")

##Change the background to a folium default
#Other defaults: Stamen Terrain, Stamen Toner, Mapbox Bright, and Mapbox Control
map_osm = folium.Map(location=myXY, tiles='Stamen Toner')
map_osm.save("map.html")
#Built in: Stamen Terrain, Stamen Toner, Mapbox Bright, & Mapbox Control

##Custom tilesets
#What alternatives to 'Stamen Toner'?
# https://leaflet-extras.github.io/leaflet-providers/preview/
tileset = 'http://{s}.tiles.wmflabs.org/bw-mapnik/{z}/{x}/{y}.png'
map_osm = folium.Map(location=myXY, tiles=tileset, attr="Foo")
map_osm.save("map.html")

##---MARKERS---
folium.Marker(myXY, popup='Environment Hall').add_to(map_osm)
map_osm.save("map.html")
