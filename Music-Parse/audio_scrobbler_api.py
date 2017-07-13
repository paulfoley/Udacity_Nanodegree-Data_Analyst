# Audio Scrobbler API Connect

# Import JSON and Requests
import json
import requests

# API Connection
url = 'http://ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key=277313dd0875f33f9b35a7c61030eee5&artist=Cher&album=Believe&format=json'
data = requests.get(url).text
data = json.loads(data)

# Output Type of Data
print(type(data))

# Output Albulm Content
print(data['album']['wiki']['content'])

# Output First Artist
artist = data['topartists']['artist'][0]['name']
print(artist)

# Output Artists
artists = data['artists']['artist']
for artist in artists:
	print(artist['name'] + ": " + artist['playcount'])