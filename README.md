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
image = imgRas.read()
    
# Obtaining NDFI from Surface Reflectance
ndfi = forestools.ndfiSMA(x = image, procesLevel = 'SR')

# Displaying the index
plt.figure(figsize=(12,12))
plt.imshow(ndfi, cmap='RdYlGn')
plt.title('NDFI - Landsat 8 OLI')
```
The output:

<img src="https://github.com/ytarazona/forestools/blob/master/figures/ndfi.png?raw=true" width = 80%/>

## 2. Breakpoint in an NDFI series

Here an NDFI series between 2000 and 2019.

```python
import forestools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# NDFI series
serie = np.array([184, 193, 181, 185, 166, 189, 175, 180, 184, 189, 
                  195, 187, 191, 195, 189, 135, 172, 180, 51, 60])
              
# Index between 2000 - 2019
time = np.arange('2000', '2020', dtype='datetime64[Y]')

# Displaying the series
fig, axes = plt.subplots(figsize = (20,12))
axes.plot(time, serie, marker='.', ms = 7, linewidth =0.7, color = 'gray', 
          label='NDFI series')
axes.set_xlabel('Time')
axes.set_ylabel('NDFI Value')
axes.legend(loc="lower left", fontsize=20)
```
The output:

<img src="https://github.com/ytarazona/forestools/blob/master/figures/serieNDFI_1.png?raw=true" width = 80%/>

### 2.1 Applying a smoothing

Before detecting a breakpoint, it is necessary to apply a smoothing to remove outliers. So, we'll use the **smootH** function from the **forestools** package. This function accepts 1d array, so that if we are working with time series we will need to convert to array -> **ndfi_serie.to_numpy()**. 

```python
import forestools
import numpy as np

# Apply a smoothing
ndfi_smooth = smootH(x = serie)
time = np.arange('2000', '2020', dtype='datetime64[Y]')

# Displaying the series
# Series without smoothing
fig, axes = plt.subplots(figsize = (20,12))
axes.plot(time, serie, marker='.', ms = 7, linewidth =0.7, color = 'silver', 
          label='NDFI series')
# Series with smoothing
axes.plot(time, ndfi_smooth, marker='.', ms = 7, linewidth =1, color = 'blue', 
          label='NDFI series - smoothed')
axes.set_xlabel('Time')
axes.set_ylabel('NDFI Value')
axes.legend(loc="lower left", fontsize=20)
```
The output:

<img src="https://github.com/ytarazona/forestools/blob/master/figures/serieNDFI_2.png?raw=true" width = 80%/>

### 2.2 Detecting a change

Let's detect change in 2018. For this, we will used the **pvts** function. First, *numpy.ndarray* will be used to detect change, and then we will do the same using *pandas.core.series.Series*.

#### 2.2.1 Using *numpy.ndarray* 

Let's use the output of the smootH function (**ndfi_smooth**), but we'll need to convert to 1d array with *ravel()*.

Parameters:
- **x**: smoothed series preferably to optimize detections.
- **startm**: monitoring year, index 19 (i.e., year 2018)
- **endm**: year of final monitoring (i.e., also year 2018)
- **threshold**: detection threshold (for NDFI series we will use $6$). If you are using PV series, NDVI or EVI series you can use $5$, $3$ or $3$ respectively. Please see [Tarazona et al. (2018)](https://www.sciencedirect.com/science/article/abs/pii/S1470160X18305326) for more details.

> **Note**: You can change the detection threshold if you need to. 

```python
# Create an array
cd = pvts(x = ndfi_smooth.ravel(), startm = 19, endm = 19, threshold = 6)

# The output
cd
{'Monitoring_period': {'start': 19, 'end': 19},
 'Breakpoint': {'Year_index': 19, 'value': 120},
 'Threshold': {'Threshold': 6, 'Lower_limit': 157.4963411841562}}
```
#### 2.2.2 Using *pandas.core.series.Series* 

Let's use again the output of the smootH function (**ndfi_smooth**), but we'll need to convert to time series.

```python
# Serie between 2000 - 2019
index =pd.date_range('2000', '2020', freq='A')
ndfi_serie = pd.Series(ndfi_smooth.ravel(), index=index)

# Create an array
cd = pvts(x = ndfi_serie, startm='2018-12-31', endm='2018-12-31', threshold= 6)

# The output
cd
{'Monitoring_period': {'start': '2018-12-31', 'end': '2018-12-31'},
 'Breakpoint': {'Year_index': '2018-12-31', 'value': 120},
 'Threshold': {'Threshold': 6, 'Lower_limit': 157.4963411841562}}
```

