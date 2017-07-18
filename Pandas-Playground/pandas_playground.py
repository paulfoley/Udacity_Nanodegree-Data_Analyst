'''
The following code is to play with the Pandas Library.
'''

## Imports
import pandas as pd
from numpy import mean


## Series
'''
You can think of Series as an one-dimensional object that is similar to
an array, list, or column in a database. By default, it will assign an
index label to each item in the Series ranging from 0 to N, where N is
the number of items in the Series minus one.
'''
### Create Series Object
if True:
    series = pd.Series(['Dave', 'Cheng-Han', 'Udacity', 42, -1789710578])
    print(series)

### Custom index in action
'''
You can also manually assign indices to the items 
in the Series when creating the series
'''
if True:
    series = pd.Series(['Dave', 'Cheng-Han', 359, 9001],
                       index=['Instructor', 'Curriculum Manager',
                              'Course Number', 'Power Level'])
    print(series)

### Series indexing in action
'''
You can use index to select specific items from the Series
'''
if True:
    series = pd.Series(['Dave', 'Cheng-Han', 359, 9001],
                       index=['Instructor', 'Curriculum Manager',
                              'Course Number', 'Power Level'])
    print(series['Instructor'])
    print("")
    print(series[['Instructor', 'Curriculum Manager', 'Course Number']])

### Boolean indexing in action
'''
You can also use boolean operators to select specific items from the Series
'''
if True:
    cuteness = pd.Series([1, 2, 3, 4, 5],
                        index=['Cockroach', 'Fish', 'Mini Pig', 'Puppy', 'Kitten'])
    print(cuteness > 3)
    print("")
    print(cuteness[cuteness > 3])


## DataFrame
'''
The following code is to play with the concept of Dataframe in Pandas.

You can think of a Dataframe as something with rows and columns. 
It is similar to a spreadsheet, a database table, or R's data.frame object.

You can think of a DataFrame as a group of Series that share an index.
This makes it easy to select specific columns that you want from the DataFrame.
'''

### Create Dataframe
'''
To create a dataframe, you can pass a dictionary of lists to the Dataframe
constructor:
1) The key of the dictionary will be the column name
2) The associating list will be the values within that column.
'''
football_data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
        'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions',
                    'Lions', 'Lions'],
        'wins': [11, 8, 10, 15, 11, 6, 10, 4],
        'losses': [5, 8, 6, 1, 5, 10, 6, 12]}

football = pd.DataFrame(data)

### Dataframe functions in action
'''
Pandas also has various functions that will help you understand some basic
information about your data frame. 

Some of these functions are:
1) dtypes: to get the datatype for each column
2) describe: useful for seeing basic statistics of the dataframe's numerical
   columns
3) head: displays the first five rows of the dataset
4) tail: displays the last five rows of the dataset
'''
if True:
    print(football.dtypes)
    print("")
    print(football.describe())
    print("")
    print(football.head())
    print("")
    print(football.tail())

### DataFrame indexing in action
'''
Also a couple pointers:
1) Selecting a single column from the DataFrame will return a Series
2) Selecting multiple columns from the DataFrame will return a DataFrame
'''
if True:
    print(football['year'])
    print('')
    print(football.year)  # shorthand for football['year']
    print('')
    print(football[['year', 'wins', 'losses']])

### Boolean Indexing in Action
'''
Row selection can be done through multiple ways.

Some of the basic and common methods are:
   1) Slicing
   2) An individual index (through the functions iloc or loc)
   3) Boolean indexing

You can also combine multiple selection requirements through boolean
operators like & (and) or | (or)
'''
if True:
    print(football.iloc[[0]])
    print("")
    print(football.loc[[0]])
    print("")
    print(football[3:5])
    print("")
    print(football[football.wins > 10])
    print("")
    print(football[(football.wins > 10) & (football.team == "Packers")])

### Another Example of DataFrames
countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
            'Netherlands', 'Germany', 'Switzerland', 'Belarus',
            'Austria', 'France', 'Poland', 'China', 'Korea', 
            'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
            'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
            'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']

gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]

olympic_medal_counts = {
                        'country_name':countries,
                        'gold': pd.Series(gold),
                        'silver': pd.Series(silver),
                        'bronze': pd.Series(bronze)
                        } 

def avg_medal_count(olympic_medal_counts):
    #### Create Medal Count DataFrame
    medal_count = pd.DataFrame(olympic_medal_counts)

    #### Average Number of Bronze Medals For Countries with Atleast One Gold
    avg_bronze_at_least_one_gold = medal_count.mean(df['bronze'][df['gold']>=1])
    
    #### Average Number of Medals
    avg_medal_count = medal_count[['gold','silver','bronze']].apply(mean)
    
    return (avg_medal_count, avg_bronze_at_least_one_gold)

print(avg_medal_count(olympic_medal_counts))




