"""
Work with cities infobox data, audit it, and then clean it up. 
Audit the datatypes that can be found in some particular fields in the dataset.

The possible types of values can be:
- NoneType if the value is a string "NULL" or an empty string ""
- list, if the value starts with "{"
- int, if the value can be cast to int
- float, if the value can be cast to float, but CANNOT be cast to int.
   For example, '3.23e+07' should be considered a float because it can be cast
   as float but int('3.23e+07') will throw a ValueError
- 'str', for all other values

The audit_file function should return a dictionary containing fieldnames and a 
SET of the types that can be found in the field. e.g.

{"field1": set([type(float()), type(int()), type(str())]),
 "field2": set([type(str())]),
  ....
}

The type() function returns a type object describing the argument given to the 
function.

Note that the first three rows (after the header row) in the cities.csv file
are not actual data points. The contents of these rows should note be included
when processing data types.
"""

# Imports
import csv
import pprint

# Fields for Auditing
FIELDS = ["name", "timeZone_label", "utcOffset", "homepage", "governmentType_label",
          "isPartOf_label", "areaCode", "populationTotal", "elevation",
          "maximumElevation", "minimumElevation", "populationDensity",
          "wgs84_pos#lat", "wgs84_pos#long", "areaLand", "areaMetro", "areaUrban"]

# Function
def audit_file(filename, fields):
  fieldtypes = {}
  extra_fields = []

  for field in fields:
    fieldtypes[field] = set()
  
  with open(filename, 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    for line in reader:
      if 'dbpedia' not in line['URI']:
        extra_fields.append(line)
      else:
        for field in fields:
          try:
            if line[field][0] =='{':
              fieldtypes[field].add(type([]))
            elif line[field] == '' or line[field] == 'NULL':
              fieldtypes[field].add(type(None))
            elif int(line[field]):
              fieldtypes[field].add(type(1))

          except ValueError:
            try:
              if float(line[field]):
                fieldtypes[field].add(type(1.1))
            
            except ValueError:
              fieldtypes[field].add(type(line[field]))
  
  return fieldtypes

# Test
def test():
    fieldtypes = audit_file('cities.csv', FIELDS)

    # Print Output
    pprint.pprint(fieldtypes)
    print(fieldtypes["areaLand"])
    print(fieldtypes['areaMetro'])
    
test()
