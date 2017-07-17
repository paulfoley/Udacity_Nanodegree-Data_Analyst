'''
This script will provide a list of titles from a specific artist
By using the the MusicBrainz.com API, querying by artist
and then returning a JSON response with titles by that artist

The output from the script is a csv file of titles by the author
'''

## Imports
import json
import requests
import csv

## MusicBrainz URL
URL = "http://musicbrainz.org/ws/2/artist/"

## Artist For Query (Pick Your Favorite!)
artist = 'Timeflies'

## Query parameters are given to the requests.get function as a dictionary
query_type = {"simple": {}, "atr": {"inc": "aliases+tags+ratings"}, "aliases": {"inc": "aliases"}, "releases": {"inc": "releases"}}

## Functions
def query_site(url, params, uid="", fmt="json"):
    ### Make queries to the MusicBrainz API, a json object will be returned
    params["fmt"] = fmt
    request = requests.get(url + uid, params = params)

    if request.status_code == requests.codes.ok:
        return request.json()
    else:
        request.raise_for_status()

def query_by_name(url, params, name):
    ### This adds an artist name to the query parameters before making an API call
    params["query"] = "artist:" + name
    return query_site(url, params)

def get_titles(artistname):
    ### Outputs a CSV with a list of Album Titles for specific Artist
    
    #### Make the API call
    json = query_by_name(URL, query_type["simple"], artistname)
    
    #### Get Artist ID 
    for artist in json["artists"]:
        if artist['name'] == artistname:
            artist_id = artist["id"]
    
    #### Get Releases by Artist
    data = query_site(URL, query_type["releases"], artist_id)
    releases = data["releases"]

    #### Get Titles
    titles = []
    for release in releases:
        if release["title"] not in titles:
            titles.append(release['title'])
    
    #### Output Titles to CSV
    filename = artistname + '_titles.csv'
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for title in titles:
            writer.writerow(title)


get_titles(artist)
