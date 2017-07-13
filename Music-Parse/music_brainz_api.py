# Connect to the MusicBrainz.com API and gets a JSON response

# Import json and requests
import json
import requests

# MusicBrainz URL
URL = "http://musicbrainz.org/ws/2/artist/"

# Query parameters are given to the requests.get function as a dictionary
query_type = {"simple": {}, "atr": {"inc": "aliases+tags+ratings"}, "aliases": {"inc": "aliases"}, "releases": {"inc": "releases"}}

# Functions
def query_site(url, params, uid="", fmt="json"):
    # Make queries to the MusicBrainz API, a json object will be returned
    params["fmt"] = fmt
    request = requests.get(url + uid, params = params)

    if request.status_code == requests.codes.ok:
        return request.json()
    else:
        request.raise_for_status()

def query_by_name(url, params, name):
    # This adds an artist name to the query parameters before making an API call
    params["query"] = "artist:" + name
    return query_site(url, params)

def pretty_print(data, indent=4):
    #Formats the output to be "prettier"
    if type(data) == dict:
        print (json.dumps(data, indent = indent, sort_keys= True))
    else:
        print(data)

def get_one_direction():
    # Makes an API Call
    results = query_by_name(URL, query_type["simple"], "One Direction")
    
    # Print One Direction
    pretty_print(results)
    artist_id = results["artists"][1]["id"]
    print ("\nARTIST:")
    pretty_print(results["artists"][1])
    artist_data = query_site(URL, query_type["releases"], artist_id)
    releases = artist_data["releases"]
    print ("\nONE RELEASE:")
    pretty_print(releases[0], indent = 2)
    release_titles = [r["title"] for r in releases]
    print ("\nALL TITLES:")
    for t in release_titles:
        print (t)

def get_david_guetta():
    # Makes an API Call
    results = query_by_name(URL, query_type["simple"], "David Guetta")
    
    # Prints Number of Artists Named David Guetta
    count = 0
    for artist in results['artists']:
        if artist['name'] == "David Guetta":
            count += 1

    print("\n Number of Artists named David Guetta")
    print(count)

def get_queen():
    # Makes an API Call
    results = query_by_name(URL, query_type["simple"], "Queen")
    
    # Prints Artists Named Queen
    print("\n Artists Named Queen")
    for artist in results['artists']:
        if artist['name'] == "Queen":
                pretty_print(artist)

get_one_direction()
get_david_guetta()
get_queen()
