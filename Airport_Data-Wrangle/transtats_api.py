# Extracted Event Validation and View State Fields to make more requests to trnstats

## Import requests and BeautifulSoup
from bs4 import BeautifulSoup
import requests

## Functions
def extract_data(page):
    data = {}
    with open(page, "r") as html:
    	soup = BeautifulSoup(html, "lxml")
    	eventvalidation = soup.find(id = '__EVENTVALIDATION')
    	data["eventvalidation"] = eventvalidation['value']
    	viewstate = soup.find(id = '__VIEWSTATE')
    	data['viewstate'] = viewstate['value']

    return data

def make_request(data, airport, carrier):
    eventvalidation = data["eventvalidation"]
    viewstate = data["viewstate"]

    request = requests.post("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
                            data={
                                  'AirportList': airport,
                                  'CarrierList': carrier,
                                  'Submit': 'Submit',
                                  "__EVENTTARGET": "",
                                  "__EVENTARGUMENT": "",
                                  "__EVENTVALIDATION": eventvalidation,
                                  "__VIEWSTATE": viewstate
                                  }
                            )

    return request.text

## Extract Event Validation and View Satate Fields
data = extract_data("airport_and_carrier.html")
with open('event_validation.txt', 'w') as txtfile:
  txtfile.write(data["eventvalidation"]) # != "", starts with: "/wEWjAkCoIj1ng0"

with open('view_state.txt', 'w') as txtfile:
  txtfile.write(data["viewstate"]) # start swith: "/wEPDwUKLTI"

## Make Request to Transtats API
airport = "BOS" # Boston Airport
carrier = "VX" # Virgin Airlines
request_text = make_request(data, airport, carrier)
with open("to_" + airport + "_on_" + carrier + ".html", "w") as htmlfile:
  htmlfile.write(request_text)