"""
This script audits the acre field of an area and returns clean data in a csv.

fix_area function takes in a string and returns the number of acres for that area.

The script as a whole outputs a csv of areas with acre data.
"""

## Imports
import csv

## Functions
def fix_area(area):
    ### Takes in an Areas Acre Value and Outputs None or a Float
    area_value = area.strip('{').strip('}')
    if area_value == 'NULL' or area_value == "":
        acres = None
    elif "|" not in area_value:
        acres = float(area_value)
    else:
        a, b = area_value.split('|')
        if len(a) > len(b):
            acres = float(a)
        else:
            acres = float(b)

    return acres

def process_file(filename):
    ### Opens and Reads the CSV File into a Python Dictionary
    data = []
    with open(filename, "r") as f:
        reader = csv.DictReader(f)

        #### Skipping the extra metadata
        for i in range(3):
            l = next(reader)

        #### Processing file
        for line in reader:
            ##### Calling the function to fix the area value
            if "areaLand" in line:
                line["areaLand"] = fix_area(line["areaLand"])
                if type(line["areaLand"]) is float:
                    data.append([line['name'].strip('{').strip('}'), line["areaLand"]])

    return data

## Output
data = process_file('cities.csv')
with open('area_land.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for d in data:
        writer.writerow(d)
