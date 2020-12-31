#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.ticker import MaxNLocator
import numpy as np
import pandas
from datetime import timedelta

def plot(x, title = None, xlabel = None, ylabel = None):
    
    cons = 1/2
    value = x['Breakpoint']['value']
    ts = x['Ts']
    title = title
    ylabel = ylabel
    xlabel = xlabel
    thr = x['Threshold']['Lower_limit']
    
    a = np.max(ts)/20
    leng = np.arange(0, len(ts), 1)
    
    p = x['Monitoring_period']['end']
    
    if isinstance (ts, (pandas.core.series.Series)):
        xlabel = 'Time'
        p = ts.index.get_loc(p)
        p = ts.index.values[p]
        leng = np.array(ts.index)
        freq = np.diff(ts.index.values).min()
        cons = freq/2

    coord = np.array([[p - cons, np.min(ts)-a], [p - cons, np.max(ts)+a], [p + cons, np.max(ts)+a], [p + cons, np.min(ts)-a]])
    poly = Polygon(coord, facecolor = 'lightsteelblue', edgecolor='none')
        
    fig, ax = plt.subplots()
    ax.plot(leng, ts, color = 'silver', marker = '.', ms = 14, linewidth= 1, markerfacecolor='black')
    ax.set_title(title)
    ax.set_ylim(np.min(ts)-a, np.max(ts)+a)
    
    if isinstance (ts, (pandas.core.series.Series)):
        ax.set_xlim(leng[0] - np.diff(ts.index.values).min(), leng[len(ts)-1] + np.diff(ts.index.values).min())

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.axhline(thr, color='red', linestyle='--')
        
    if ~np.isnan(value):
        ax.add_patch(poly)
        ax.axvline(p - cons, color='blue', linestyle='--')
        ax.axvline(p + cons, color='blue', linestyle='--')
        ax.axhline(thr, color='red', linestyle='--')
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        ax.legend(('Variable', 'Lower limit', 'Breakpoint detected'), loc='lower left', 
                 shadow=True, handlelength=1.5, fontsize=16)
    
    elif np.isnan(value):
        ax.axvline(p, color='blue', linestyle=':')
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        ax.legend(('Variable', 'Lower limit', 'Breakpoint not detected'), loc='lower left', 
                 shadow=True, handlelength=1.5, fontsize=16)
        
    return ax

