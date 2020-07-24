#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy
import pandas

def pvts(x, startm, endm, threshold = 5):
    '''
    This algorithm will allow to detect disturbances in the forests using
    all the available Landsat set. In fact, it can also be run with sensors
    such as MODIS.
    
    Parameters:
    
        x: Can be numpy.ndarray with 1d or 2d without NaN's or pandas.core.series.Series.
    
        startm: The start of the monitoring time.
        
        endm: The end of the monitoring time.
    
        threshold: The default thresholds are 5 or 6 for photosynthetic vegetation, for indices such 
              as NDVI and EVI the threshold is 3, and for fraction indices (NDFI) the thresholds are 
              between 5 and 11.
    Return:
        Detections as a dictionary.
    
    '''
    
    if any(numpy.isnan(x)):
        raise Exception('The object cannot contain NaN: {}'.format(x))
        
    if isinstance (x, (numpy.ndarray)):
        
        if x.ndim == 1:
            
            mean_pvts = numpy.mean(x[0:(startm-1)])
            std_pvts = numpy.std(x[0:(startm-1)])
            li = mean_pvts - threshold*std_pvts
            value = x[endm-1]
            
        else:
            raise Exception('2d ndarray not supported')
        
    elif isinstance (x, (pandas.core.series.Series)):
        
        startm_n = x.index.get_loc(startm)+1
        endm_n = x.index.get_loc(endm)+1
        
        mean_pvts = numpy.mean(x[0:(startm_n-1)])
        std_pvts = numpy.std(x[0:(startm_n-1)])
        li = mean_pvts - threshold*std_pvts
        value = x[endm_n-1]
        
    else:
        raise NotImplemented('Type of "x" is not implemented.')
    
    if value < li:
        
        output = {'Monitoring_period': {'start': startm, 'end': endm},
                  'Breakpoint'       : {'Year_index': endm, 'value': value},
                  'Threshold'        : {'Threshold': threshold, 'Lower_limit': li}} 
        return output
    else:
        output = {'Monitoring_period': {'start': startm, 'end': endm},
                  'Breakpoint'       : {'Year_index': np.nan, 'value': np.nan},
                  'Threshold'        : {'Threshold': threshold, 'Lower_limit': li}} 
        return output

