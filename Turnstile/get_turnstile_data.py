'''
The MTA Subway Turnstile data reports on the cumulative number of entries and exits per row. 
'''

## Imports
import pandas as pd
import pandasql

## Data
turnstile_data = pd.read_csv('turnstile-solution.txt', sep = ',', names = ['C/A','UNIT','SCP','DATEn','TIMEn','DESCn','ENTRIESn','EXITSn'])

## Functions
def get_hourly_exits(turnstile_data):
    '''
    This function changes the cumulative exit numbers to a count of exits since the last reading
    (i.e., exits since the last row in the dataframe).
    
    More specifically, you want to do two things:
       `1) Create a new column called EXITSn_hourly
        2) Assign to the column the difference between EXITSn of the current row and the previous row. 
        3) If there is any NaN, fill/replace it with 0.
    '''
    turnstile_data['EXITSn_hourly'] = (turnstile_data['EXITSn'] - turnstile_data['EXITSn'].shift(1)).fillna(0)
    turnstile_data.to_csv("turnstile_exits.csv")

def get_hourly_entries(turnstile_data):
    '''
    This function changes the cumulative entry numbers to a count of entries since the last reading
    (i.e., entries since the last row in the dataframe).
    
    More specifically, you want to do two things:
        1) Create a new column called Entriesn_hourly
        2) Assign to the column the difference between ENTRIESn of the current row  and the previous row. 
        3) If there is any NaN, fill/replace it with 0.
    '''   
    turnstile_data['ENTRIESn_hourly'] = (turnstile_data['ENTRIESn'] - turnstile_data['ENTRIESn'].shift(1)).fillna(1)
    turnstile_data.to_csv("turnstile_entries.csv")

def filter_by_regular(turnstile_data):
    '''
    This function filters the dataframe to only rows where the 'DESCn' column has the value 'REGULAR'.
    
    For example, if the pandas dataframe is as follows:
    ,C/A,UNIT,SCP,DATEn,TIMEn,DESCn,ENTRIESn,EXITSn
    0,A002,R051,02-00-00,05-01-11,00:00:00,REGULAR,3144312,1088151
    1,A002,R051,02-00-00,05-01-11,04:00:00,DOOR,3144335,1088159
    2,A002,R051,02-00-00,05-01-11,08:00:00,REGULAR,3144353,1088177
    3,A002,R051,02-00-00,05-01-11,12:00:00,DOOR,3144424,1088231
    
    The dataframe will look like below after filtering 
    to only rows where DESCn column has the value 'REGULAR':
    0,A002,R051,02-00-00,05-01-11,00:00:00,REGULAR,3144312,1088151
    2,A002,R051,02-00-00,05-01-11,08:00:00,REGULAR,3144353,1088177
    '''
    #### Query
    query = """
            SELECT * 
            FROM turnstile_data 
            WHERE DESCn = 'REGULAR';
            """

    #### Execute the SQL command against the pandas frame
    turnstile_solution = pandasql.sqldf(query, locals())
    turnstile_solution.to_csv("turnstile_regular.csv")

## Outputs
get_hourly_entries(turnstile_data)
get_hourly_exits(turnstile_data)
filter_by_regular(turnstile_data)

