# Returns a list of airport codes, excluding any combinations like "All".

## Import BeautifulSoup
from bs4 import BeautifulSoup
import csv

## Functions
def extract_airports(page):
    ### Get a list of Airports
    airport_values = []
    with open(page, "r") as html:
        #### Setup BeautifulSoup
        soup = BeautifulSoup(html, "lxml")

        #### Get list of Airports
        airport_list = soup.find(id="AirportList")
        airports = airport_list.find_all('option')
        for airport in airports:
            airport_values.append(airport['value'])

    data = []
    for value in airport_values:
        if "All" not in value:
            data.append(value)

    return data

## Output Airports
airports = extract_airports("airport_and_carrier.html")
print("Number of Airports:")
print(len(airports)) # 15

with open('airports.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow("Airports")
    for airport in airports:
        writer.writerow(airport)