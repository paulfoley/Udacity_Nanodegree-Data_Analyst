## Script to explore postal code and outputs

# Imports
import xml.etree.ElementTree as ET
import pprint

# Functions
def audit_post_code(element):
	# Finds Post Codes that are Not Correctly Formatted
	post_code = 0
	if element.tag == 'tag':
		attribute = element.get('k')
		if attribute == 'addr:postcode':
			post_code = element.get('v')
			if len(post_code) > 5:
				return post_code

def process_map(filename):
	# Process OSM Data and returns a Dictionary of Users with their contribution count
	post_codes = []
	for _, element in ET.iterparse(filename):
		post_code = audit_post_code(element)
		if post_code:
			post_codes.append(post_code)
	
	return post_codes

# Print Results
post_codes = process_map('denver_sample.osm')
pprint.pprint(post_codes)
