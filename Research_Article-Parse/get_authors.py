# Parse a Research Article for Author Names and Paper Titles

## Imports
import xml.etree.ElementTree as ET
import csv

## Create a 'tree' and 'root' file
tree = ET.parse("research_article.xml")
root = tree.getroot()

## Functions

### Get Title and Author Email
title = root.find('./fm/bibl/title')
title_text = ""
for p in title:
	title_text += p.text
heading = "Title: " + title_text 	

def get_authors(root):
	# Finds Author's: First Name, Last Name, Email, and Insr's
	author_list = []
	authors = root.findall('.fm/bibl/aug/au')
	for author in authors:
		author_data = {"insr": []}
		author_data["Email"] = author.find('email').text
		author_data["First Name"] = author.find('fnm').text
		author_data["Last Name"] = author.find("snm").text

		insr = author.findall('insr')
		for i in insr:
			author_data['insr'].append(i.attrib['iid'])

		author_list.append(author_data)
	return author_list

### Output of Authors in a CSV file
authors = get_authors(root)
with open('authors.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(heading)
    
    fieldnames = ['insr', 'Email', 'First Name', 'Last Name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for author in authors:
    	writer.writerow(author)