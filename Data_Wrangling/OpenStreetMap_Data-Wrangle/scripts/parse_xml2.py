## Example of Parsing an XML File using ElementTree's Iterative Parsing
"""
Your task is to use the iterative parsing to process the map file and
find out not only what tags are there, but also how many, to get the
feeling on how much of which data you can expect to have in the map.
Fill out the count_tags function. It should return a dictionary with the 
tag name as the key and number of times this tag can be encountered in 
the map as value.
"""

# Imports
import xml.etree.cElementTree as ET
import pprint

# Create 'tree' and 'root'
tree = ET.parse('osm_example3.xml')
root = tree.getroot()

# Functions
def count_tags():
    # Counts Tags
    tags = {}
    tags[root.tag] = 1
    for child in root:
        if child.tag not in tags:
        	tags[child.tag] = 1
        else:
        	tags[child.tag] += 1

        for c in child:
        	if c.tag not in tags:
        		tags[c.tag] = 1
        	else:
        		tags[c.tag] += 1
        			
    return tags


def test():
    tags = count_tags()
    pprint.pprint(tags) # {'bounds': 1, 'member': 3, 'nd': 4, 'node': 20, 'osm': 1, 'relation': 1, 'tag': 7, 'way': 1}

test()