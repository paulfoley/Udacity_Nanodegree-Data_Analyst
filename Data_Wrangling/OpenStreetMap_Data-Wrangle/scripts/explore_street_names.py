## Audits Street Names in the OSM File and returns Unexpected Values

# Imports
import xml.etree.ElementTree as ET
from collections import defaultdict
import re
import pprint

# Using a Regular Expression to get Street Type
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)

# Expected Street Names
expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Circle", "Lane", "Road", "Trail", "Parkway", "Way"]

# Functions
def audit_street_type(street_types, street_name):
	# Checks to see if the Street has the expected ending
	match = street_type_re.search(street_name)
	if match:
		street_type = match.group()
		if street_type not in expected:
			street_types[street_type].add(street_name)

def process_map(filename):
	# Takes in the OSM File, loops through it's tags and then runs audit_street_type
	osm_file = open(filename, "r")
	street_types = defaultdict(set)
	for event, element in ET.iterparse(osm_file, events=("start",)):
		if element.tag == "node" or element.tag == "way":
			for tag in element.iter("tag"):
				if tag.attrib['k'] ==  "addr:street":
					audit_street_type(street_types, tag.attrib['v'])
	osm_file.close()
	return street_types

# Print Output
st_types = process_map('denver_sample.osm')
pprint.pprint(dict(st_types))
