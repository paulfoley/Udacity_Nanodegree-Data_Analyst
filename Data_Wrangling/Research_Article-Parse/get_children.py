## Example of Parsing an Research XML File using ElementTree

# Imports
import xml.etree.ElementTree as ET

# Create the 'tree' and 'root'
tree = ET.parse('exampleResearchArticle.xml')
root = tree.getroot()

# Print Children of Root
print("\nChildren of root:")
for child in root:
	print(child.tag)