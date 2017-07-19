"""
Fix city names in the data

The fix_name function return a list of all the names, removing Null's  
If there is only one name, the list will have only one item in it; 
If there are multiple names, only the first will be taken

The script as a whole outputs the cleaned names of areas in a csv file
"""

## Imports
import csv

## Functions
def fix_name(name):
    ### Audits the Name Column of City Data
    name_list = []
    name_value = name.strip('{').strip('}')

    if name_value == 'NULL':
        name_list = []
    elif "|" in name_value:
        name_list.append(name_value.split('|')[0])
    else:
        name_list = [name_value]

    #### Return Cleaned Name
    return name_list

def process_file(filename):
    ### Opens the CSV File and Reads it into a Python Dictionary
    data = []
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        #### Skipping the extra metadata
        for i in range(3):
            l = next(reader)
        #### Processing file
        for line in reader:
            ##### calling the Fix Name Function to fix the area value
            if "name" in line:
                line["name"] = fix_name(line["name"])
                data.append(line['name'])
    
    ### Returns Cleaned Data
    return data

## Output
data = process_file('cities.csv')
with open('area_names.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow("Area_Names:")
    for d in data:
        writer.writerow(d)