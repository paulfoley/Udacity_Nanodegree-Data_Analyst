## Analyze Aadhaar Data
## AAdhaar - The India's government initiative to register their 1 Billion + Citizens

# Import Pandas and PandaSQL
import pandas
import pandasql

# Read in the aadhaar_data CSV to a pandas dataframe. 
aadhaar_data = pandas.read_csv('aadhaar_data.csv')
aadhaar_data.rename(columns = lambda x: x.replace(' ', '_').lower(), inplace=True)

# Function
def describe(aadhaar_data):
    # Describe the Data Set 
    return aadhaar_data.describe()

def select_first_50(aadhaar_data):
    # Select First 50 Data Points
    # Create Query
    q = "SELECT registrar, enrolment_agency FROM aadhaar_data LIMIT 50"

    # Execute your SQL command against the pandas frame
    aadhaar_solution = pandasql.sqldf(q.lower(), locals())
    aadhaar_solution.to_csv("select_first_fifty.csv")

def select_state(aadhaar_data):
    # Filter By State Gujarat
    # Create Query
    q = "SELECT * FROM aadhaar_data WHERE state = 'Gujarat';"

    #Execute your SQL command against the pandas frame
    aadhaar_solution = pandasql.sqldf(q.lower(), locals())
    aadhaar_solution.to_csv("select_state.csv")

def select_district(aadhaar_data):
    # Select District And Sub-District
    # Create Query
    q = """SELECT district, sub_district, sum(aadhaar_generated) 
    		FROM aadhaar_data
    		WHERE age > 60
    		GROUP BY district, sub_district;"""

    # Execute your SQL command against the pandas frame
    aadhaar_solution = pandasql.sqldf(q.lower(), locals())
    aadhaar_solution.to_csv("select_district.csv")

def select_gender(aadhaar_data):
    # Select Gender and District
    # Create Query
    q = """ SELECT gender, district, sum(aadhaar_generated) 
            FROM aadhaar_data 
            WHERE age > 50
            GROUP BY gender, district;"""

    # Execute your SQL command against the pandas frame
    aadhaar_solution = pandasql.sqldf(q.lower(), locals())
    aadhaar_solution.to_csv("select_gender.csv")

# Output Description
print("Aadhaar Data Description:")
print(describe(aadhaar_data))

# Output Files
select_first_50(aadhaar_data)
select_state(aadhaar_data)
select_district(aadhaar_data)
select_gender(aadhaar_data)
