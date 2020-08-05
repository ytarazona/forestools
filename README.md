[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://paypal.me/APROGIS?locale.x=es_XC)

# forestools

**forestools** is a Python package that was created to provide tools for monitoring and mapping vegetation cover, especially detecting deforestation. The [**PVts-Beta**](https://www.sciencedirect.com/science/article/abs/pii/S1470160X18305326) approach, a non-seasonal detection approach (time-series-based), is implemented in this package. 

<img src="figures/img_readme.png">

# IEEE Geoscience and Remote Sensing Letters

This repository is part of the paper "Mapping deforestation using fractions indices and the PVts-beta approach" submitted to [IEEE Geoscience and Remote Sensing Letters](https://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=8859).

# Funding

The development of this package was funded by [American Program in GIS and Remote Sensing (APROGIS)](https://www.apgis-rs.com/). <img src="figures/logo_aprogis.png" align="right" width = 15%/> ARROGIS was established in 2018 as a leading scientific institution and pioneer in the field of Remote Sensing and Geographic Information Systems (GIS). APROGIS promotes the use of state-of-the-art space technology and earth observation for the sustainable development of states. It is an institution capable of generating new knowledge through publications in the highest impact journals in the field of Remote Sensing. More about APROGIS [here](https://www.apgis-rs.com/acerca-de-nosotros/mision-y-vision).

# Introduction

**forestools** is a Python package mainly focused on mapping and monitoring deforestation, although it can be used for monitoring forest degradation or detecting early warnings. The detection algorithm embedded in this package is a non-seasonal detection approach - unlike seasonal algorithms - that does not model the seasonal component of a time series, is intuitive, has only one calibration parameter, and can be run with vegetation indices such as NDVI and EVI, photosynthetic vegetation from CLASlite software, with radar polarizations, and with NDFI fraction indices. In fact, this package includes an algorithm that is capable of obtaining NDFI indices, which until now was only possible to obtain from Google Earth Engine.

**forestools** is intended for students, professionals, researchers, and organizations dedicated to forest monitoring and assessment, and any public interested in mapping the changes experienced by the different forests on the planet due to anthropogenic disturbances but also to minor natural disturbances.

# Installation

To used **forestools** it is necessary to install first. There are three options:

## 1. From PyPI

**forestools** is available on PyPI, so to install it, run this command in your terminal:

    pip install forestools

## 2. Installing from source

It is also possible to install the latest development version directly from the GitHub repository with:
    
    pip install git+git://github.com/ytarazona/forestools.git

## 3. Installing with Anaconda/conda

If you have Anaconda or Miniconda installed, you can then do:  

    conda install forestools 

Or you can create a conda Python environment to install **forestools**:
    
    conda create -n forest_env python=3.7
    conda activate forest_env
    conda install forestools

# Examples

## 1. Obtaining NDFI index

Landsat 8 OLI (Operational Land Imager) was used to obtain the NDFI index in this example. This image contain bands: ['B2', 'B3', 'B4','B5','B6','B7'].

```python
import forestools
import rasterio
import matplotlib.pyplot as plt

# Read raster bands
imgRas = rasterio.open('tests/data/LC08_232066_20190727.jp2')
    
# Raster to Numpay arrays
image = imgRes.read()
    
# Obtaining NDFI from Surface Reflectance
ndfi = forestools.ndfiSMA(x = image, procesLevel = 'SR')

# Displaying the index
plt.figure(figsize=(9,9))
plt.imshow(ndfi, cmap='RdYlGn')
plt.title('NDFI - Landsat 8 OLI')
```
The output:
<img src="https://raw.githubusercontent.com/ytarazona/forestools/master/figures/ndfi.png" align="right" width = 15%/>



    

