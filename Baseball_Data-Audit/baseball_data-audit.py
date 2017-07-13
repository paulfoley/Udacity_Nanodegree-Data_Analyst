# Pandas dataframes have a method called 'fillna(value)', 
# such that you can pass in a single value to replace any NAs in a dataframe or series. 
# You can call it like this: 
#     dataframe['column'] = dataframe['column'].fillna(value)

# Using the numpy.mean function, which calculates the mean of a numpy array,
# impute any missing values in our Lahman baseball data sets 'weight' column 
# by setting them equal to the average weight.

# You can access the 'weight' colum in the baseball data frame by calling baseball['weight']

# Import Pandas and Numpy
import pandas
import numpy

# Function
def impute(filename):
    # Fill in the blank 'wegiht' fields in the baseball data set
    baseball = pandas.read_csv(filename)
    avg_weight = numpy.mean(baseball['weight'])
    baseball['weight'] = baseball['weight'].fillna(avg_weight)
    return baseball['weight']

print(impute('Master.csv'))