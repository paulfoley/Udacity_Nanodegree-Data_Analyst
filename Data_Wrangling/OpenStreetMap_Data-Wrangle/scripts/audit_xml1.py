## Example Auditing Data in an OpenStreetMap XML file using ElementTree

# Imports
import xml.etree.ElementTree as ET
from collections import defaultdict
import re
import pprint

# Regular Expressions
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)

# Audit Data
expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road", "Trail", "Parkway", "Commons"]
mapping = {"St" : "Street", "St." : "Street", "Rd." : "Road", "Ave" : "Avenue"}

# Functions
def audit_street_type(street_types, street_name):
	# Audit's Street Type 
	match = street_type_re.search(street_name)
	if match:
		street_type = match.group()
		if street_type not in expected:
			street_types[street_type].add(street_name)

def is_street_name(element):
	# Get the Street Name
	return (element.attrib['k'] ==  "addr:street")

def audit(filename):
	# Audit Setup
	osm_file = open(filename, "r")
	street_types = defaultdict(set)
	for event, element in ET.iterparse(osm_file, events=("start",)):
		if element.tag == "node" or element.tag == "way":
			for tag in element.iter("tag"):
				if is_street_name(tag):
					audit_street_type(street_types, tag.attrib['v'])
	osm_file.close()
	return street_types

def update_name(name, mapping):
	# Updates Data
	match = street_type_re.search(name)
	if match:
		street_type = match.group()
		if street_type in mapping:
			name = re.sub(street_type, mapping[street_type], name)
	return name


def test():
	st_types = audit('osm_example4.xml')

	for st_type, ways in st_types.items():
		for name in ways:
			better_name = update_name(name, mapping)
			print (name, "=>", better_name)
			# ('West Lexington St.', '=>', 'West Lexington Street')
			# ('Baldwin Rd.', '=>', 'Baldwin Road')
test()