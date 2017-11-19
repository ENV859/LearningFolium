import folium

#Coordinates
xyDuke = [36.0010,-78.9400]
xyEnvHall = (36.0055,-78.9420)
OSMtileset=r'http://{s}.tiles.wmflabs.org/bw-mapnik/{z}/{x}/{y}.png'
ESRItileset =r'http://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}'
                    
map_osm = folium.Map(location=xyDuke,
                     tiles=ESRItileset,
                     attr="MyMap",
                     zoom_start=17)

folium.Marker([36.0055,-78.9420], popup='EnvHall',
                   icon = folium.Icon(icon = 'star',color='green')).add_to(map_osm)

cm = folium.CircleMarker(xyEnvHall,radius=20,
                         popup="Aura of green",
                         color="blue").add_to(map_osm)


p = folium.ClickForMarker(popup="Foo")
p.add_to(map_osm)

map_osm.save('osm.html')