## Auditing the Denver/Boulder oSM Street Data and Outputting Data in CSV Files

# Imports
import csv
import codecs
import pprint
import re
import xml.etree.ElementTree as ET
import cerberus
import schema
from update_street_names import update_name
from update_post_codes import update_code


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
		# error_string = pprint.pformat(errors)
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

process_map("denver_sample.osm", validate=True)
