"""
Script to connect to the NY TImes API

To run this code locally you have to register at the NYTimes developer site 
and get your own API key.

Returns a tuple of variables containing the following data:
- labels: list of dictionaries, where the keys are the "section" values and
  values are the "title" values for each of the retrieved articles.
- urls: list of URLs for all 'media' entries with "format": "Standard Thumbnail"
"""

## Imports
import json
import codecs
import requests

## URL Request
URL_MAIN = "http://api.nytimes.com/svc/"
URL_POPULAR = URL_MAIN + "mostpopular/v2/"
API_KEY = { "popular": "6d0ebec95b0846aeb8ffe8f94eb268bd", "article": "6d0ebec95b0846aeb8ffe8f94eb268bd"}

## Functions
def get_from_file(kind, period):
    ### Returns json File
    filename = "popular-{0}-{1}.json".format(kind, period)
    with open(filename, "r") as jsonfile:
        return json.loads(jsonfile.read())

def article_overview(kind, period):
    ### Returns Titles and Urls of Articles
    data = get_from_file(kind, period)
    titles = []
    urls =[]
    for row in data:
        section = row['section']
        title = row['title']
        titles.append({section: title})
        if row['media']:
            medias = row['media']
            for media in medias:
                metas = media["media-metadata"]
                for meta in metas:
                    if meta["format"] == "Standard Thumbnail":
                        urls.append(meta['url'])
    return (titles, urls)

def query_site(url, target, offset):
    '''
    Query the NY Times API with key and offset
    NYTimes returns 20 articles per request, 
    if you want the next 20, you have to provide the offset parameter

    Returns Json File of Articles
    '''
    if API_KEY["popular"] == "" or API_KEY["article"] == "":
        print("You need to register for NYTimes Developer account to run this program.")
        print("See Intructor notes for information")
        return False
    params = {"api-key": API_KEY[target], "offset": offset}
    r = requests.get(url, params = params)

    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        r.raise_for_status()


def get_popular(url, kind, days, section="all-sections", offset=0):
    '''
    Construct the query according to the requirements of the NY Times site
    Returns the data, or prints an error message if called incorrectly
    '''
    if days not in [1,7,30]:
        print("Time period can be 1,7, 30 days only")
        return False
    if kind not in ["viewed", "shared", "emailed"]:
        print("kind can be only one of viewed/shared/emailed")
        return False

    url += "most{0}/{1}/{2}.json".format(kind, section, days)
    data = query_site(url, "popular", offset)

    return data


def save_file(kind, period):
    '''
    Process all results, by calling the API repeatedly with supplied offset value,
    Combine the data and then write all results in a file.
    '''
    data = get_popular(URL_POPULAR, "viewed", 1)
    num_results = data["num_results"]
    full_data = []
    with codecs.open("popular-{0}-{1}.json".format(kind, period), encoding='utf-8', mode='w') as v:
        for offset in range(0, num_results, 20):        
            data = get_popular(URL_POPULAR, kind, period, offset=offset)
            full_data += data["results"]
        
        v.write(json.dumps(full_data, indent=2))


titles, urls = article_overview("viewed", 1)
print(titles)
print(urls)