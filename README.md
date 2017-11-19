---
Title: Getting started with Folium
Author: John Fay
Date: Fall 2107
---

# Getting Started With Folium

### Introduction

In previous years, I would spend several lectures on how to construct a web page with a Google Map embedded in it. It required learning a bit of HTML and JavaScript. The documentation from Google Was good, but it still required a lot of background to learn just to get a map of a set of points to appear. 
Much has changed in the last year. Now we have R libraries and Python modules that essentially write the HTML and JavaScript code for you from our more familiar coding platforms. Last week, Matt shows us a quick overview of how the Leaflet library in R can quickly – really quickly – generate a map showing our vector or raster data. 

Today, we return to Python and explore, a bit more slowly and deliberately, how similar maps can be made in that language. The Python module we will use is called Folium which works quite the same as the R Leaflet library. We'll explore how the Folium module (and how most 3rd party modules) are installed in Python, 

The goals in this tutorial are many fold. We will, of course, learn how to generate web-enabled maps using the Folium module, but this will also be an opportunity to examine how and where 3rd party Python plugins get installed. We'll also examine how Folium works in terms of generating HTML, JavaScript code, and the Leaflet JavaScript API as this will enable us to get past limitations the Folium module has. 

## 1. Installing the Folium module for Python

Folium can be installed with `pip`:

```DOS
pip install folium
```

## 2. Getting Started With Folium: Diving In

Now we'll focus on generating some quick maps with Folium.  
Folium, like most modules these days, is in a state of constant development and is therefore housed on GitHub: https://github.com/python-visualization/folium. Navigate to that site and you'll see some documentation; scroll down to the **Getting Started** section and let's get started! 

You'll see a number of code snippets to experiment with. We'll play around with these to get a feel for what Leaflet can do. Create a folder on your V: drive called **Folium** and then create a new empty Python script file. Open that up in PythonWin and then you can copy and paste these snippets from the Folium web page to your Python script and run them. 

Below are the concepts you should become familiar with after running through these snippets:

#### Creating a **map object** centered on a specific location

* Try centering the map on the Duke Campus: : (36.0010, -78.9400)

#### Changing the **base map** and **zoom** level:

* Try changing the basemap to "stamen terrain" with a zoom of 15
* Try "mapbox control room" with a zoom of 4

#### Changing the base map to use one of leaflet's standard tilesets:

(https://leaflet-extras.github.io/leaflet-providers/preview/). 

* Open the providers link above and preview `OpenStreetMap BlackAndWhite`
* Copy the link shown in red next to `tileLayer`
* Set that as the `tile` value and set an `attr` value

```javascript
myTileset=r'http://{s}.tiles.wmflabs.org/bw-mapnik/{z}/{x}/{y}.png'
myAttr='ENV 859'
                     
map_osm = folium.Map(location=[36.0010,-78.9400],
                     tiles=myTileset,
                     attr=myAttr,
                     zoom_start=14)
map_osm.save('osm.html')
```

#### Adding simple **markers**

* Add a simple marker to your Duke campus map
  *  Set its location to (36.0055, -78.9420)
  * Add a popup that says Environment Hall
  * Set its icon to be a green star

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