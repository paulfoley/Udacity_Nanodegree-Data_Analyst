"""
Return a list of codes for all airline carriers. 
Excludes all of the combination values like "All U.S. Carriers"
"""

## Import BeautifulSoup
from bs4 import BeautifulSoup
import csv

## Function
def extract_carriers(page):
  ### Get a list of Carriers
  carrier_values = []
  with open(page, "r") as html:
    #### Setup BeautifulSoup
    soup = BeautifulSoup(html, "lxml")

    #### Create list of Carriers
    carrier_list = soup.find(id="CarrierList")
    carriers = carrier_list.find_all('option')
    for carrier in carriers:
      carrier_values.append(carrier['value'])
  
  return carrier_values[3:]

## Output Carriers
carriers = extract_carriers("airport_and_carrier.html")
print("Number of Carriers:")
print(len(carriers)) # 16

with open('carriers.csv', 'w', newline='') as csvfile:
  writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
  writer.writerow("Carriers")
  for carrier in carriers:
    writer.writerow(carrier)
