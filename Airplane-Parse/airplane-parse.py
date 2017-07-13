## Example of Parsing an HTML File using BeautifulSoup

# Imports
from bs4 import BeautifulSoup
import requests

request = requests.Session().get("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2")
soup = BeautifulSoup(request.text, "lxml")

viewstate_element = soup.find(id='__VIEWSTATE')
viewstate = viewstate_element['value']
eventvalidation_element = soup.find(id='__EVENTVALIDATION')
eventvalidation = eventvalidation_element['value']
viewstategenerator_element = soup.find(id='__VIEWSTATEGENERATOR')
viewstategenerator = viewstategenerator_element['value']

request = requests.Session().post("https://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
                                   data = (
                                           ("__EVENTTARGET", ""),
                                           ("__EVENTARGUMENT", ""),
                                           ("__VIEWSTATE", viewstate),
                                           ("__VIEWSTATEGENERATOR",viewstategenerator),
                                           ("__EVENTVALIDATION", eventvalidation),
                                           ("CarrierList", "VX"),
                                           ("AirportList", "BOS"),
                                           ("Submit", "Submit")
                                          ))

file = open('virgin_and_logan_airport.html', 'w')
file.write(request.text)