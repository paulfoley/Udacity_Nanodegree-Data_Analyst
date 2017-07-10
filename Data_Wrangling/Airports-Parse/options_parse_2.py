"""
Complete the 'extract_airports()' function so that it returns a list of airport
codes, excluding any combinations like "All".

Refer to the 'options.html' file in the tab above for a stripped down version
of what is actually on the website. The test() assertions are based on the
given file.
"""

# Imports
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

data = extract_airports("options.html")
print(len(data)) # 15
print(data) # 'ATL' and 'ABR' should be included
