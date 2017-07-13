## Find how many unique users have contributed to the map in this particular area!
"""
Your task is to explore the data a bit more.
The first task is a fun one - find out how many unique users
have contributed to the map in this particular area!

The function process_map should return a set of unique user IDs ("uid")
"""

# Import Libraries
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
	# Process XML File
	users = []
	for _, element in ET.iterparse(filename):
		uid = get_user(element)
		if uid:
			if uid not in users:
				users.append(uid)
	return users

def test():
	users = process_map('osm_example3.xml')
	pprint.pprint(users) # ['451048', '567034', '147510', '26299', '1219059', '939355']

test()
