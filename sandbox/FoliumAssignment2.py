import folium
import pandas as pd

state_geo = r'data/us-states.json'
state_unemployment = r'data/US_Unemployment_Oct2012.csv'

state_data = pd.read_csv(state_unemployment)

#Let Folium determine the scale
map = folium.Map(location=[48, -102], zoom_start=3)
map.choropleth(geo_path=r'data/NC_Counties.json')
map.choropleth(geo_path=state_geo, data=state_data,
             columns=['State', 'Unemployment'],
             key_on='feature.id',
             fill_color='YlGn', fill_opacity=0.7, line_opacity=0.2,
             legend_name='Unemployment Rate (%)')
map.save('us_states.html')

co_geo = r'data/us_counties_20m_topo.json'
co_data = r'data/us_county_data.csv'

co_df = pd.read_csv(co_data)

map = folium.Map(location=[48, -102], zoom_start=3)
map.choropleth(geo_path=co_geo, data=co_df,
             columns=['State', 'Unemployment'],
             key_on='feature.id',
             fill_color='YlGn', fill_opacity=0.7, line_opacity=0.2,
             legend_name='Unemployment Rate (%)')
map.save('us_states.html')

print state_data.shape
print state_data.columns
print state_data.head(4)
print state_data['Unemployment'].mean()
print state_data[(state_data.State == 'NC')]
print state_data[(state_data.Unemployment > 10)]

