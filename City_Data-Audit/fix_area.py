"""
Work with cities infobox data, audit it, and then clean it up.

Receive a string as an input, and it has to return a float representing the value of the area or None.
"""

# Imports
import csv
import pprint

# Functions
def fix_area(area):
    area_value = area.strip('{').strip('}')
    if area_value == 'NULL' or area_value == "":
        data = None
    elif "|" not in area_value:
        data = float(area_value)
    else:
        a, b = area_value.split('|')
        if len(a) > len(b):
            data = float(a)
        else:
            data = float(b)

    return data

def process_file(filename):
    # Opens and Reads the CSV File into a Python Dictionary
    data = []

    with open(filename, "r") as f:
        reader = csv.DictReader(f)

        #skipping the extra metadata
        for i in range(3):
            l = reader.next()

        # processing file
        for line in reader:
            # calling your function to fix the area value
            if "areaLand" in line:
                line["areaLand"] = fix_area(line["areaLand"])
            data.append(line)

    return data

# Test
def test():
    data = process_file('cities.csv')
    print("Printing three example results:")
    for n in range(5,8):
        pprint.pprint(data[n]["areaLand"])

    print(data[3]["areaLand"]) # None        
    print(data[8]["areaLand"]) # 55166700.0
    print(data[20]["areaLand"]) # 14581600.0
    print(data[33]["areaLand"]) # 20564500.0    

test()