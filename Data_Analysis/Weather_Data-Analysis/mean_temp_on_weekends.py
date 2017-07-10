'''
    This function should run a SQL query on a dataframe of
    weather data.  The SQL query should return one column and
    one row - the average meantempi on days that are a Saturday
    or Sunday (i.e., the the average mean temperature on weekends).
    The dataframe will be titled 'weather_data' and you can access
    the date in the dataframe via the 'date' column.
    
    You'll need to provide  the SQL query.
    
    You might also find that interpreting numbers as integers or floats may not
    work initially.  In order to get around this issue, it may be useful to cast
    these numbers as integers.  This can be done by writing cast(column as integer).
    So for example, if we wanted to cast the maxtempi column as an integer, we would actually
    write something like where cast(maxtempi as integer) = 76, as opposed to simply 
    where maxtempi = 76.
    
    Also, you can convert dates to days of the week via the 'strftime' keyword in SQL.
    For example, cast (strftime('%w', date) as integer) will return 0 if the date
    is a Sunday or 6 if the date is a Saturday.
'''

# Import Pandas and PandaSQL
import pandas
import pandasql

def avg_weekend_temperature(filename):
    # Returns the average temperature on the weekends
    weather_data = pandas.read_csv(filename)

    query = """
    SELECT  avg(cast(meantempi as integer)) as avg_temp
    FROM weather_data
    WHERE cast(strftime('%w', date) as integer) = 0 or cast(strftime('%w', date) as integer) = 6;
    """
    
    #Execute your SQL command against the pandas frame
    mean_temp_weekends = pandasql.sqldf(query.lower(), locals())
    return mean_temp_weekends

print(avg_weekend_temperature('weather_underground.csv'))