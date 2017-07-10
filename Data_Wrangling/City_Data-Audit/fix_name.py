"""
Work with cities infobox data, audit it, and then clean it up.

Recieve a string as an input, and it will return a list of all the names. 
If there is only one name, the list will have only one item in it; 
if the name is "NULL", the list should be empty.
"""

# Imports
import csv
import pprint

# Functions
def fix_name(name):
    # Audits the Name column
    name_value = name.strip('{').strip('}')
    if name_value == 'NULL':
        data = []
    elif "|" in name_value:
        a,b = name_value.split('|')
        data = [a,b]
    else:
        data = [name_value]

    return data

def process_file(filename):
    # Opens the CSV File and Reads it into a Python Dictionary
    data = []
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        #skipping the extra metadata
        for i in range(3):
            l = reader.next()
        # processing file
        for line in reader:
            # calling your function to fix the area value
            if "name" in line:
                line["name"] = fix_name(line["name"])
            data.append(line)
    return data

# Test
def test():
    data = process_file('cities.csv')

    # Print Out Results
    print("Printing 20 results:")
    for n in range(20):
        pprint.pprint(data[n]["name"])

    print(data[14]["name"]) # ['Negtemiut', 'Nightmute']
    print(data[9]["name"]) # ['Pell City Alabama']
    print(data[3]["name"]) # ['Kumhari']

test()