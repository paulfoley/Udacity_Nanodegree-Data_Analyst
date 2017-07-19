'''
This script uses the 2013 ERCOT data to find the min, max, and average energy loads.

The XLRD module is used to read in the 2013 ERCOT XLS file.
The CSV module is used to write out a CSV file with the min, max, and average energy loads.
'''

## Imports
import xlrd
import csv

## Functions
def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)

    data = {}
    # Process all rows that contain station data
    for n in range (1, 9):
        station = sheet.cell_value(0, n)
        column_values = sheet.col_values(n, start_rowx=1, end_rowx=None)
        
        # Get Max and Min Values
        max_value = max(column_values)
        max_pos = column_values.index(max_value) + 1
        min_value = min(column_values)
        min_pos = column_values.index(min_value) + 1

        # Get Max and Min Times
        max_time = sheet.cell_value(max_pos, 0)
        max_time_real = xlrd.xldate_as_tuple(max_time, 0)
        min_time = sheet.cell_value(min_pos, 0)
        min_time_real = xlrd.xldate_as_tuple(min_time, 0)

        data[station] = {
                        'Maximum_Value': max_value,
                        'Maximum_Time': max_time_real,
                        'Minimum_Value': min_value,
                        'Minimum_Time': min_time_real,
                        'Average': sum(column_values)/float(len(column_values))
                        }

    return data

def save_file(data, filename):
    with open(filename, "w") as csvfile:
        writer = csv.writer(csvfile, delimiter='|')
        writer.writerow(["Station", "Max Load", "Year", "Month", "Day", "Hour", "Min Load", "Year", "Month", "Day", "Hour", "Average Load"])
        for d in data:
            max_year, max_month, max_day, max_hour, _ , _= data[d]['Maximum_Time']
            min_year, min_month, min_day, min_hour, _ , _= data[d]['Minimum_Time']
            writer.writerow([d, data[d]['Maximum_Value'], max_year, max_month, max_day, max_hour, data[d]['Minimum_Value'], min_year, min_month, min_day, min_hour, data[d]['Average']])
 
# Output Minimum, Maximum, and Average Hourly Energy Loads
data = parse_file("2013_ERCOT_hourly_load_data.xls")
save_file(data, "2013_max_min_loads.csv")
