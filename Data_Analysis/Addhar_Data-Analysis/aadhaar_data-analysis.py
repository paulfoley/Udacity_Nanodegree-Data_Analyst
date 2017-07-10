'''
Annalyze the  Aadhaar Data

Firt we need to do some clean up, 
We'll rename the columns by replacing spaces with underscores and setting all characters to lowercase, 
so the column names more closely resemble columns names one might find in a table.

Next we'll select out the first 50 values for "registrar" and "enrolment_agency" 
in the aadhaar_data table using SQL syntax. 

Notes: that "enrolment_agency" is spelled with one l. 
Also, the order of the select does matter. 

Finally, we'll select from the aadhaar_data table how many men and how many women over the age of 50
have had aadhaar generated for them in each district.

aadhaar_generated is a column in the Aadhaar Data that denotes the number who have had aadhaar generated in each row of the table.

The possible columns to select from aadhaar data are:
    1) registrar
    2) enrolment_agency
    3) state
    4) district
    5) sub_district
    6) pin_code
    7) gender
    8) age
    9) aadhaar_generated
    10) enrolment_rejected
    11) residents_providing_email,
    12) residents_providing_mobile_number
'''

# Import Pandas and PandaSQL
import pandas
import pandasql

# Function
def describe(filename):
    # Read in our aadhaar_data csv to a pandas dataframe.  Afterwards, we rename the columns
    # by replacing spaces with underscores and setting all characters to lowercase, so the
    # column names more closely resemble columns names one might find in a table.
    
    aadhaar_data = pandas.read_csv(filename)

    return aadhaar_data.describe()

def select_first_50(filename):
    # Read in Data, Rename Columns, and select the first 50 values
    aadhaar_data = pandas.read_csv(filename)
    aadhaar_data.rename(columns = lambda x: x.replace(' ', '_').lower(), inplace=True)

    q = "SELECT registrar, enrolment_agency FROM aadhaar_data LIMIT 50"

    #Execute your SQL command against the pandas frame
    aadhaar_solution = pandasql.sqldf(q.lower(), locals())
    aadhaar_solution.to_csv("aadhaar_output_1.csv")

def select_state(filename):
    # Read in Data, Rename Columns, and select the first 50 values
    aadhaar_data = pandas.read_csv(filename)
    aadhaar_data.rename(columns = lambda x: x.replace(' ', '_').lower(), inplace=True)

    q = "SELECT * FROM aadhaar_data WHERE state = 'Gujarat';"

    #Execute your SQL command against the pandas frame
    aadhaar_solution = pandasql.sqldf(q.lower(), locals())
    aadhaar_solution.to_csv("aadhaar_output_2.csv")

def select_district(filename):
    # Read in Data, Rename Columns, and select the first 50 values
    aadhaar_data = pandas.read_csv(filename)
    aadhaar_data.rename(columns = lambda x: x.replace(' ', '_').lower(), inplace=True)

    q = """SELECT district, sub_district, sum(aadhaar_generated) 
    		FROM aadhaar_data
    		WHERE age > 60
    		GROUP BY district, sub_district;"""

    #Execute your SQL command against the pandas frame
    aadhaar_solution = pandasql.sqldf(q.lower(), locals())
    aadhaar_solution.to_csv("aadhaar_output_3.csv")

def aggregate_query(filename):
    # Read in our aadhaar_data csv to a pandas dataframe.  Afterwards, we rename the columns
    # by replacing spaces with underscores and setting all characters to lowercase, so the
    # column names more closely resemble columns names one might find in a table.
    
    aadhaar_data = pandas.read_csv(filename)
    aadhaar_data.rename(columns = lambda x: x.replace(' ', '_').lower(), inplace=True)
        
    query = """ SELECT gender, district, sum(aadhaar_generated) 
            FROM aadhaar_data 
            WHERE age > 50
            GROUP BY gender, district; """

    # Execute your SQL command against the pandas frame
    aadhaar_solution = pandasql.sqldf(query.lower(), locals())
    aadhaar_solution.to_csv("aadhaar_output_4.csv")

aggregate_query('aadhaar_data.csv')
select_district('aadhaar_data.csv')
select_first_50('aadhaar_data.csv')
select_state('aadhaar_data.csv')
describe('aadhaar_data.csv')
