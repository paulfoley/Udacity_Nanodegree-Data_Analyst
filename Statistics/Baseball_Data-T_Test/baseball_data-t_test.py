"""
    Performs a t-test on two sets of baseball data (left-handed and right-handed hitters).

    You will be given a csv file that has three columns.  A player's
    name, handedness (L for lefthanded or R for righthanded) and their
    career batting average (called 'avg'). You can look at the csv
    file by downloading the baseball_stats file from Downloadables below. 
    
    Write a function that will read that the csv file into a pandas data frame,
    and run Welch's t-test on the two cohorts defined by handedness.
    
    One cohort should be a data frame of right-handed batters. And the other
    cohort should be a data frame of left-handed batters.
    
    We have included the scipy.stats library to help you write
    or implement Welch's t-test:
    http://docs.scipy.org/doc/scipy/reference/stats.html
    
    With a significance level of 95%, if there is no difference
    between the two cohorts, return a tuple consisting of
    True, and then the tuple returned by scipy.stats.ttest.  
    
    If there is a difference, return a tuple consisting of
    False, and then the tuple returned by scipy.stats.ttest.
    
    For example, the tuple that you return may look like:
    (True, (9.93570222, 0.000023))
"""

# Import Pandas and Scipy
import pandas
import scipy.stats

# Functions
def perform_t_test(list_1, list_2):
    # Performs a Welch t-test
    t, p = scipy.stats.ttest_ind(list_1, list_2, equal_var=False)
    return t, p

def check_for_significance(t, p, pcrit):
    # Checks for Significance
    if p <= pcrit:
        return False, [t,p]
    else:
        return True [t,p]

def compare_averages(filename):
    # Compares the batting averages of left hand and right hand hitters to see if their is a significant difference
    baseball_dataframe = pandas.read_csv(filename) 
    list_left_handers_avg = baseball_dataframe[baseball_dataframe['handedness'] == 'L']['avg']
    list_right_handers_avg = baseball_dataframe[baseball_dataframe['handedness'] == 'R']['avg']

    t, p = perform_t_test(list_left_handers_avg, list_right_handers_avg)
    result = check_for_significance(t, p, .05)

    return result

# Output Results
print(compare_averages('baseball_stats.csv'))