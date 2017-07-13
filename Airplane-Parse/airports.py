"""
Returns a list of airport codes, excluding any combinations like "All".
"""

# Import BeautifulSoup
from bs4 import BeautifulSoup

# Functions
def extract_airports(page):
    # Get a list of Airports
    airport_values = []
    with open(page, "r") as html:
        # Setup BeautifulSoup
        soup = BeautifulSoup(html, "lxml")

        # Get list of Airports
        airport_list = soup.find(id="AirportList")
        airports = airport_list.find_all('option')
        for airport in airports:
            airport_values.append(airport['value'])

    data = []
    for value in airport_values:
        if "All" not in value:
            data.append(value)

    return data

# Output
airports = extract_airports("airport_and_carrier_list.html")
print("Number of Airports:")
print(len(airports)) # 15

print("Airports:")
print(airports) # 'ATL' and 'ABR' should be included
