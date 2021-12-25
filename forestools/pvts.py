#!/usr/bin/env python
# coding: utf-8
# %%
import numpy as np
import pandas as pd

def pvts(x, startm, endm, threshold = 5):
    '''
    This algorithm will allow to detect disturbances in the forests using
    all the available Landsat set. In fact, it can also be run with sensors
    such as MODIS.
    
    Parameters:
    
        x: Can be numpy.ndarray with 1d or 2d without NaN's, pandas.core.series.Series or 
           pandas.core.indexes.datetimes.DatetimeIndex.
    
        startm: The start of the monitoring time.
        
        endm: The end of the monitoring time.
    
        threshold: The default thresholds are 5 or 6 for photosynthetic vegetation, for indices such 
              as NDVI and EVI the threshold is 3, and for fraction indices (NDFI) the thresholds is 5.
    Return:
        Detections as a dictionary.
    
    '''
    
    if isinstance (x, (np.ndarray)):
        
        if any(np.isnan(x)):
            raise Exception('The object cannot contain NaN: {}'.format(x))
        
        if x.ndim == 1:
            
            mean_pvts = np.mean(x[0:(startm-1)])
            std_pvts = np.std(x[0:(startm-1)])
            li = mean_pvts - threshold*std_pvts
            value = x[endm]
            
        else:
            raise Exception('2d ndarray not supported')
        
    elif isinstance (x, (pd.core.series.Series)):
        
        if any(x.isnull().values):
            raise Exception('The object cannot contain NaN: {}'.format(x))
        
        startm_n = x.index.get_loc(startm)
        endm_n = x.index.get_loc(endm)
        
        mean_pvts = np.mean(x[0:(startm_n -1)])
        std_pvts = np.std(x[0:(startm_n -1)])
        li = mean_pvts - threshold*std_pvts
        value = x[endm_n]
        
    elif isinstance (x, (pd.core.frame.DataFrame)):
        
        if any(x.isnull().values):
            raise Exception('The object cannot contain NaN: {}'.format(x))
        
        # whether the time series comes from google earth engine
        if isinstance (x.index, (pd.core.indexes.datetimes.DatetimeIndex)):
            #x = x.squeeze()
            x.index = x.index.date
            x.index = pd.to_datetime(x.index)
            x = pd.Series(x.iloc[:, 0], index = x.index)
        
        startm_n = x.index.get_loc(startm)
        endm_n = x.index.get_loc(endm)
        
        mean_pvts = np.mean(x[0:(startm_n -1)])
        std_pvts = np.std(x[0:(startm_n -1)])
        li = mean_pvts - threshold*std_pvts
        value = x[endm_n]
        
    else:
        raise NotImplemented('Type of "x" is not implemented.')
    
    if value < li:
        
        output = {'Ts': x,
                  'Monitoring_period': {'start': startm, 'end': endm},
                  'Breakpoint'       : {'Year_index': endm, 'value': value},
                  'Threshold'        : {'Threshold': threshold, 'Lower_limit': li}} 
        return output
    else:
        output = {'Ts': x,
                  'Monitoring_period': {'start': startm, 'end': endm},
                  'Breakpoint'       : {'Year_index': np.nan, 'value': np.nan},
                  'Threshold'        : {'Threshold': threshold, 'Lower_limit': li}} 
        return output

