<!-- markdownlint-disable -->

<a href="..\forestools\ndfiSMA.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `ndfiSMA`





---

<a href="..\forestools\ndfiSMA.py#L6"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `ndfiSMA`

```python
ndfiSMA(x, procesLevel='SR')
```

The NDFI it is sensitive to the state of the canopy cover, and has been successfully applied  to monitor forest degradation and deforestation in Peru and Brazil. This index comes from the  endmembers Green Vegetation (GV), non-photosynthetic vegetation (NPV), Soil (S) and the reminder  is the shade component. 



**Parameters:**
 


 - <b>`x`</b>:  Can be numpy.ndarray with 2d without NaN's. Array dimensions should be rows, columns   and number of bands. The image must be in surface reflectance or TOA but scaled from 0 to 10000. 


 - <b>`procesLevel`</b>:  procesLevel Processing level. It is possible to obtain the NDFI from images in   surface reflectance (SR) from TM, ETM+ and OLI, or Top of Atmosphere (TOA)   values only for Landsat 8 OLI. The default is SR. In addition, for any processing  level, the image values must be rescaled between 0 and 10000. 

Return: numpy.ndarray with 2d. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
