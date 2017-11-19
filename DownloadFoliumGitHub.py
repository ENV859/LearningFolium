#DownloadFoliumGitHub.py
#
# Downloads the folium github repository
#
# John.Fay@duke.edu for ENV 858

import sys, os, urllib, zipfile

#The url for the repo
theURL = 'https://github.com/python-visualization/folium/archive/master.zip'
localFilename = os.path.basename(theURL)

#Get it
response = urllib.urlretrieve(theURL,localFilename)
print "Downloading %s" %theURL

#Unzip it
zf = zipfile.ZipFile(localFilename)
zf.extractall()
zf.close()
