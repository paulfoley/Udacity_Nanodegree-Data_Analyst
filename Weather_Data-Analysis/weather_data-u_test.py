'''
    This function will consume the turnstile_weather dataframe containing
    our final turnstile weather data. 
    
    You will want to take the means and run the Mann Whitney U-test on the 
    ENTRIESn_hourly column in the turnstile_weather dataframe.
    
    This function should return:
        1) the mean of entries with rain
        2) the mean of entries without rain
        3) the Mann-Whitney U-statistic and p-value comparing the number of entries
           with rain and the number of entries without rain
    
    You should feel free to use scipy's Mann-Whitney implementation, and you 
    might also find it useful to use numpy's mean function.
    
    Here are the functions' documentation:
    http://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mannwhitneyu.html
    http://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html
'''

# Imports
from scipy.stats import mannwhitneyu
from pandas import DataFrame, read_csv
from numpy import mean


turnstile_weather = read_csv('turnstile_data_master_with_weather.csv') 

def mann_whitney_plus_means(turnstile_weather):
    turnstile_raining = turnstile_weather[turnstile_weather['rain'] == 1]['ENTRIESn_hourly']
    turnstile_not_raining = turnstile_weather[turnstile_weather['rain'] == 0]['ENTRIESn_hourly']

    print(turnstile_raining)

    with_rain_mean = mean(turnstile_raining)
    without_rain_mean = mean(turnstile_not_raining)

    U, p = mannwhitneyu(turnstile_raining, turnstile_not_raining)
    
    return with_rain_mean, without_rain_mean, U, p

print(mann_whitney_plus_means(turnstile_weather))