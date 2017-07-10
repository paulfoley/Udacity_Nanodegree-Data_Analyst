## Example of building an XML file using Element Tree

# Import Element Tree
import xml.etree.ElementTree as ET

# Building XML using .Element() and .SubElement()

root = ET.Element('root')
tree_a = ET.SubElement(root, 'tree_a')
tree_b = ET.SubElement(root, 'tree_b')
tree_c = ET.SubElement(tree_b, 'tree_c')

ET.dump(root)