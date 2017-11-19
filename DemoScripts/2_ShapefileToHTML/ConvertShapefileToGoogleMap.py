#ConverShapefileToGoogleMap.py

#Creates a Google Maps HTML document containing
#features from a supplied shapefile

import arcpy, sys, os

# User variables
inputFC = "Synoptic_Points_1991_2011_mrgis.shp"
nameFld = "LOC_ID"
outputHTML = "Features.html"

# Begin building the HTML file using boilerplate code
outFileObj = open(outputHTML,'w')
outFileObj.write('''
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="initial-scale=1.0, user-scalable=no" />
<meta http-equiv="content-type" content="text/html; charset=UTF-8"/>
<link href="http://code.google.com/apis/maps/documentation/javascript/examples/default.css" rel="stylesheet" type="text/css" />
<script type="text/javascript" 
  src="http://maps.googleapis.com/maps/api/js?sensor=false">
 </script>
<script type="text/javascript">
var map
//Function to create a marker at a given point with a given label
function createMarker(name, latlng, map) {
    var marker = new google.maps.Marker({position: latlng, map: map});
    google.maps.event.addListener(marker, "click", function() {
      infowindow = new google.maps.InfoWindow({content: name});
      infowindow.open(map, marker);
    });
    return marker;
    }
//Initialize function
function initialize() {
  var center = new google.maps.LatLng(28, -79.500);
  var myOptions = {
    zoom: 7,
    center: center,
    mapTypeId: google.maps.MapTypeId.ROADMAP
    }
  map = new google.maps.Map(document.getElementById("map_canvas"),myOptions);
''')

#Loop through [selected] features
googleSR = arcpy.SpatialReference("WGS 1984") #Using the WGS 84 in the search cursor gives coordinates in lat/long
rows = arcpy.SearchCursor(inputFC,'"YEAR" = 2006 AND "ADULTS" > 4',googleSR)
row = rows.next()
while row:
    shape = row.shape 
    Longitude=shape.firstPoint.X
    Latitude=shape.firstPoint.Y
    name = row.getValue(nameFld)
    outFileObj.write("  createMarker(\"%s\",new google.maps.LatLng(%s,%s),map)\n" %(name,Latitude,Longitude))
    row = rows.next()
del row, rows

# Add the remaining HTML code to the outFile
outFileObj.write('''
}
</script>
</head>
<body onload="initialize()">
  <div id="map_canvas" style="width:100%; height:80%"></div>
</body>
</html>''')

# Close the outFileObj
outFileObj.close()

# Additional code to open the file in the default browser
# Open the file in a web browser
import webbrowser
webbrowser.open_new(outputHTML)
