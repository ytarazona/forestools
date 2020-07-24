#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy
import pandas

def smootH(x, method_interp = 'linear', limit = 20):
    '''
    Description of the smootH function
    
    Parameters:
    
        x: Can be numpy.ndarray with 1d or 2d.
    
        method_interp: Interpolation method. It can be "time" or "linear".
        
        limit: Number of data to be interpolated. Must be greater than 0.
    
    Return:
        Smoothed input.
    
    '''
    if isinstance (x, (numpy.ndarray)):
        
        if x.ndim == 1:
            x = pandas.DataFrame({'Value': x})
            
            if any(numpy.isnan(x)):
                
                if method_interp == 'linear':
                    x = x.interpolate(method = method_interp, limit = limit)
                    x = x.to_numpy()
                elif method_interp == 'time':
                    x = x.interpolate(method = method_interp, limit = limit)
                    x = x.to_numpy()
                else:
                    raise NotImplemented('Interpolation not supported.')
                
            for i in numpy.arange(1, (len(x)-1),1):
                x[i] = numpy.where(((x[i]-x[i-1] < -0.01*x[i-1]) & (x[i]-x[i+1] < -0.01*x[i+1])), 
                                (x[i-1]+x[i+1])/2, x[i])
        
        elif x.ndim == 2:
            for i in numpy.arange(0, x.shape[0], 1):
                for j in numpy.arange(1, (x.shape[1]-1),1):
                    x[i,:][j] = numpy.where(((x[i,:][j] - x[i,:][j-1] < -0.01*x[i,:][j-1]) & (x[i,:][j]-x[i,:][j+1] < -0.01*x[i,:][j+1])), 
                                         (x[i,:][j-1]+x[i,:][j+1])/2, x[i,:][j])
        
        else:
            raise ValueError('Non-implemented array size')
            
    else:
        raise NotImplemented('Type of "x" is not implemented.')
    
    return x

