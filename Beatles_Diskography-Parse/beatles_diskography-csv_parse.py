# Parse Beatle's Diskography CSV

# Imports
import os
import csv
import pprint

# Functions
def parse_csv(datafile):
    # Function Parsing a CSV
    data = []
    with open(datafile,'r', encoding='utf-8') as file:
        rows = csv.DictReader(file)
        for row in rows:
            data.append(row)
        return data

datafile = os.path.join("", "beatles-diskography.csv")
results = parse_csv(datafile)
pprint.pprint(results)
