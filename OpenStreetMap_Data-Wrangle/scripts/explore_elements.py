## Figure out which and how many tags are in denver.osm file

# Imports
import xml.etree.cElementTree as ET
import pprint

# Create 'tree' and 'root'
tree = ET.parse('denver_sample.osm')
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

# Print Out Results
tags = count_tags()
pprint.pprint(tags)

# Results
"""
{'bounds': 1,
 'member': 39294,
 'nd': 4740351,
 'node': 4109077,
 'osm': 1,
 'relation': 2137,
 'tag': 2230326,
 'way': 460309}
 """
 