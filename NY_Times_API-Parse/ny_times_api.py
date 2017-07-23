"""
Script to connect to the NY TImes API

Returns a tuple of variables containing the following data:
- labels: list of dictionaries, where the keys are the "section" values and
  values are the "title" values for each of the retrieved articles.
- urls: list of URLs for all 'media' entries with "format": "Standard Thumbnail"
"""

## Imports
import json
import codecs
import requests
import csv

## URL Request
PRIMARY_URL = "https://api.nytimes.com/svc/" # NY Times API URL
API_TYPE = "topstories/v2/" # Top Stories
SECTION = "technology.json" # Technology
URL = PRIMARY_URL + API_TYPE + SECTION # Full URL
API_KEY = "6d0ebec95b0846aeb8ffe8f94eb268bd"

## Functions

### Get JSON file from NY Times
def query_site():
    '''
    Query the NY Times API with key and offset
    NYTimes returns 20 articles per request, 
    if you want the next 20, you have to provide the offset parameter

    Returns Json File of Articles
    '''
    #### Check for API Key
    if API_KEY == "":
        print("You need to register for NYTimes Developer account to run this script")
        return None
    
    #### Set Parameters
    params = {"api-key": API_KEY}

    #### Make Request
    r = requests.get(URL, params = params)

    #### Return JSON File
    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        r.raise_for_status()

def get_json_file():
    '''
    Process all results, by calling the API repeatedly with supplied offset value,
    Combine the data and then write all results in a file.
    '''
    data = query_site()
    num_results = data["num_results"]
    with codecs.open("topstories_technology.json", encoding='utf-8', mode='w') as jsonfile:        
        jsonfile.write(json.dumps(data, indent=2))

### Get Titles and URLs from JSON File
def get_from_file():
    ### Returns json File
    filename = "topstories_technology.json"
    with open(filename, "r") as jsonfile:
        return json.loads(jsonfile.read())

def article_overview():
    ### Returns Titles and Urls of Articles
    data = get_from_file()
    titles = []
    urls =[]
    for row in data["results"]:
        section = row['section']
        
        if row['title']:
            title = row['title']
            titles.append({section: title})
        
        if row['url']:
            urls.append(row['url'])
    return (titles, urls)

## Outputs

### Output JSON File
get_json_file()

### Output Titles and Article URLS
titles, urls = article_overview()

with open('article_titles.csv', 'w') as csvfile:
    fieldnames = ['Technology', 'Business Day', 'Style', 'Theater','Arts','U.S.', 'Health', 'Science', 'Obituaries', 'N.Y. / Region', 'Magazine']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for title in titles:
        writer.writerow(title)

with open('article_urls.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for url in urls:
        writer.writerow([url])
