'''
Script to query weather data, provided by wunderground.com  to derive insights.

We'll be using Pandas and PandaSQL to perform the various queries:
* Max Temperature on Foggy and Non-Foggy Days
* Number of Rainy Days
* Average Temperature on the weekends
* Average temperatures on rainy days where the minimum temperature is greater then 55
'''

## Import Pandas and PandaSQL
import pandas
import pandasql

## Data
weather_data = pandas.read_csv('weather.csv')

## Functions
def max_temp_aggregate_by_fog(weather_data):
    ### Returns Max Temperature when Foggy or Non-Foggy
    #### Query
    query = """
            SELECT fog, max(maxtempi) as max_temp
            FROM weather_data
            GROUP BY fog;
            """
    
    #### Execute the SQL command against the pandas frame
    foggy_days = pandasql.sqldf(query.lower(), locals())
    
    return foggy_days

def num_rainy_days(weather_data):
    ### Count the number rainy days
    #### Query
    query = """
            SELECT count(rain) as rainy_days
            FROM weather_data
            WHERE rain = 1;
            """
    
    #### Execute the SQL command against the pandas frame
    rainy_days = pandasql.sqldf(query.lower(), locals())
    
    return rainy_days

def avg_weekend_temperature(weather_data):
    ### Returns the average temperature on the weekends
    #### Query
    query = """
            SELECT  avg(cast(meantempi as integer)) as avg_temp
            FROM weather_data
            WHERE cast(strftime('%w', date) as integer) = 0 or cast(strftime('%w', date) as integer) = 6;
            """
    
    #### Execute the SQL command against the pandas frame
    mean_temp_weekends = pandasql.sqldf(query.lower(), locals())
    
    return mean_temp_weekends

def avg_min_temperature(weather_data):
    ### Returns the average temperatures on rainy days where the minimum temperature is greater then 55
    #### Query
    query = """
            SELECT avg(cast(mintempi AS integer)) AS avg_min_temp
            FROM weather_data
            WHERE rain = 1 and mintempi > 55;
            """
    
    #### Execute the SQL command against the pandas frame
    avg_min_temp_rainy = pandasql.sqldf(query.lower(), locals())
    
    return avg_min_temp_rainy

## Output
print(max_temp_aggregate_by_fog(weather_data))
print(num_rainy_days(weather_data))
print(avg_weekend_temperature(weather_data))
print(avg_min_temperature(weather_data))
