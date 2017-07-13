# 1) Write a function that reads a csv located at "path_to_csv" 
# into a pandas dataframe and adds a new column called 'nameFull'
# with a player's full name.

    #For example:
    #   for Hank Aaron, nameFull would be 'Hank Aaron', 

#2) Write the data in the pandas dataFrame to a new csv file located at
#path_to_new_csv

# Import Pandas
import pandas

def add_full_name(path_to_csv, path_to_new_csv):
	# Add nameFull Field
    baseball_data = pandas.read_csv("Master.csv")
    baseball_data['nameFull'] = baseball_data['nameFirst'] + ' ' + baseball_data['nameLast']
    baseball_data.to_csv(path_to_new_csv)

add_full_name("Master.csv", "Output.csv")
