## Example of Parsing an HTML File using BeautifulSoup

# Imports
from bs4 import BeautifulSoup
import requests

# Functions
def extract_data(page):
    data = {}
    with open(page, "r") as html:
    	soup = BeautifulSoup(html, "lxml")
    	eventvalidation = soup.find(id = '__EVENTVALIDATION')
    	data["eventvalidation"] = eventvalidation['value']
    	viewstate = soup.find(id = '__VIEWSTATE')
    	data['viewstate'] = viewstate['value']
        pass

    return data

def make_request(data):
    eventvalidation = data["eventvalidation"]
    viewstate = data["viewstate"]

    request = requests.post("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
                            data={
                                  'AirportList': "BOS",
                                  'CarrierList': "VX",
                                  'Submit': 'Submit',
                                  "__EVENTTARGET": "",
                                  "__EVENTARGUMENT": "",
                                  "__EVENTVALIDATION": eventvalidation,
                                  "__VIEWSTATE": viewstate
                                  }
                            )

    return request.text

# Get Data
data = extract_data("page_source.html")
print(data["eventvalidation"]) # != "", starts with: "/wEWjAkCoIj1ng0"
print(data["viewstate"]) # start swith: "/wEPDwUKLTI"
