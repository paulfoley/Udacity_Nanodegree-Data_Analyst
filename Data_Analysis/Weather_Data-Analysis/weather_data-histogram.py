'''
    Before we perform any analysis, it might be useful to take a
    look at the data we're hoping to analyze. More specifically, let's 
    examine the hourly entries in our NYC subway data and determine what
    distribution the data follows. This data is stored in a dataframe
    called turnstile_weather under the ['ENTRIESn_hourly'] column.
    
    Let's plot two histograms on the same axes to show hourly
    entries when raining vs. when not raining. Here's an example on how
    to plot histograms with pandas and matplotlib:
    turnstile_weather['column_to_graph'].hist()
    
    Your histogram may look similar to bar graph in the instructor notes below.
    
    You can read a bit about using matplotlib and pandas to plot histograms here:
    http://pandas.pydata.org/pandas-docs/stable/visualization.html#histograms
'''

# Import Pandas and Matplot
import pandas
import matplotlib.pyplot as plt

turnstile_weather = pandas.read_csv('turnstile_data_master_with_weather.csv') 

def entries_histogram(turnstile_weather):
    plt.figure()
    turnstile_raining = turnstile_weather[turnstile_weather['rain'] == 1]
    turnstile_not_raining = turnstile_weather[turnstile_weather['rain'] == 0]
    
    turnstile_raining['ENTRIESn_hourly'].hist()
    turnstile_not_raining['ENTRIESn_hourly'].hist()
    
    return plt

plot = entries_histogram(turnstile_weather)
plot.show()