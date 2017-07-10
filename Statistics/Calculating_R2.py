'''    
    Given a list of original data points, and also a list of predicted data points,
    write a function that will compute and return the coefficient of determination (R^2)
    for this data.  numpy.mean() and numpy.sum() might both be useful here, but
    not necessary.

    Documentation about numpy.mean() and numpy.sum() below:
    http://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html
    http://docs.scipy.org/doc/numpy/reference/generated/numpy.sum.html
'''
# Import Numpy
import numpy

def compute_r_squared(data, predictions):
    '''
    A function that, given two input numpy arrays, 'data', and 'predictions,'
    returns the coefficient of determination, R^2, 
    for the model that produced predictions.
    '''
    SST = ((data - numpy.mean(data))**2).sum()
    SSReg = ((predictions - data)**2).sum()
    r_squared = 1 - SSReg / SST
    
    return r_squared