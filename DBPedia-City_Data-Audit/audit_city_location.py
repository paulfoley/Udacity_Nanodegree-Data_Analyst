'''
We want to know how many cities have a valid locations in our cities.csv data set.
As well as know how many of the cities have 'Null' or 'Empty' locations.

In the audit_city_location function we'll count the number of cties 
that have a 'Null' or 'Empty' or empty location.
'''

## Import
import csv

## Fields to Audit
fieldname = "wgs84_pos#lat"
minval = -90
maxval = 90

## Functions
def skip_lines(input_file, skip):
	### Skips intial lines
	for i in range(0, skip):
		next(input_file)

def is_number(s):
	### Determines if input is a string or number
	try:
		float(s)
		return True
	except ValueError:
		return False

def audit_city_location(v, counts):
	### Auditing for Empty, Null, and NaN Fields
	v = v.strip()
	if '{' in v or '}' in v:
		v = v.strip('{').strip('}')
	
	if v == "NULL":
		counts['nulls'] += 1
	elif v == "":
		counts['empties'] += 1
	elif '|' in v:
		v_list = v.split('|')
		for u in v_list:
			if not is_number(u):
				print("Found non number:", u)
			else:
				u = float(u)
				if not ((minval <= u) and (u <= maxval)):
					print ("Found of out of range value:", u)
	else:
		v = float(v)
		if not ((minval <= v) and (v <= maxval)):
			print ("Found of out of range value:", v)

## Output
input_file = csv.DictReader(open("cities.csv"))
skip_lines(input_file, 3)

counts = {"nulls": 0, "empties": 0}
nrows = 0
for row in input_file:
	valid_city(row[fieldname], counts)
	nrows += 1

print("num cities:", nrows)
print("nulls:", counts['nulls'])
print('empties:', counts["empties"])
