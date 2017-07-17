'''
Script to get the album information from the AudioScrobbler API

Inputs:
- Artist
- Albulm

Output:
- Album Information
'''

## Import JSON and Requests
import json
import requests

## Artist and Album to get data for:
artist = 'Avicii'
album = 'Stories'

# API Connection
url = 'http://ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key=277313dd0875f33f9b35a7c61030eee5&artist='+ artist +'&album=' + album +'&format=json'
data = requests.get(url).text
data = json.loads(data)

filename = artist + '_' + album + '_Info.txt'
# Output Albulm Content
with open(filename, 'w') as txtfile:
	txtfile.write('Album Information:')
	txtfile.write(data['album']['wiki']['content'])
