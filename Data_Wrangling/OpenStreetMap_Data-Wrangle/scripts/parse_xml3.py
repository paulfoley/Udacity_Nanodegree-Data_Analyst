## Parse an OpenStreetMap XML File using ElementTree
"""
Your task is to explore the data a bit more.
Before you process the data and add it into your database, you should check the
"k" value for each "<tag>" and see if there are any potential problems.

We have provided you with 3 regular expressions to check for certain patterns
in the tags. As we saw in the quiz earlier, we would like to change the data
model and expand the "addr:street" type of keys to a dictionary like this:
{"address": {"street": "Some value"}}
So, we have to see if we have such tags, and if we have any tags with
problematic characters.

Please complete the function 'key_type', such that we have a count of each of
four tag categories in a dictionary:
  "lower", for tags that contain only lowercase letters and are valid,
  "lower_colon", for otherwise valid tags with a colon in their names,
  "problemchars", for tags with problematic characters, and
  "other", for other tags that do not fall into the other three categories.
See the 'process_map' and 'test' functions for examples of the expected format.
"""

# Imports
import xml.etree.ElementTree as ET
import pprint
import re

# Regular Expressions
lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

# Functions
def key_type(element, keys):
	# Function to understand the key key values
	if element.tag == "tag":
		attribute = element.get('k')
		if bool(lower.search(attribute)):
			keys['lower'] += 1
		elif bool(lower_colon.search(attribute)):
			keys['lower_colon'] += 1
		elif bool(problemchars.search(attribute)):
			keys['problemchars'] += 1
		else:
			keys['other'] +=1
	return keys

def process_map(filename):
	# Function to setup key_type
	keys = {"lower": 0, "lower_colon": 0, "problemchars":0, "other": 0}
	for _, element in ET.iterparse(filename):
		keys = key_type(element, keys)
	return keys

def test():
	# Function to test the code on data set osm_example2.xml
	keys = process_map('osm_example2.xml')
	pprint.pprint(keys) # {'lower':5, 'lower_colon':0, 'other':1, 'problemchars':1}

test()
