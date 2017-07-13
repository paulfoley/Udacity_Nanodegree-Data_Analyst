'''
    This function should read the csv file located at filename into a pandas dataframe,
    and filter the dataframe to only rows where the 'DESCn' column has the value 'REGULAR'.
    
    For example, if the pandas dataframe is as follows:
    ,C/A,UNIT,SCP,DATEn,TIMEn,DESCn,ENTRIESn,EXITSn
    0,A002,R051,02-00-00,05-01-11,00:00:00,REGULAR,3144312,1088151
    1,A002,R051,02-00-00,05-01-11,04:00:00,DOOR,3144335,1088159
    2,A002,R051,02-00-00,05-01-11,08:00:00,REGULAR,3144353,1088177
    3,A002,R051,02-00-00,05-01-11,12:00:00,DOOR,3144424,1088231
    
    The dataframe will look like below after filtering to only rows where DESCn column
    has the value 'REGULAR':
    0,A002,R051,02-00-00,05-01-11,00:00:00,REGULAR,3144312,1088151
    2,A002,R051,02-00-00,05-01-11,08:00:00,REGULAR,3144353,1088177
'''

# Import Pandas and PandaSQL
import pandas
import pandasql

def filter_by_regular(filename):
    turnstile_data = pandas.read_csv(filename, sep = ',', names = ['C/A','UNIT','SCP','DATEn','TIMEn','DESCn','ENTRIESn','EXITSn'])
    
    # Execute your SQL command against the pandas frame
    query = """ SELECT * 
    FROM turnstile_data 
    WHERE DESCn = 'REGULAR'; """
    
    turnstile_solution = pandasql.sqldf(query, locals())
    turnstile_solution.to_csv("turnstile_output_3.csv")

filter_by_regular('turnstile-solution.txt')