"""
Your task in this exercise is to modify 'extract_carrier()` to get a list of
all airlines. Exclude all of the combination values like "All U.S. Carriers"
from the data that you return. You should return a list of codes for the
carriers.

All your changes should be in the 'extract_carrier()' function. The
'options.html' file in the tab above is a stripped down version of what is
actually on the website, but should provide an example of what you should get
from the full file.

Please note that the function 'make_request()' is provided for your reference
only. You will not be able to to actually use it from within the Udacity web UI.
"""

# Imports
from bs4 import BeautifulSoup

# Functions
def extract_carriers(page):
  # Get a list of Carriers
  carrier_values = []
  with open(page, "r") as html:
    # Setup BeautifulSoup
    soup = BeautifulSoup(html, "lxml")

    # Create list of Carriers
    carrier_list = soup.find(id="CarrierList")
    carriers = carrier_list.find_all('option')
    for carrier in carriers:
      carrier_values.append(carrier['value'])
  
  return carrier_values[3:]

data = extract_carriers("options.html")
print(len(data)) # 16
print(data) # FL and NK should be in data
