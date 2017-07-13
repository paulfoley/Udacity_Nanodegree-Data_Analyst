## Parsing a Beatles Diskograpny CSV without CSV Module

# Imports
import os

# Functions
def parse_file(datafile):
    # Parses a File
    data = []
    with open(datafile, "r") as file:
        header = file.readline().split(",")
        for line in file:
            if len(data) >= 10:
                break
            else:
                fields = line.split(",")
                entry = {}
                for i, value in enumerate(fields):
                    entry[header[i].strip()] = value.strip()
                data.append(entry)
    return data

# a simple test of implemetation
datafile = os.path.join("", "beatles-diskography.csv")
d = parse_file(datafile)
print(d[0]) # {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
print(d[9])  # {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964', 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}
