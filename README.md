---
Title: Getting started with Folium
Author: John Fay
Date: Fall 2107
---

# Getting Started With Folium

## Introduction

In previous years, I would spend several lectures on how to construct a web page with a Google Map embedded in it. It required learning a bit of HTML and JavaScript. The documentation from Google Was good, but it still required a bit of a learning investment just to get a map of a set of points to appear. 

Since then, coders have developed some nifty Python (and R) packages that alleviate the need to learn JavaScript and HTML. These packages essentially write the HTML and embedded JavaScript for you from our familiar Python platform. In this lesson we explore one of these packages - **Folium** - using it to quickly construct some handy web-based maps. 

The goals in this tutorial are many fold. We will, of course, learn how to generate web-enabled maps using the Folium module, but this will also be an opportunity to examine how and where 3rd party Python plugins get installed. We'll also examine how Folium works in terms of generating HTML, JavaScript code, and the Leaflet JavaScript API as this will enable us to get past limitations the Folium module has. 

## ♦ Installing the Folium module for Python

Before we move forward, we need to be sure Folium is installed on our machine. Folium can be installed the usual way with `pip`:

```dos
C:\Python27\ArcGIS10.5\scripts\pip install folium
```



## ♦ Introduction to creating web-based maps

In the `DemoScripts` folder within this workspace are a set of Python scripts that create web maps. Navigate to the `1_CSVtoHTMLwithPython` folder and you'll see two scripts that do the same thing: create web map showing the point listed in the `Pennsylvania Oil and Gas Violations.csv` file. Our first exercise will quickly explore these two scripts. 


1. Navigate to the `DemoScripts/1_CSVtoHTMLwithPython` folder
2. Open the `Pennsylvania Oil and Gas Violations.csv`
3. Run the `1CreateHTMLFromCSV_GoogleAPI.py1` script. An HTML file is created. 
4. Open the `Violations_Google.html` file in your browser: You see the violation points!
5. Do the same for the `CreateHTMLFromCSV_Folium.py` script and open the resulting HTML file. 


These two Python scripts use two separate web-mapping platforms. The first uses the [Google Maps API](https://developers.google.com/maps/) and the second uses the [Leaflet API](http://leafletjs.com/). Both of these are JavaScript based APIs which are "activated" by our Python scripts. 

Have a look at each script and see whether you can get a rough idea how each work. Briefly, the Google script simply writes raw HTML and JavaScript from Python. The Folium one does as well, but it does so more "programmatically" via the `Folium` package. 

Also, open the HTML files in a text editor and see what you can glean about how these work. 

We will discuss each in class, but the overall mechanism going on here is the underlying focus of todays lesson... 



## ♦  Getting Started With Folium: Diving In

*Ok, let's  focus on generating some quick maps with Folium. We'll do so by exploring the Folium GitHub site and its documentation, and by tweaking some of the example notebooks it provides.* 

Folium, like most modules these days, is in a state of constant development and is therefore housed on GitHub: https://github.com/python-visualization/folium . Navigate to that site and you'll a link to some documentation: http://python-visualization.github.io/folium/docs-master/ . Scroll down to the **Quick Start** and you'll see an example notebook showing how easy it is to create a web map with Folium. 

I've downloaded all the Folium example notebooks into the `examples.zip` file included in this workspace. Unzip this folder and then fire up Jupyter notebooks. We'll tinker with these examples, making changes and seeing how they manifest themselves in the resulting maps produced! (If you totally mess up a notebook, you can always pull the original out from the `example.zip` file...)

**Alternatively**, I prefer to copy these snippets over to a Python script rather than working in a Jupyter notebook as notebooks with large embedded maps tend to get confusing. Either way, the journey to learning is roughly the same. 

<u>Below are the concepts you should become familiar with after running through these snippets:</u><br>As you run these, try to gain understanding of the various Folium objects (e.g. the `map` object) are created and manipulated. 

### Quickstart - Getting Started

http://python-visualization.github.io/folium/docs-master/quickstart.html

##### ◘ Creating a <u>map object</u> <u>centered</u> on a specific location:

* Open the `01_Quickstart` notebook and run it. (or copy the code to a new Python script...)
* Try recoding the notebook so that it produces at map centered on the Nicholas School: <br>
  (36.0010, -78.9400)
* Modify the `save` function to your notebook to save the map as `myMap.html`. Then open the HTML document in your browser. 

##### ◘ Changing the <u>base map</u> and <u>zoom</u> level:

* Try changing the basemap to `Stamen Terrain` with a zoom of `15`

* Try `Mapbox Control Room` with a zoom of 4

  * *Seems you need to sign up for an API to use this base map...*

  ```
  You can use Jupyter's functionality to reveal what other attributes of the map document can be changed and refer to the documentation to better understand what these options are. 
  ```

##### ◘ Changing the base map to use one of Leaflet's standard *tilesets* :

What is a *tileset*? 

What is *Leaflet*??

*Seems we dove in a bit too fast. Let's pause, step back, and get a broader understanding of what Folium is and how this stuff is working. Folium is essentially a Python "wrapper" for the Leaflet API, meaning Folium allows us to write Python scripts that construct web pages that use Leaflet to display maps. "Tilesets" are Leaflet constructs that allow 3rd (or 4th?) party coders to generate their own base maps.* 

A gallery of Leaflet tilesets is provided here: <br>
https://leaflet-extras.github.io/leaflet-providers/preview/

Looking at the QuickStart example, we get an idea of how a Leaflet tileset is used in a Folium script.

```javascript
myTileset=r'http://{s}.tiles.wmflabs.org/bw-mapnik/{z}/{x}/{y}.png'
myAttr='ENV 859'
                     
map_osm = folium.Map(location=[36.0010,-78.9400],
                     tiles=myTileset,
                     attr=myAttr,
                     zoom_start=14)
map_osm.save('osm.html')
```

Let's try change this:

(https://leaflet-extras.github.io/leaflet-providers/preview/). 

- Open the providers link above and preview `OpenStreetMap BlackAndWhite`
- Copy the link shown in red next to `tileLayer`
- Set that as the `tile` value and set an `attr` value

### Markers

http://localhost:8888/notebooks/notebooks/01_Quickstart.ipynb#Markers

#### Adding simple **markers**

* Add a simple marker to your Duke campus map
  *  Set its location to (36.0055, -78.9420)
  *  Add a popup that says Environment Hall
  *  Set its icon to be a green star

You're starting to get the idea of how to learn to construct maps using Folium. We look at examples, modify a few things and learn what properties do what. As the examples get more complex, however, you might feel hungry for more documentation or at least a better explanation of what some of the newer concepts are. What is "GeoJSON"? What is a tileset? 

This situation, I'm afraid to say, is typical when you are working on the "bleeding edge" of technology. Coders are providing these nifty tools they’ve developed for free; what documentation they provide is often a bonus. We must bridge the gap of what documentation is provided and what we need to know through a combination of creativity, a broader understanding of how things work, and trial and error experience. 
With that said, let's step back from what we accomplished from diving in to Folium and examine what, exactly, Folium is doing and how it's doing it. 

## 3. What *is* Folium? (and Leaflet.js? and JavaScript?)

The Folium document explains what it does: 

* "Folium builds on the data wrangling strengths of the Python ecosystem and the mapping strengths of the Leaflet.js library. Manipulate your data in Python, then visualize it in on a Leaflet map via Folium."

#### What is Leaflet.js?

We are familiar with "the Python ecosystem", but perhaps not so much what the "Leaflet.js library" is. Briefly, Leaflet.is is a JavaScript library, that is, a plug in for yet another programming language – JavaScript. 

#### What is JavaScript? 

JavaScript is, among other things, a scripting language that web browsers are programmed to read and run. You may have heard of HTML, or Hyper Text Markup Language, and understood that to be the language of web browsers; and that's true, but HTML is only good at displaying static information. If you want dynamic content or any sort of interactivity on your web site, you also need a programming language, which is often JavaScript. 

So… JavaScript is a programming language that can be invoked in any standard web browser. JavaScript includes all the elements of any scripting language: variables (and data types), loops, and conditional statements. And also like other scripting languages, JavaScript can be extended by importing libraries, or bits of code that define functions and classes (and the properties and methods of these classes). 

#### Getting back to Leaflet.js

Leaflet.js, then, is one particular JavaScript library; it adds a number of mapping functions and classes which combine to enable us to add and manipulate maps in web pages. It's not the only JavaScript mapping library; others include Google Maps and Microsoft Bing Maps. However, Leaflet is rapidly becoming the de facto library because of its speed, small footprint, and [relative] ease of use. 

Leaflet (and most other JavaScript libraries) are accessed through their API, or Application Programming Interface. http://leafletjs.com/reference.html. The API reveals the programming classes and functions contained in the library. We'll dig deeper into these items in a later tutorial, but first, let's quickly preview of what a very simple Leaflet web document looks like: