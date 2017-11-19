import sys, os, folium

#Some coordinates
dukeXY = (36.0010,-78.9400)
ehXY = (36.0055, -78.9420)
mlXY = (34.7166, -76.6723)

#Step 1
map_osm = folium.Map(location=dukeXY)  
map_osm.save("Step1.html")                

##Change the zoom
map_osm = folium.Map(location=dukeXY, zoom_start=15)
map_osm.save("Step1.html")

##Change the background to a folium default
#Other defaults: Stamen Terrain, Stamen Toner, Mapbox Bright, and Mapbox Control
map_osm = folium.Map(location=dukeXY, tiles='stamen terrain')
map_osm.save("Step2.html")
#Built in: Stamen Terrain, Stamen Toner, Mapbox Bright, & Mapbox Control

##Custom tilesets
#What alternatives to 'Stamen Toner'?
# https://leaflet-extras.github.io/leaflet-providers/preview/
tileset = 'http://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png'
attribution = "CartoDB Positron"
map_osm = folium.Map(location=dukeXY,
                     zoom_start=15,
                     tiles=tileset,
                     attr=attribution)
map_osm.save("Step3.html")

#Add marker
folium.Marker(mlXY, popup='Home of Advanced GIS').add_to(map_osm)
map_osm.save("Step4.html")

#GeoJSON
geo_path = r'data/antarctic_ice_edge.json'
topo_path = r'data/antarctic_ice_shelf_topo.json'
duml_map = folium.Map(location=mlXY,
                   tiles='Mapbox Bright', zoom_start=2)
duml_map.choropleth(geo_path=geo_path)
duml_map.choropleth(geo_path=topo_path, topojson='objects.antarctic_ice_shelf')
duml_map.save('Step5.html')
