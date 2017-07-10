## Example of Parsing an HTML File using BeautifulSoup

# Imports
from bs4 import BeautifulSoup
import requests
import json

# Functions
def options(soup, id):
	# Create a List of Values
	option_values = []
	lists = soup.find(id=id)
	options = lists.find_all('option')
	for option in options:
		option_values.append(option['value'])
	
	return option_values

def print_list(label, codes):
	print('\n%s:' % label)
	for c in codes:
		print (c)

def main():
	# Setup BeautifulSoup
	soup = BeautifulSoup(open("Data_Elements.html"), "lxml")

	# Create a List of Carriers
	carriers = options(soup, "CarrierList")
	print_list("Carriers", carriers)

	# Create a List of Airports
	airports = options(soup, "AirportList")
	print_list("Airports", airports)

main()