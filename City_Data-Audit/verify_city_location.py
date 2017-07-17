"""
In this script we will verify is a citieslocation accuracy
By cross checking the cities longitude and latitude locations.

The function check_loc() will recieve 3 strings: first, the combined
value of "point" followed by the separate "wgs84_pos#" values. 
The output of the function will be true or false based on the verification.

The script Returns a CSV file of locations to check.
"""

## Imports
import csv
from decimal import Decimal

## Functions
def check_loc(point, lat, lon):
    ### Cross Check a Cities Longitude and Latitude Location
    ### Return True or False
    if '|' in point:
        new_point, dispose_point = point.split('|')
        point = new_point.strip('{').strip('}')
    
    if len(point.split(" ")) < 2:
        return False   
    else: 
        p_lat, p_lon = point.split(" ")    
        p_lat = round(Decimal(p_lat),2)
        p_lon = round(Decimal(p_lon),2)
    
    if "|" in lat:
        new_lat, dispose_lat = lat.split('|')
        lat = new_lat.strip('{').strip('}')
    
    if lat == 'NULL':
        return False
    else:
        lat = round(Decimal(lat),2)

    if "|" in lon:
        new_lon, dispose_lon = lon.split('|')
        lon = new_lon.strip('{').strip('}')
    
    if lon == 'NULL':
        return False
    else:
        lon = round(Decimal(lon),2)

    if p_lat == lat and p_lon == lon:
        return True
    else:
        return False

def process_file(filename):
    ### Opens a CSV File and Reads it as Python Dictionary
    data = []
    with open(filename, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        #### Skipping the extra matadata
        for i in range(3):
            l = next(reader)
        
        #### Processing File
        for line in reader:
            ##### Calling the function to check the location
            result = check_loc(line["point"], line["wgs84_pos#lat"], line["wgs84_pos#long"])
            if not result:
               data.append([line['name'], line['point']])

    return data

## Output CSV File
data = process_file('cities.csv')

with open('locations_to_check.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for d in data:
        writer.writerow(d)
