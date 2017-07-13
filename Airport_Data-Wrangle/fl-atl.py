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
    flight_dict = {}

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
                flight_dict['domestic'] = int(td_list[2].replace(',', ''))
                flight_dict['international'] = int(td_list[3].replace(',', ''))
                info['flights'] = flight_dict.copy()
                data.append(info.copy())

    return data

## Output Flight Data
flight = process_file("fl-atl.html")
print(flight)
