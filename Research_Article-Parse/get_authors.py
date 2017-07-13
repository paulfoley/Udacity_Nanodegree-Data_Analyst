# Example of using ElementTree to Parse a Research XML File

# Imports
import xml.etree.ElementTree as ET

# Create a 'tree' and 'root' file
tree = ET.parse("exampleResearchArticle.xml")
root = tree.getroot()

# Functions
def get_authors(root):
	# Finds Author's: First Name, Last Name, Email, and Insr's
	authors = []
	aus = root.findall('.fm/bibl/aug/au')
	for author in aus:
		author_data = {"insr": []}
		author_data["email"] = author.find('email').text
		author_data["fnm"] = author.find('fnm').text
		author_data["snm"] = author.find("snm").text

		insr = author.findall('insr')
		for i in insr:
			author_data['insr'].append(i.attrib['iid'])

		authors.append(author_data)
	return authors


authors = get_authors(root)
print(authors[0]) # {'insr': ['I1'], 'fnm': 'Omer', 'snm': 'Mei-Dan', 'email': 'omer@extremegate.com'}
print(authors[1]['insr']) # ['I2']