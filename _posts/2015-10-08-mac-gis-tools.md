---
layout: post
title: "Mac GIS tools"
description: ""
category: GIS
tags: [mac,gis,tools,configuration]
---
{% include JB/setup %}

# Mac GIS Tools

This is documentation on how to configure your Mac system for GIS tools.

## Install brew.sh - the missing package manager for OS X

<a href="http://brew.sh" target="_blank">http://brew.sh</a>

Homebrew installs the stuff you need that Apple didn't.

Follow the instructions. Requires termial: 

``COMMAND + spacebar > search 'terminal'``

Paste command:

``ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"``

Confirm install:

``$ brew --help``

## Easy installations:

QGIS requires: Python2.7, GDAL, PROJ.4, NumPy, SciPy, Matplotlib

Install the libraries/software in the order below.

- To allow unrecognized developers/apps to be installed: CONTROL + CLICK on .pkg to open

GDAL:

- <a href="http://www.kyngchaos.com/files/software/frameworks/GDAL_Complete-1.11.dmg" target="_blank">GDAL 1.11 Complete</a>

PROJ:

- <a href="http://www.kyngchaos.com/files/software/frameworks/PROJ_Framework-4.9.2-1.dmg" target="_blank">PROJ.4</a>

NumPy:

Included on the GDAL Framework disk image.

- <a href="http://www.kyngchaos.com/files/software/python/NumPy-1.9.2-1.dmg" target="_blank">NumPy 1.9.2-1</a>
- <a href="http://www.kyngchaos.com/files/software/python/NumPy-1.8.0-1.dmg" target="_blank">NumPy 1.8.0-1 (32+64bit, Snow Leopard+)</a>

**Matplotlib:**

Requires: NumPy

- <a href="http://www.kyngchaos.com/files/software/python/matplotlib-1.4.3-1.dmg">matplotlib 1.4.3-1</a>

**QGIS:**

- <a href="http://www.kyngchaos.com/files/software/qgis/QGIS-2.10.1-1.dmg">QGIS 2.10.1-1</a>


#### Optional Python modules:

**SciPy:**

Requires: NumPy

- <a href="http://www.kyngchaos.com/files/software/python/SciPy-0.16.0-1.dmg" target="_blank">SciPy 0.16.0-1</a>
- <a href="http://www.kyngchaos.com/files/software/python/SciPy-0.13.1-1.dmg" target="_blank">SciPy 0.13.1-1 (32+64bit, Snow Leopard+)</a>

**Python Imaging Library (PIL):**

Requires: UnixImageIO, FreeType

- <a href="http://www.kyngchaos.com/files/software/python/PIL-1.1.7-4.dmg" target="_blank">PIL 1.1.7-4 (32+64bit, Snow Leopard+)</a>

**psycopg2:**

PostgreSQL interface

- <a href="http://www.kyngchaos.com/files/software/python/Psycopg2-2.4.5-2.dmg">Psycopg2 2.4.5-2</a>

**RPy2:**

Requires: R 3.1

- <a href="http://www.kyngchaos.com/files/software/python/RPy2-2.5.4-1.dmg">RPy2 2.5.4-1 for R 3.1</a>

**Pythoni Spatial Analysis Library (PySAL):**

Requires: NumPy, SciPy

``$ sudo easy_install pysal``

## GDAL for terminal

This installation will allow command line access to GDAL for scripting geoprocessing and PostgreSQL support. BuildingOnMac documentation is located <a href="https://trac.osgeo.org/gdal/wiki/BuildingOnMac" target="_blank">here</a>.

Open terminal:

``COMMAND + SPACEBAR > search 'terminal'``

Install GDAL:

This one will take some time.

``$ brew install gdal --with-unsupported --with-libkml --with-postgresql-9.4``

Confirm install: 

``$ gdalinfo``

