# Parse XML Data Using Element Tree

# Imports
import xml.etree.ElementTree as ET

# Create 'tree' and 'root'
tree = ET.parse('osm_example1.xml')
root = tree.getroot()

for child in root:
	for c in child:
		print (c.tag)