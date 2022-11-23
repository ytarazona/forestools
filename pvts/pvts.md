<!-- markdownlint-disable -->

<a href="..\forestools\pvts.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `pvts`





---

<a href="..\forestools\pvts.py#L7"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `pvts`

```python
pvts(x, startm, endm, threshold=5)
```

This algorithm will allow to detect disturbances in the forests using all the available Landsat set. In fact, it can also be run with sensors such as MODIS. 



**Parameters:**
 


 - <b>`x`</b>:  Can be numpy.ndarray with 1d or 2d without NaN's or pandas.core.series.Series. 


 - <b>`startm`</b>:  The start of the monitoring time. 


 - <b>`endm`</b>:  The end of the monitoring time. 


 - <b>`threshold`</b>:  The default thresholds are 5 or 6 for photosynthetic vegetation, for indices such   as NDVI and EVI the threshold is 3, and for fraction indices (NDFI) the thresholds is 5. Return: Detections as a dictionary. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
