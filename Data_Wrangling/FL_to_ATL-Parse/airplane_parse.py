"""
Let's assume that you combined the code from the previous 2 exercises with code
from the lesson on how to build requests, and downloaded all the data locally.
The files are in a directory "data", named after the carrier and airport:
"{}-{}.html".format(carrier, airport), for example "FL-ATL.html".

The table with flight info has a table class="dataTDRight". Your task is to
use 'process_file()' to extract the flight data from that table as a list of
dictionaries, each dictionary containing relevant data from the file and table
row. This is an example of the data structure you should return:

data = [{"courier": "FL",
         "airport": "ATL",
         "year": 2012,
         "month": 12,
         "flights": {"domestic": 100,
                     "international": 100}
        },
         {"courier": "..."}
]

Note - year, month, and the flight data should be integers.
You should skip the rows that contain the TOTAL data for a year.

There are couple of helper functions to deal with the data files.
Please do not change them for grading purposes.
All your changes should be in the 'process_file()' function.

The 'FL-ATL.html' file in the tab above is only a part of the full data,
covering data through 2003. The test() code will be run on the full table, but
the given file should provide an example of what you will get.
"""

# Imports
from bs4 import BeautifulSoup

# Functions
def process_file(file):
    """
    This function extracts data from the file given as the function argument in
    a list of dictionaries. This is example of the data structure you should
    return:

    data = [{"courier": "FL",
             "airport": "ATL",
             "year": 2012,
             "month": 12,
             "flights": {"domestic": 100,
                         "international": 100}
            },
            {"courier": "..."}
    ]


    Note - year, month, and the flight data should be integers.
    You should skip the rows that contain the TOTAL data for a year.
    """
    data = []
    info = {}
    info["courier"], info["airport"] = file[:6].split("-")
    flight_dict = {}
    # Note: create a new dictionary for each entry in the output data list.
    # If you use the info dictionary defined here each element in the list 
    # will be a reference to the same info dictionary.
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

data = process_file("FL-ATL.html")
print(data)
