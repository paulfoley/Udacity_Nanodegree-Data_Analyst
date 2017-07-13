## Script to find out how many users have contributed to this particular area

# Imports
import xml.etree.ElementTree as ET
import pprint
import re

# Functions
def get_user(element):
	# Get Users
	uid = ""
	if element.tag == 'node' or element.tag == 'way' or element.tag == 'relation':
		uid = element.get('uid')
	return uid

def process_map(filename):
	# Process OSM Data and returns a Dictionary of Users with their contribution count
	users = {}
	for _, element in ET.iterparse(filename):
		uid = get_user(element)
		if uid:
			if uid not in users:
				users[uid] = 1
			else:
				users[uid] +=1
	return users

# Print Results
users = process_map('denver_sample.osm')
pprint.pprint(users)
