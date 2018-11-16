---
Title: Getting started with Folium
Author: John Fay
Date: Fall 2018
---

# Getting Started With Folium

## ♦ Introduction

In previous years, I would spend several lectures on how to construct a web page with a Google Map embedded in it. It required learning a bit of HTML and JavaScript. The documentation from Google Was good, but it still required a bit of a learning investment just to get a map of a set of points to appear. 

Since then, coders have developed some nifty Python (and R) packages that alleviate the need to learn JavaScript and HTML. These packages essentially write the HTML and embedded JavaScript for you from our familiar Python platform. In this lesson we explore one of these packages - **Folium** - using it to quickly construct some handy web-based maps. 

The goals in this tutorial are many fold. We will, of course, learn how to generate web-enabled maps using the Folium module, but this will also be an opportunity to examine how and where 3rd party Python plugins get installed. We'll also examine how Folium works in terms of generating HTML, JavaScript code, and the Leaflet JavaScript API as this will enable us to get past limitations the Folium module has. 



## ♦ Installing the Folium module for Python

Before we move forward, we need to be sure Folium is installed on our machine. We installed Folium in our "my_env" environment in the GeoPandas, but in case it's not, here's the command to install it.

```dos
conda install -c conda-forge folium
```



## ♦ Creating web-based maps - Quick start examples

In the **DemoScripts** folder within this workspace are a set of Jupyter notebooks that create web maps. Navigate to the **1_CSVtoHTMLwithPython** folder and you'll see two scripts that do the same thing: create web map showing the points listed in the `Pennsylvania Oil and Gas Violations.csv` file. Our first exercise will quickly explore these two scripts. 




1. Open Jupyter Notebooks (a shortcut using the "my_env" environment is included in the repo).

2. Navigate to `DemoScripts/1_CSVtoHTMLwithPython` .

3. Open the `Pennsylvania Oil and Gas Violations.csv` in a text editor or Excel.

4. Open the `CreateHTMLFromCSV_GoogleAPI.ipynb` notebook and run it. An HTML file is created. 

5. Open the `Violations_Google.html` file in your browser: You see the violation points!

6. Open and run the `CreateHTMLFromCSV_Folium.ipynb` notebook and open the resulting HTML file. 



These two Python scripts use two separate web-mapping platforms. The first uses the [Google Maps API](https://developers.google.com/maps/) and the second uses the [Leaflet API](http://leafletjs.com/). Both of these are JavaScript based APIs which are "activated" by our Python scripts. 

Have a look at each script and see whether you can get a rough idea how each work. Briefly, the Google script simply writes raw HTML and JavaScript from Python. The Folium one does as well, but it does so more "programmatically" via the `Folium` package. 

Also, open the HTML files in a text editor and see what you can glean about how these work. 

We will discuss each in class, but the overall mechanism going on here is the underlying focus of todays lesson... 



## ♦  Getting Started With *Folium*: Diving In

*Ok, let's  focus on how **Folium** does its magic. We'll do so by exploring the Folium GitHub site and its documentation, and by tweaking some of the example notebooks it provides.* 

Folium, like most modules these days, is in a state of constant development and is therefore housed on **GitHub**: https://github.com/python-visualization/folium . Navigate to that site and you'll a link to some documentation: http://python-visualization.github.io/folium/docs-master/ . Scroll down to the **Quick Start** and you'll see an example notebook showing how easy it is to create a web map with Folium. 

I've downloaded all the Folium example notebooks into the `examples.zip` file included in this workspace. 

* <u>Unzip this folder and then fire up Jupyter notebooks.</u> We'll tinker with these examples, making changes and seeing how they manifest themselves in the resulting maps produced! (If you totally mess up a notebook, you can always pull the original out from the `example.zip` file...)
* <u>Start Jupyter Notebooks</u> (if needed), navigate to the Examples folder and <u>open the **QuickStart** notebook</u>. 

> As we run through this and other examples in class, we'll run through our typical learning procedures: *What objects d**oes the Folium package bring to Python; what can we do with these objects; how do we get them to do what we want...*



### Folium's *Map* object

http://python-visualization.github.io/folium/docs-master/quickstart.html

#### 1. Creating a <u>map object</u> <u>centered</u> on a specific location:

* Open the `Quickstart` notebook and run it.
* Try recoding the notebook so that it produces at map centered on the Nicholas School:  `36.0010, -78.9400`
* Modify the `save` function to your notebook to save the map as `myMap.html`. Then open the HTML document in your browser. 

#### 2. Changing the <u>base map</u> and <u>zoom</u> level:

* Try changing the basemap to `Stamen Terrain` with a zoom of `15`

* Try the `Cloudmade`  basemap...

  * *Seems you need to sign up for an API to use this base map...*

You can use Jupyter's functionality to reveal what other attributes of the map document can be changed (`map?`) and refer to the [documentation on the map class](http://python-visualization.github.io/folium/docs-master/modules.html) to better understand what these options are. 

#### 3. Changing the base map to use one of Leaflet's standard *tilesets*:

A bit further down in the QuickStart notebook, you'll see a mention of "`leaflet.js` compatible tilesets" and then some code:

```
folium.Map(location=[45.372, -121.6972],
           zoom_start=12,
           tiles='http://{s}.tiles.yourtiles.com/{z}/{x}/{y}.png',
           attr='My Data Attribution')
```

A gallery of these Leaflet tilesets is provided here: 
https://leaflet-extras.github.io/leaflet-providers/preview/, and we'll try updating our map to use one of these. 

* Copy and paste the above code into a new code cell. 
* Open the [providers link](https://leaflet-extras.github.io/leaflet-providers/preview/) above and preview `OpenStreetMap BlackAndWhite` option
* Copy the link shown in red next to `tileLayer` <font color='red' face='verdana'>https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png</font>
* In your notebook, set that as the `tile` value and set the `attr` value to "OSM Black & White"
  * *Note, the `attr` value is arbitrary, but will appear on your map to indicate the source of the tileset*

```python
folium.Map(location=[45.372, -121.6972],
           zoom_start=12,
           tiles='https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
           attr='OSM Black & White')
```

* Run view your map. 
* <mark>Try using some other tilesets.</mark>



### Folium's *Markers* object

At the bottom of the QuickStart notebook is a section on Markers. Run that code block

#### See if you can add your own simple **markers**

* Add a simple marker to your Duke campus map
  *  Set its location to (36.0055, -78.9420)
  *  Add a popup that says "Grainger Hall"
  *  Set its icon to be a green star


### *Etc., etc., etc...*

You're starting to get the idea of how to learn to construct maps using Folium. We look at examples, modify a few things and learn what properties do what. As the examples get more complex, however, you might feel hungry for more documentation or at least a better explanation of what some of the newer concepts are. What is "GeoJSON"? What is a tileset? 

This situation, I'm afraid to say, is typical when you are working on the "bleeding edge" of technology. Coders are providing these nifty tools they’ve developed for free; what documentation they provide is often a bonus. We must bridge the gap of what documentation is provided and what we need to know through a combination of creativity, a broader understanding of how things work, and trial and error experience. 
With that said, let's step back from what we accomplished from diving in to Folium and examine what, exactly, Folium is doing and how it's doing it. 

---

## ♦ What *is* Folium? (and Leaflet.js? and JavaScript?)

The Folium document explains what it does: 

> "Folium builds on the data wrangling strengths of the Python ecosystem and the mapping strengths of the **Leaflet.js library**. Manipulate your data in Python, then visualize it in on a Leaflet map via Folium."



### What is *Leaflet.js*?

We are familiar with "the Python ecosystem", but perhaps not so much what the "**Leaflet.js library**" is. Briefly, **Leaflet.js** is a **JavaScript** library, that is, a plug in for yet another programming language – JavaScript. 



### What is *JavaScript*? 

**JavaScript** is, among other things, a scripting language that web browsers are programmed to read and run. You may have heard of HTML, or Hyper Text Markup Language, and understood that to be the language of web browsers; and that's true, but HTML is only good at displaying static information. If you want dynamic content or any sort of interactivity on your web site, you also need a programming language, which is often JavaScript. 

So… JavaScript is a programming language that can be invoked in any standard web browser. JavaScript includes all the elements of any scripting language: variables (and data types), loops, and conditional statements. And also like other scripting languages, JavaScript can be extended by importing libraries, or bits of code that define functions and classes (and the properties and methods of these classes). 

►<font color='blue'>A good source for learning more about JavaScript and HTML is https://www.w3schools.com/ </font>



### Getting back to *Leaflet.js*

**Leaflet.js**, then, is one particular JavaScript library; it adds a number of mapping functions and classes which combine to enable us to add and manipulate maps in web pages. It's not the only JavaScript mapping library; others include **Google Maps** and **Microsoft Bing Maps**. However, Leaflet is rapidly becoming the de facto library because of its speed, small footprint, and [relative] ease of use. 

Leaflet (and most other JavaScript libraries) are accessed through their **API**, or Application Programming Interface: http://leafletjs.com/reference.html . The API reveals the programming *classes* and *functions* contained in the library. We'll dig deeper into these items in a later tutorial, but first, let's quickly preview of what a very simple Leaflet web document looks like:

1. **Open this link: http://leafletjs.com/examples/quick-start/example.html**

   This is taken from the Leaflet *quickstart* (http://leafletjs.com/examples/quick-start/).  You'll see that it contains all those things that we controlled via Folium – and more.

2. **Now view code behind this web page by hitting ctrl-U with the web page active.** 

   You'll see it's just text. This text includes some HTML and some JavaScript, all of which combines to produce the interactive web page that hosts the map. 

The text behind the web page likely seems a bit mysterious and confusing if you've never seen raw HTML before, but actually its highly structured and somewhat easy to pick out important bits if you know where to look. Briefly, the HTML document is split into a head and body. The head (lines 3-17) contains meta information about the document, including where modules get imported. You can see where Leaflet is imported in line 13. And the body contains instructions on how the page should be displayed: what programming elements should appear and where as well as the behaviors associated with them. In this quick start example, there's one html object explicitly added to the page: the `<div>` object created in line 22. (A `<div>` object defines a section in a web page.) However, just after this `<div>`object is added a snipped of JavaScript is run (lines 23-62). And in this JavaScript, a Leaflet map is created and set to appear within the`<div>` object (line 25). The JavaScript also adds a number of items to our map (lines 27 – 51), and sets a function that listens for the user to click on the map and show the coordinates where he/she clicked (lines 53-58).

Ok, that still may be a bit confusing, but it you just take away that (1) the HTML file is just a text file, and (2) that the text in the file is simply either HTML or JavaScript instruction on how to display and allow interaction with various objects in web browser, you can get a much better idea of what Folium does…

### Getting back to *Folium*…

Really all that Folium is doing is taking our instructions, written in Python, and translating those instructions to HTML and JavaScript and writing them to a text file with an HTML extension. (This is also how R's leaflet library works too, by the way…). In fact, you can open the html files you saved in the exercises above in a text editor and see some similarities, though the HTML documents Folium creates aren't as tidy as our quick start example. 

### *So why is it important to know all this?* 

Admittedly, the Folium module is nicely written and allows us to make web maps far more easily (leveraging our knowledge of Python) than having to learn the entire Leaflet or Google Maps API. But, if we limit our knowledge to just what Folium can do (and further by what the documentation explains), we are missing out on some powerful web mapping capabilities. Additionally, understanding the mechanism of how Folium works in terms of the HTML and JavaScript it creates both facilitates debugging and enables us to adapt quickly to future changes to the API. 

### Where to go from here? 

Here, we will continue to work through Folium examples and learn more about constructing maps using Python and Folium. Next up we will look more at the JavaScript APIs that enable us to publish, view, and interact with spatial data via the internet. 



## The bigger picture

We’ve glossed over a lot here and without too much depth. (Leaflet is capable of a lot more than we've toyed with!) However, if you pause and contemplate what's behind what we’ve done, you should see some interesting patterns. In particular, <u>the heavy use of text in all facets of web mapping</u>: in the Python/Folium code, in data formats that are used in creating geographic features (e.g. markers and JSON), and in the HTML/JavaScript page that is loaded into a browser to create your beautiful interactive map. 

Why is this worth mentioning? Two reasons. First, while binary data (stuff that appears as garbage if try to open it in Notepad++) is much more efficient for machines to manipulate, binary data is, well, cryptic; the format of binary files must match the processor type of specific machines (e.g. Apple vs PC). Text files, on the other hand are "platform agnostic". Not only can all machines read text, but we humans can "read" it too. That means, while GeoJSON objects are written with a specific design in mind, we can access specific bits of a GeoJSON quite easily and manipulate it for a different use without too much overhead. For example, imagine a Python script to extract all the coordinate pairs in a GeoJSON file versus a similar script that extracts coordinates from a binary shapefile…

The second reason why the prevalence of text is interesting is we can read and write text quite easily in Python. In fact, as we’ve mentioned, all the Folium module does is translate Python instructions (in text) into JavaScript instructions (in text). If you extend that further, you can see how converting a shapefile to GeoJSON format is fairly straightforward using ArcPy cursors (if you know the GeoJSON format). Or, constructing a set of Markers from a file of XY coordinates is also a matter of Python’s read statement and a loop to format the data from the input file to the GeoJSON output format. 

So, while there are a LOT of additional details to iron out to make maps appear exactly how you want, it’s within your grasp to do so. It's not some form of coding voodoo; it's understanding what objects and features are available to control and learning the commands how to control them. 