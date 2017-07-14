# Import
import csv
import pprint

# Fields to Audit
fieldname = "wgs84_pos#lat"
minval = -90
maxval = 90

# Functions
def skip_lines(input_file, skip):
	for i in range(0, skip):
		next(input_file)

def is_number(s):
	# Determines if input is a string or number
	try:
		float(s)
		return True
	except ValueError:
		return False

def audit_float_field(v, counts):
	## Auditing for Empty, Null, and NaN Fields
	v = v.strip()
	if v == "NULL":
		counts['nulls'] += 1
	elif v == "":
		counts['empties'] += 1
	elif not is_number(v):
		print("Found non number:", v)
	else:
		v = float(v)
		if not ((minval <= v) and (v <= maxval)):
			print ("Found of out of range value:", v)


input_file = csv.DictReader(open("cities.csv"))
skip_lines(input_file, 3)

counts = {"nulls": 0, "empties": 0}
nrows = 0
for row in input_file:
	audit_float_field(row[fieldname], counts)
	nrows += 1

print("num cities:", nrows)
print("nulls:", counts['nulls'])
print('empties:', counts["empties"])