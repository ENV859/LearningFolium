# CreateHTMLFromCSV_GoogleAPI.py

# Creates a Google Maps HTML document containing
# markers contained in the specified CSV file

# Fall 2017
# J.Fay for ENV859

import sys, os

# Script variables
inputCSV = "Pennsylvania Oil and Gas Violations.csv"
latFld = "latitude"
lonFld = "longitude"
nameFld = "Viol Id"
outputHTML = "Violations_Google.html"

# Read header row
inFileObj = open(inputCSV,'r')
headerLine = inFileObj.readline()
fieldNames = headerLine.split(",")

# Get field indices based on where the field names occur in the list of header items
latIdx = fieldNames.index(latFld)
lonIdx = fieldNames.index(lonFld)
nameIdx = fieldNames.index(nameFld)

# Begin building the HTML file using boilerplate code
outFileObj = open(outputHTML,'w')
outFileObj.write('''
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="initial-scale=1.0, user-scalable=no" />
<meta http-equiv="content-type" content="text/html; charset=UTF-8"/>
<link href="http://code.google.com/apis/maps/documentation/javascript/examples/default.css" rel="stylesheet" type="text/css" />
<title>Pennsylvania Oil and Gas Violations</title>
<script type="text/javascript" 
  src="http://maps.googleapis.com/maps/api/js?sensor=false">
 </script>
<script type="text/javascript">
var map
//Initialize function
function initialize() {
  var center = new google.maps.LatLng(41.79, -76.58);
  var myOptions = {
    zoom: 10,
    center: center,
    mapTypeId: google.maps.MapTypeId.ROADMAP
    }
  map = new google.maps.Map(document.getElementById("map_canvas"),myOptions);
''')

#Loop through records in the input CSV and write markers for each
lineString = inFileObj.readline()
while lineString:
    # Parse the lineString into alist
    lineData = lineString.split(",")
    try: # Will skip line if lat or lon aren't numbers
    # Get Values at the indices discovered above
        lat = float(lineData[latIdx])
        lon = float(lineData[lonIdx])
        name = lineData[nameIdx]
        outFileObj.write("  var marker = new google.maps.Marker({\n")
        outFileObj.write("    position: new google.maps.LatLng("+str(lat)+", "+str(lon)+"),\n")
        outFileObj.write("    title: \""+name+"\",\n")
        outFileObj.write("    map: map\n")
        outFileObj.write("  });\n")
    except:
        pass#print lineString
    lineString = inFileObj.readline()

# Close the inFileObj
inFileObj.close()

# Add the remaining HTML code to the outFile
outFileObj.write('''
  }
</script>
</head>
<body onload="initialize()">
  <div id="map_canvas" style="width:100%; height:100%"></div>
</body>
</html>''')

# Close the outFileObj
outFileObj.close()

                     
