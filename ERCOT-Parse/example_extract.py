# Use CSV Module to Extract Data from a CSV File

# Imports
import csv
import os

# Functions
def parse_file(datafile):
	# Function to open datafile
	data = []
	temp_line_dict = {}

	with open(datafile,'r') as file:
		name = file.readline().split(",")[1].replace('"','')
		header = file.readline()
		rows = csv.reader(file)
		for row in rows:
			data.append(row)
	return (name, data)

# Output Some Results
datafile = os.path.join("", "745090.csv")
name, data = parse_file(datafile)
print (name) # MOUNTAIN VIEW MOFFETT FLD NAS
print(data[0][1]) # 01:00
print (data[2][0]) # 01/01/2005
print (data[2][5]) # 2