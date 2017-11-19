import folium

world_path = r'data/world-countries.json'
africa_path = 'data/africa.json'
geo_path = r'data/antarctic_ice_edge.json'
topo_path = r'data/antarctic_ice_shelf_topo.json'

ice_map = folium.Map(location=[0,0],
                   tiles='Mapbox Bright', zoom_start=2)
ice_map.choropleth(geo_path=africa_path)
ice_map.save('ice_map.html')

