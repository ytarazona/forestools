#!/usr/bin/env python
# coding: utf-8

# In[30]:


import numpy

def ndfiSMA(x, procesLevel = 'SR'):
    '''
    The NDFI it is sensitive to the state of the canopy cover, and has been successfully applied 
    to monitor forest degradation and deforestation in Peru and Brazil. This index comes from the 
    endmembers Green Vegetation (GV), non-photosynthetic vegetation (NPV), Soil (S) and the reminder 
    is the shade component.
    
    Parameters:
    
        x: Can be numpy.ndarray with 2d without NaN's. Array dimensions should be rows, columns 
           and number of bands. The image must be in surface reflectance or TOA but scaled from 0 to 10000.
        
        procesLevel: procesLevel Processing level. It is possible to obtain the NDFI from images in 
                     surface reflectance (SR) from TM, ETM+ and OLI, or Top of Atmosphere (TOA) 
                     values only for Landsat 8 OLI. The default is SR. In addition, for any processing
                     level, the image values must be rescaled between 0 and 10000.
    
    Return:
        numpy.ndarray with 2d.
    '''
    if isinstance (x, (numpy.ndarray)):
        
        M_img = numpy.zeros((x.shape[1], x.shape[2], x.shape[0]))
        
        for i in range(0, x.shape[0], 1):
            M_img[:,:,i] = x[i,:,:]
        
        row = M_img.shape[0]
        col = M_img.shape[1]
        bands = M_img.shape[2]
        x = M_img.reshape((row*col, bands))
    else:
        raise NotImplemented('"x" must be numpy.ndarray with rows, cols and bands.')
    
    if procesLevel == 'SR':
        
        M =[[119.0,  475.0,  169.0,  6250.0, 2399.0, 675.0], # gv
            [1514.0, 1597.0, 1421.0, 3053.0, 7707.0, 1975.0], # npv
            [1799.0, 2479.0, 3158.0, 5437.0, 7707.0, 6646.0], # soil
            [4031.0, 8714.0, 7900.0, 8989.0, 7002.0, 6607.0], # cloud
           ]
        M = numpy.array(M)
        
    elif  procesLevel == 'TOA':
        
        M =[[119.0,  475.0,  169.0,  6250.0, 2399.0, 675.0], # gv
            [1514.0, 1597.0, 1421.0, 3053.0, 7707.0, 1975.0], # npv
            [1799.0, 2479.0, 3158.0, 5437.0, 7707.0, 6646.0], # soil
            [4031.0, 8714.0, 7900.0, 8989.0, 7002.0, 6607.0], # cloud
           ]
        M = numpy.array(M)
        
    else:
        raise NotImplemented('Processing level not supported.')
        
    if x.shape[1] > M.shape[0]:
        if x.shape[1] == M.shape[1]:
            M = numpy.transpose(M)
            mat_oper = numpy.dot(numpy.linalg.inv(numpy.dot(numpy.transpose(M), M)),
                                     numpy.transpose(M)) 
            frac = numpy.zeros((row*col, 4))
                
            for i in numpy.arange(0, 3, 1):
                for j in numpy.arange(0, row*col, 1):
                    f = numpy.dot(mat_oper, x[j,:])
                    frac[j,i] = f[i,]
            sma_img = numpy.zeros((row, col, 4)) # filas, columnas y n bandas
            
            # Realizamos el stack
            for i in range(0, 4, 1):
                sma_img[:,:,i] = frac[:,i].reshape(row, col)
            
        else:
            raise NotImplemented('The number of values extracted in band should be equal.')
    
    else:
        raise NotImplemented('The number of bands must be greater than the number of endmembers.')
    
    gv = sma_img[:,:,0]*100; gv[gv<0] = 0 # Green Vegetation
    npv = sma_img[:,:,1]*100; npv[npv<0] = 0 # Non Photosynthetic Vegetation
    soil = sma_img[:,:,2]*100; soil[soil<0] = 0 # Soil
    cloud = sma_img[:,:,3]*100; cloud[cloud<0] = 0 # Cloud

    # gv + npv + soil + cloud
    summed = gv + npv + soil + cloud
    gvs = (gv/summed)*100

    # npv + soil + cloud
    npvSoil = npv + soil + cloud

    # NDFI
    ndfi_index = (gvs-npvSoil)/(gvs+npvSoil)*100 + 100
    
    return ndfi_index

