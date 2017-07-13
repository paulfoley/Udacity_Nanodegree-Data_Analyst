## Example of Auditing an OpenStreetMap XML and Outputting CSV Files
"""
After auditing is complete the next step is to prepare the data to be inserted into a SQL database.
To do so you will parse the elements in the OSM XML file, transforming them from document format to
tabular format, thus making it possible to write to .csv files.  These csv files can then easily be
imported to a SQL database as tables.

The process for this transformation is as follows:
- Use iterparse to iteratively step through each top level element in the XML
- Shape each element into several data structures using a custom function
- Utilize a schema and validation library to ensure the transformed data is in the correct format
- Write each data structure to the appropriate .csv files

We've already provided the code needed to load the data, perform iterative parsing and write the
output to csv files. Your task is to complete the shape_element function that will transform each
element into the correct format. To make this process easier we've already defined a schema (see
the schema.py file in the last code tab) for the .csv files and the eventual tables. Using the 
cerberus library we can validate the output against this schema to ensure it is correct.

## Shape Element Function
The function should take as input an iterparse Element object and return a dictionary.

### If the element top level tag is "node":
The dictionary returned should have the format {"node": .., "node_tags": ...}

The "node" field should hold a dictionary of the following top level node attributes:
- id
- user
- uid
- version
- lat
- lon
- timestamp
- changeset
All other attributes can be ignored

The "node_tags" field should hold a list of dictionaries, one per secondary tag. Secondary tags are
child tags of node which have the tag name/type: "tag". Each dictionary should have the following
fields from the secondary tag attributes:
- id: the top level node id attribute value
- key: the full tag "k" attribute value if no colon is present or the characters after the colon if one is.
- value: the tag "v" attribute value
- type: either the characters before the colon in the tag "k" value or "regular" if a colon
        is not present.

Additionally,

- if the tag "k" value contains problematic characters, the tag should be ignored
- if the tag "k" value contains a ":" the characters before the ":" should be set as the tag type
  and characters after the ":" should be set as the tag key
- if there are additional ":" in the "k" value they and they should be ignored and kept as part of
  the tag key. For example:

  <tag k="addr:street:name" v="Lincoln"/>
  should be turned into
  {'id': 12345, 'key': 'street:name', 'value': 'Lincoln', 'type': 'addr'}

- If a node has no secondary tags then the "node_tags" field should just contain an empty list.

### If the element top level tag is "way":
The dictionary should have the format {"way": ..., "way_tags": ..., "way_nodes": ...}

The "way" field should hold a dictionary of the following top level way attributes:
- id
-  user
- uid
- version
- timestamp
- changeset

All other attributes can be ignored

The "way_tags" field should again hold a list of dictionaries, following the exact same rules as
for "node_tags".

Additionally, the dictionary should have a field "way_nodes". "way_nodes" should hold a list of
dictionaries, one for each nd child tag.  Each dictionary should have the fields:
- id: the top level element (way) id
- node_id: the ref attribute value of the nd tag
- position: the index starting at 0 of the nd tag i.e. what order the nd tag appears within
            the way element
"""


# Imports
import csv
import codecs
import pprint
import re
import xml.etree.ElementTree as ET
import cerberus
import schema

# Output CSV FIles
NODES_PATH = "nodes.csv"
NODE_TAGS_PATH = "nodes_tags.csv"
WAYS_PATH = "ways.csv"
WAY_NODES_PATH = "ways_nodes.csv"
WAY_TAGS_PATH = "ways_tags.csv"

# Regular Expressions
LOWER_COLON = re.compile(r'^([a-z]|_)+:([a-z]|_)+')
PROBLEMCHARS = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')
SCHEMA = schema.schema

# Data Audit
NODE_FIELDS = ['id','lat', 'lon', 'user', 'uid', 'version', 'changeset', 'timestamp']
NODE_TAGS_FIELDS = ['id', 'key', 'value', 'type']
WAY_FIELDS = ['id', 'user', 'uid', 'version', 'changeset', 'timestamp']
WAY_TAGS_FIELDS = ['id', 'key', 'value', 'type']
WAY_NODES_FIELDS = ['id', 'node_id', 'position']

# Functions
def shape_element(element, node_attr_fields = NODE_FIELDS, way_attr_fields = WAY_FIELDS, problem_chars = PROBLEMCHARS, default_tag_type = 'regular'):
	# Clean and shape node or way XML element to Python dict
	node_attribs = {}
	way_attribs = {}
	way_nodes = []
	tags = [] # Handle secondary tags the same way for both node and way elements
	
	if element.tag == 'node':
		for attribute in element.attrib:
			if attribute in NODE_FIELDS:
				node_attribs[attribute] = element.attrib[attribute]
		for child in element:
			nodes = {}
			if PROBLEMCHARS.match(child.attrib['k']):
				pass
			elif LOWER_COLON.match(child.attrib['k']):
				nodes["type"] = child.attrib['k'].split(":", 1)[0]
				nodes["key"] = child.attrib['k'].split(":", 1)[1]
				nodes["id"] = element.attrib['id']
				nodes["value"] = child.attrib['v']
				tags.append(nodes)
			else:
				nodes["type"] = "regular"
				nodes["key"] = child.attrib['k']
				nodes["id"] = element.attrib['id']
				nodes["value"] = child.attrib['v']
				tags.append(nodes)
		return {'node': node_attribs, 'node_tags': tags}
	elif element.tag == 'way':
		for attribute in element.attrib:
			if attribute in WAY_FIELDS:
				way_attribs[attribute] = element.attrib[attribute]
		
		position = 0
		for child in element:
			way_n = {}
			way_t = {}
			if child.tag == "nd":
				if element.attrib["id"] not in way_nodes:
					way_n["position"] = position
					way_n["id"] = element.attrib["id"]
					way_n["node_id"] = child.attrib["ref"]
					way_nodes.append(way_n)
					position += 1
				else:
					way_n["position"] = position
					way_n["id"] = element.attrib["id"]
					way_n["node_id"] = child.attrib["ref"]
					way_nodes.append(way_n)
					position += 1
			elif child.tag == "tag":
				if PROBLEMCHARS.match(child.attrib["k"]):
					pass
				elif LOWER_COLON.match(child.attrib["k"]):
					way_t["type"] = child.attrib["k"].split(":",1)[0]
					way_t["key"] = child.attrib["k"].split(":",1)[1]
					way_t["id"] = element.attrib["id"]
					way_t["value"] = child.attrib["v"]
					tags.append(way_t)
				else:
					way_t["type"] = "regular"
					way_t["key"] = child.attrib["k"]
					way_t["id"] = element.attrib["id"]
					way_t["value"] = child.attrib["v"]
					tags.append(way_t)
		return {'way' : way_attribs, 'way_nodes': way_nodes, 'way_tags': tags}

def get_element(filename, tags=('node','way', 'relation')):
	# Yield element if it is the right type of tag
	context = ET.iterparse(filename, events=('start', 'end'))
	_, root = next(context)
	for event, element in context:
		if event == 'end' and element.tag in tags:
			yield element
			root.clear()

def validate_element(element, validator, schema=SCHEMA):
	# Raise ValidationError if element does not match schema
	if validator.validate(element, schema) is not True:
		field, errors = next(validator.errors.items())
		message_string = "\nElement of type '{0}' has the following errors:\n{1}"
		error_string = pprint.pformat(errors)
		raise Exception(message_string.format(field, error_string))

class UnicodeDictWriter(csv.DictWriter, object):
    # Extend csv.DictWriter to handle Unicode input
    def writerow(self, row):
        super(UnicodeDictWriter, self).writerow({
            k: (v.encode('utf-8') if isinstance(v, unicode) else v) for k, v in row.items()
        })

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)

def process_map(file_in, validate):
    # Iteratively process each XML element and write to csv(s)
    with codecs.open(NODES_PATH, 'w') as nodes_file, \
         codecs.open(NODE_TAGS_PATH, 'w') as nodes_tags_file, \
         codecs.open(WAYS_PATH, 'w') as ways_file, \
         codecs.open(WAY_NODES_PATH, 'w') as way_nodes_file, \
         codecs.open(WAY_TAGS_PATH, 'w') as way_tags_file:

        nodes_writer = UnicodeDictWriter(nodes_file, NODE_FIELDS)
        node_tags_writer = UnicodeDictWriter(nodes_tags_file, NODE_TAGS_FIELDS)
        ways_writer = UnicodeDictWriter(ways_file, WAY_FIELDS)
        way_nodes_writer = UnicodeDictWriter(way_nodes_file, WAY_NODES_FIELDS)
        way_tags_writer = UnicodeDictWriter(way_tags_file, WAY_TAGS_FIELDS)

        nodes_writer.writeheader()
        node_tags_writer.writeheader()
        ways_writer.writeheader()
        way_nodes_writer.writeheader()
        way_tags_writer.writeheader()

        validator = cerberus.Validator()

        for element in get_element(file_in, tags=('node', 'way')):
            el = shape_element(element)
            if el:
                if validate is True:
                    validate_element(el, validator)

                if element.tag == 'node':
                    nodes_writer.writerow(el['node'])
                    node_tags_writer.writerows(el['node_tags'])
                elif element.tag == 'way':
                    ways_writer.writerow(el['way'])
                    way_nodes_writer.writerows(el['way_nodes'])
                    way_tags_writer.writerows(el['way_tags'])

process_map("osm_example5.xml", validate=True)