# Use the XLRD Module to Read in ERCOT XLS FIle
# Use the CSV Module to Write Out a CSV File

# Imports
import xlrd
import os
import csv
from zipfile import ZipFile

# Functions
def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    data = {}
    # process all rows that contain station data
    for n in range (1, 9):
        station = sheet.cell_value(0, n)
        cv = sheet.col_values(n, start_rowx=1, end_rowx=None)
        maxval = max(cv)
        maxpos = cv.index(maxval) + 1
        maxtime = sheet.cell_value(maxpos, 0)
        realtime = xlrd.xldate_as_tuple(maxtime, 0)
        data[station] = {"maxval": maxval, "maxtime": realtime}

    print (data)
    return data

def save_file(data, filename):
    with open(filename, "w") as csvfile:
        writer = csv.writer(csvfile, delimiter='|')
        writer.writerow(["Station", "Year", "Month", "Day", "Hour", "Max Load"])
        for s in data:
            year, month, day, hour, _ , _= data[s]["maxtime"]
            writer.writerow([s, year, month, day, hour, data[s]["maxval"]])
 
def output_file():
    data = parse_file("2013_ERCOT_Hourly_Load_Data.xls")
    save_file(data, "2013_Max_Loads.csv")

    number_of_rows = 0
    stations = []
    fields = ['Year', 'Month', 'Day', 'Hour', 'Max Load']
    ans = {'FAR_WEST': {'Max Load': '2281.2722140000024', 'Year': '2013', 'Month': '6','Day': '26','Hour': '17'}}

    with open("2013_Max_Loads.csv") as of:
        csvfile = csv.DictReader(of, delimiter="|")
        for line in csvfile:
            station = line['Station']
            if station == 'FAR_WEST':
                for field in fields:
                    # Check if 'Max Load' is within .1 of answer
                    if field == 'Max Load':
                        max_answer = round(float(ans[station][field]), 1)
                        max_line = round(float(line[field]), 1)
                        if max_answer == max_line:
                            print("Max Load Correct")

            number_of_rows += 1
            stations.append(station)

        # Check
        print(number_of_rows) # 8

        # Check Station Names
        print(set(stations)) #['COAST', 'EAST', 'FAR_WEST', 'NORTH', 'NORTH_C', 'SOUTHERN', 'SOUTH_C', 'WEST']

# Run Script        
output_file()
