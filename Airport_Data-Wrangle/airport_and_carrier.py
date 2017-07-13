# Prints list of Carriers and Airports

## Imports
from bs4 import BeautifulSoup
import requests
import json

## Sub-Functions
def options(soup, id):
	### Create a List of Options
	option_values = []
	lists = soup.find(id=id)
	options = lists.find_all('option')

	for option in options:
		option_values.append(option['value'])
	
	return option_values

def print_list(label, codes):
	### Function to Easily Print a List
	print('\n%s:' % label)
	for c in codes:
		print(c)

## Main Function
def get_airport_carriers():
	# Setup BeautifulSoup
	soup = BeautifulSoup(open("airport_and_carrier_list.html"), "lxml")

	# Create a List of Carriers
	carriers = options(soup, "CarrierList")
	print_list("Carriers", carriers)

	# Create a List of Airports
	airports = options(soup, "AirportList")
	print_list("Airports", airports)

## Output Airports and Carriers
get_airport_carriers()