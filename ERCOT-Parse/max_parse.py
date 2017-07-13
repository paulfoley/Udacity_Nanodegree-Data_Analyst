## Get Max Time and Max Value in ERCOT xls file

# Imports
import xlrd

# Function
def parse_file(datafile):
    # Parse an XLS file using XLRD
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    column_values = sheet.col_values(1, start_rowx = 1, end_rowx = None)

    # Get Max and Min Values
    max_value = max(column_values)
    min_value = min(column_values)
    max_pos = column_values.index(max_value) + 1
    min_pos = column_values.index(min_value) + 1

    # Get Max and Min Times
    max_time = sheet.cell_value(max_pos, 0)
    real_time = xlrd.xldate_as_tuple(max_time, 0)
    min_time = sheet.cell_value(min_pos, 0)
    real_min_time = xlrd.xldate_as_tuple(min_time, 0)

    results = {
    'maxtime': real_time,
    'maxvalue': max_value,
    'mintime': real_min_time,
    'minvalue': min_value,
    'avgcoast': sum(column_values)/float(len(column_values))
    }
    return results

data = parse_file("2013_ERCOT_Hourly_Load_Data.xls")

# Print Results
print(data['maxtime']) # (2013, 8, 13, 17, 0, 0)
print(data['maxvalue']) # 18779.02551
