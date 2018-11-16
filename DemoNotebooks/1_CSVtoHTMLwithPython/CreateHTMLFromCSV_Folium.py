# CreateHTMLFromCSV.py

# Creates a Google Maps HTML document containing
# markers contained in the specified CSV file

# Fall 2018
# J.Fay for ENV859

import sys, os
import pandas as pd
import folium
from folium.plugins import MarkerCluster

#Set the working directory
os.chdir(os.path.dirname(sys.path[-1])+'\\1_CSVtoHTMLwithPython')

#Filename to save the output to:
outputHTML = 'Violations_folium.html'

#Read the data into a Pandas dataFrame
df = pd.read_csv('Pennsylvania Oil and Gas Violations.csv')

#Remove rows missing lat/long data
df.dropna(subset=['latitude','longitude'],axis='rows',how='any',inplace=True)

#Get the mean latitude and longitude, to set as the center of the map
meanLat = df['latitude'].mean()
meanLng = df['longitude'].mean()

#Create the folium map object
wellMap = folium.Map(location=(meanLat,meanLng),zoom_start=8)

#Create a marker cluster object which enables a cleaner display of markers
marker_cluster = MarkerCluster()
marker_cluster.add_to(wellMap)

#Add as Clustered Markers
for row in df.iterrows():
    #Print dots to show progress
    print ('.',end='')

    #Get the data from the row; it's the 2nd object (1st is the row's index)
    data = row[1] 
    
    #Get the row's data that we want
    lat = data['latitude']
    lon = data['longitude']
    name = data['Violation Code']
    
    #Create a marker
    m = folium.Marker((lat,lon),popup=str(name))
    
    #Add it to the marker cluster object
    m.add_to(marker_cluster)

# Save the map
wellMap.save(outputHTML)