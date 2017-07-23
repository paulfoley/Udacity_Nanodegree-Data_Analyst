'''
In this script we're going to explore how turnstile entries and exits 
are effected by their features.

Specifically we'll:

1) Visualize the turnstile entries when raining versus not raining

2) Create predictions on number of entries based on features

3) Visualize Cost History

4) Plot residuals to see how far off our predictions are

5) Perform a Mann Whitney U Test
'''

## Imports
import numpy as np
import pandas as pd
import scipy as sc
import matplotlib.pyplot as plt
from ggplot import *

## Data
turnstile_weather = pd.read_csv('turnstile_data_master_with_weather.csv') 

## Histogram of Ridership when Raining and when Not Raining
def entries_histogram(turnstile_weather):
    '''
    Function examines the hourly entries in the NYC subway 
    and determines what distribution the data follows. 
    This data is stored in a dataframe called turnstile_weather under the ['ENTRIESn_hourly'] column.
    
    The function plots two histograms on the same axes 
    to show hourly entries when raining vs. when not raining. 
    '''
    
    turnstile_raining = turnstile_weather[turnstile_weather['rain'] == 1]
    turnstile_not_raining = turnstile_weather[turnstile_weather['rain'] == 0]
    
    #### Plot Histgoram
    plt.figure()
    #### Creates Histogram of Entries When Raining Vs. Not Raining
    turnstile_raining['ENTRIESn_hourly'].hist()
    turnstile_not_raining['ENTRIESn_hourly'].hist()
    
    return plt

## Precition of Ridership
def normalize_features(df):
    """
    Normalize the features in the data set.
    """
    mu = df.mean()
    sigma = df.std()
    
    if (sigma == 0).any():
        raise Exception("One or more features had the same value for all samples, and thus could " + \
                         "not be normalized. Please do not include features with only a single value " + \
                         "in your model.")
    df_normalized = (df - df.mean()) / df.std()

    return df_normalized, mu, sigma

def compute_cost(features, values, theta):
    """
    Compute the cost function given a set of features / values, 
    and the values for our thetas.
    """
    m = len(values)
    sum_of_square_errors = np.square(np.dot(features, theta) - values).sum()
    cost = sum_of_square_errors / (2*m)

    return cost

def gradient_descent(features, values, theta, alpha, num_iterations):
    """
    Perform gradient descent given a data set with an arbitrary number of features.
    """
    
    m = len(values)
    cost_history = []

    for i in range(num_iterations):
        predicted_values = np.dot(features, theta)
        theta = theta - alpha / m * np.dot((predicted_values - values), features)

        cost = compute_cost(features, values, theta)
        cost_history.append(cost)

    return theta, pd.Series(cost_history)

def plot_cost_history(alpha, cost_history):
   """
   This function is for viewing the plot of your cost history.
   """
   cost_df = pd.DataFrame({
      'Cost_History': cost_history,
      'Iteration': range(len(cost_history))
   })
   return ggplot(cost_df, aes('Iteration', 'Cost_History')) + geom_point() + ggtitle('Cost History for alpha = %.3f' % alpha)

def predictions(dataframe):
    '''
    Function to predict the ridership of the NYC subway 
    using linear regression with gradient descent.    
    
    Also outputs a plot of your cost history for reference
    The slowdown from plotting is significant, 
    so if you  are timing out, the first thing to do is to comment out the plot command again.
'''
    ### Select Features (try different features!)
    features = dataframe[['rain', 'precipi', 'Hour', 'meantempi']]
    
    ### Add UNIT to features using dummy variables
    dummy_units = pd.get_dummies(dataframe['UNIT'], prefix='unit')
    features = features.join(dummy_units)
    
    ### Values
    values = dataframe['ENTRIESn_hourly']
    m = len(values)

    ### Normalize Features
    features, mu, sigma = normalize_features(features)
    features['ones'] = np.ones(m) # Add a column of 1s (y intercept)
    
    ### Convert Features and values to numpy arrays
    features_array = np.array(features)
    values_array = np.array(values)

    ### Set values for alpha, number of iterations.
    alpha = 0.1 # Please feel free to change this value
    num_iterations = 75 # Please feel free to change this value

    ### Initialize theta, perform gradient descent
    theta_gradient_descent = np.zeros(len(features.columns))
    theta_gradient_descent, cost_history = gradient_descent(features_array, 
                                                            values_array, 
                                                            theta_gradient_descent, 
                                                            alpha, 
                                                            num_iterations)

    ### Plots cost history
    plot = plot_cost_history(alpha, cost_history)

    ### Get Predictions
    predictions = np.dot(features_array, theta_gradient_descent)
    
    return predictions, plot

## Histogram of Residuals from Predictions
def plot_residuals(turnstile_weather, predictions):
    '''
    Make a histogram of the residuals
    The difference between the original hourly entry data and the predicted values.
    '''
    plt.figure()
    (turnstile_weather['ENTRIESn_hourly'] - predictions).hist()
    
    return plt

## Perform Man Whitney U Test
def mann_whitney_plus_means(turnstile_weather):
    '''
    Function take the means and runs the Mann Whitney U-test 
    on the ENTRIESn_hourly column in the turnstile_weather dataframe.
    
    This function will return:
        1) the mean of entries with rain
        2) the mean of entries without rain
        3) the Mann-Whitney U-statistic and p-value comparing the number of entries
           with rain and the number of entries without rain
    '''
    turnstile_raining = turnstile_weather[turnstile_weather['rain'] == 1]['ENTRIESn_hourly']
    turnstile_not_raining = turnstile_weather[turnstile_weather['rain'] == 0]['ENTRIESn_hourly']

    print(turnstile_raining)

    with_rain_mean = np.mean(turnstile_raining)
    without_rain_mean = np.mean(turnstile_not_raining)

    U, p = sc.stats.mannwhitneyu(turnstile_raining, turnstile_not_raining)
    
    return with_rain_mean, without_rain_mean, U, p

## Outputs

### Plots
entries_plot = entries_histogram(turnstile_weather)
entries_plot.show()

predictions, plot_cost_history = predictions(turnstile_weather)
print(plot_cost_history)

residual_plot = plot_residuals(turnstile_weather, predictions)
residual_plot.show()

### Terminal Output
print("Predictions:")
print(predictions)
print("\nU Test:")
print(mann_whitney_plus_means(turnstile_weather))
