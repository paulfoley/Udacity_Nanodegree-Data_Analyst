## Example of using ElementTree to Parse and XML file

# Imports
import xml.etree.ElementTree as ET
import pprint

# Create 'tree' and 'root'
tree = ET.parse('exampleResearchArticle.xml')
root = tree.getroot()

# Print Title, and Author Email
title = root.find('./fm/bibl/title')
title_text = ""
for p in title:
	title_text += p.text 
print("Title:", title_text)
print("\nAuthor email addresses:")
for a in root.findall('./fm/bibl/aug/au'):
	email = a.find('email')
	if email is not None:
		print(email.text)
