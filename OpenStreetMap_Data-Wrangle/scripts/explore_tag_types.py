## Prints out the tag values to allow us to get a better understanding of the Tag Elements

# Imports
import xml.etree.ElementTree as ET
import pprint

# Functions
def count_tag_type(element, tags):
	# Counts the tag types
	if element.tag == "tag":
		attribute = element.get('k')
		if attribute in tags:
			tags[attribute] += 1
		else:
			tags[attribute] = 1

	return tags

def process_map(filename):
	# Processes the OSM File returns tag value and the count
	tags = {}
	for _, element in ET.iterparse(filename):
		tags = count_tag_type(element, tags)
	return tags

# Print Out Results
keys = process_map('denver_sample.osm')
pprint.pprint(keys)