"""
Extract the flight data from the 'fl-atl.html' file

This is an example of the data structure you should return:
data = [{"courier": "FL",
         "airport": "ATL",
         "year": 2012,
         "month": 12,
         "flights": {"domestic": 100,
                     "international": 100}
        },
         {"courier": "..."}

"""

## Import BeautifulSoup
from bs4 import BeautifulSoup
import csv

## Function
def process_file(file):
    """
    This function extracts data from the file given as the function argument in a list of dictionaries. 
    
    example: 
    flight = [{"courier": "FL",
             "airport": "ATL",
             "year": 2012,
             "month": 12,
             "flights": {"domestic": 100,
                         "international": 100}
            },
            {"courier": "..."}
    ]

    The table with flight info has a table class="dataTDRight".
    """

    data = []
    info = {}
    info["courier"], info["airport"] = file[:6].split("-")


    # Create a new dictionary for each entry in the output data list
    with open(file, "r") as html:
        soup = BeautifulSoup(html, "lxml")
        flight_list = soup.find(id="DataGrid1")
        flights = flight_list.find_all('tr')
        for flight in flights:
            td_list = []
            tds = flight.find_all('td')
            for td in tds:
                td_list.append(td.get_text())
            if td_list[0] == 'Year':
                pass
            elif td_list[1] == "TOTAL":
                pass
            else:
                info['year'] = int(td_list[0])
                info['month'] = int(td_list[1])
                info['domestic'] = int(td_list[2].replace(',', ''))
                info['international'] = int(td_list[3].replace(',', ''))
                data.append(info.copy())

    return data

## Output Flight Data
flights = process_file("fl-atl.html")

with open('fl-atl.csv', 'w', newline='') as csvfile:
    fieldnames = ['courier', 'airport', 'year', 'month', 'domestic', 'international']
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writeheader()
    for flight in flights:
        writer.writerow(flight)

