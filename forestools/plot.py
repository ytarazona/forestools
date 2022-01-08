#!/usr/bin/env python
# coding: utf-8
# %%
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np
import pandas as pd

def plot(x, title = None, xlabel = None, ylabel = None, ax = None, **kwargs):
    
    '''
    This function is to show a non-seasonal detection aproach.
    
    Parameters:
    -----------
    
        x: Can be numpy.ndarray or pandas.core.series.Series.
    
        title: Assigned title.
        
        xlabel: X axis title.
        
        ylabel: Y axis title.
        
        ax: current axes
        
        **kwargs: These will be passed to the matplotlib plot, please see full lists at:
                https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
        
    Returns
    -------
        ax : Graphic of change detection using the matplotlib plot function.
    '''
    
    # Extracting data and lower limit detected
    ts = x['Ts']
    a = np.max(ts)/20
    thr = x['Threshold']['Lower_limit']
    
    # Only array and pandas series can be used
    if isinstance (ts, (np.ndarray)):
        value = x['Breakpoint']['value']
        leng = np.arange(0, len(ts), 1)
        p = x['Monitoring_period']['end']
        cons = 1/3
        
    elif isinstance(ts, (pd.core.series.Series)):
        value = x['Breakpoint']['value']
        pos = x['Monitoring_period']['end']
        post = ts.index.get_loc(pos)
        p = ts.index.values[post]
        leng = np.array(ts.index)
        freq = np.diff(ts.index.values).min()
        cons = freq/3
        
    else:
        raise Exception('object not supported')
        
    # title
    if title is None:
        if ~np.isnan(value):
            title = "Breakpoint Detected: Non-seasonal detection approach"
        elif np.isnan(value):
            title = "Breakpoint Not Detected: Non-seasonal detection approach"
    
    title = title
    
    # ylabel
    if ylabel is None:
        ylabel = "Variable"
    ylabel = ylabel
    
    # xlabel
    if xlabel is None:
        xlabel = "Index"
        if isinstance(x['Ts'], (pd.core.series.Series)):
            xlabel = 'Time'
    xlabel = xlabel
    
    if ax is None:
        ax = plt.gca()
    
    ax.plot(leng, ts, color = 'silver', marker = '.', ms = 14, linewidth= 1, 
            markerfacecolor = 'black', **kwargs)
    ax.set_title(title)
    #ax.set_ylim(np.min(ts)-a, np.max(ts)+a)
    
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.axhline(thr, color = 'red', alpha=0.7, linestyle = '--')
    
    # Drawing a poly if a breakpoint is detected
    if ~np.isnan(value):
        ax.axvspan(p-cons, p+cons, facecolor = 'lightsteelblue', edgecolor = 'none', alpha = 0.6)
        ax.axvline(p - cons, color = 'blue', linestyle = '--', alpha = 0.5)
        ax.axvline(p + cons, color = 'blue', linestyle = '--', alpha = 0.5)
        ax.xaxis.set_major_locator(MaxNLocator(integer = True))
        ax.legend(('Variable', 'Lower limit', 'Breakpoint detected'), loc = 'lower left', 
                 shadow = True, handlelength = 1.5, fontsize = 16)
    
    # Drawing a line if a breakpoint is not detected
    elif np.isnan(value):
        ax.axvline(p, color = 'blue', linestyle = ':')
        ax.xaxis.set_major_locator(MaxNLocator(integer = True))
        ax.legend(('Variable', 'Lower limit', 'Breakpoint Not detected'), loc = 'lower left', 
                 shadow = True, handlelength = 1.5, fontsize = 16)
            
    return ax
