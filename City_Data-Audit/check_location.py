"""
Work with cities infobox data, audit it, and then clean it up.

If you look at the full city data, you will notice that there are couple of
values that seem to provide the same information in different formats: "point"
seems to be the combination of "wgs84_pos#lat" and "wgs84_pos#long". However,
we do not know if that is the case and should check if they are equivalent.

The function check_loc() will recieve 3 strings: first, the combined
value of "point" followed by the separate "wgs84_pos#" values. 
"""

# Imports
import csv
import pprint

# Functions
def check_loc(point, lat, longi):
    p_lat,  p_long = point.split(" ")
    p_lat = float(p_lat)
    p_long = float(p_long)
    lat = float(lat)
    longi = float(longi)

    if p_lat == lat and p_long == longi:
        return True
    else:
        return False

def process_file(filename):
    # Opens a CSV File and Reads it as Python Dictionary
    data = []
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        #skipping the extra matadata
        for i in range(3):
            l = reader.next()
        # processing file
        for line in reader:
            # calling your function to check the location
            result = check_loc(line["point"], line["wgs84_pos#lat"], line["wgs84_pos#long"])
            if not result:
                print ("{}: {} != {} {}".format(line["name"], line["point"], line["wgs84_pos#lat"], line["wgs84_pos#long"]))
            data.append(line)

    return data

data = process_file('cities.csv')
print(check_loc("33.08 75.28", "33.08", "75.28")) # True
print(check_loc("44.57833333333333 -91.21833333333333", "44.5783", "-91.2183")) # False
