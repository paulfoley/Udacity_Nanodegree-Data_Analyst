'''
    This function should run a SQL query on a dataframe of
    weather data. More specifically you want to find the average
    minimum temperature (mintempi column of the weather dataframe) on 
    rainy days where the minimum temperature is greater than 55 degrees.
    
    You might also find that interpreting numbers as integers or floats may not
    work initially.  In order to get around this issue, it may be useful to cast
    these numbers as integers.  This can be done by writing cast(column as integer).
    So for example, if we wanted to cast the maxtempi column as an integer, we would actually
    write something like where cast(maxtempi as integer) = 76, as opposed to simply 
    where maxtempi = 76.
'''
import pandas
import pandasql

def avg_min_temperature(filename):
    # Returns the average of minimum temperatures on rainy days where the minimum temperature is greater then 55
    weather_data = pandas.read_csv(filename)

    query = """
    SELECT avg(cast(mintempi AS integer)) AS avg_min_temp
    FROM weather_data
    WHERE rain = 1 and mintempi > 55;
    """
    
    #Execute your SQL command against the pandas frame
    avg_min_temp_rainy = pandasql.sqldf(query.lower(), locals())
    return avg_min_temp_rainy

print(avg_min_temperature('weather_underground.csv'))