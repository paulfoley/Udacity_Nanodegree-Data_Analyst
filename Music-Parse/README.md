# Data Extract - Music Data

Music is amazing. With the rise of the internet, there are a ton of sites that have an encyclopedia worth of music data, two of which are [MusicBrainz](https://musicbrainz.org/) and [AudioScrobbler](http://www.audioscrobbler.net/).

These sites also have API's which allows us to conenct and extract their information. 


## Project Overview

We'll be using the [MusicBrainz](https://musicbrainz.org/) and [AudioScrobbler](http://www.audioscrobbler.net/) API's to get info about our favorite artists and their albulms.

### MusicBrainz

We'll be using the [MusicBrainz](https://musicbrainz.org/) to pull in data about an artist and output a .csv file of all their albulm titles.

### AudioScrobbler

We'll be using the [AudioScrobbler](http://www.audioscrobbler.net/) to pull in data about an albulm and output the albulm description to a .txt file.


## Getting Started

### Prerequisites

You'll need to install:

* [Anaconda](https://www.continuum.io/downloads)
* [Python (Minimum 3)](https://www.continuum.io/blog/developer-blog/python-3-support-anaconda)


## Scripts

* `music_brainz_api.py` - Pulls in data about a musical artist from the [MusicBrainz](https://musicbrainz.org/) API and outputs a .csv file of their albulms.
* `audio_scrobbler_api.py` - Pulls in data from the [AudioScrobbler](http://www.audioscrobbler.net/) about a specific albulm and outputs albulm info in a .txt file.

### Outputs:

* `%_titles.csv` - A .csv file listing all the albulms by a certain artist.
* `%_%_Info.txt` - A .txt file with the albulm information of a certain artist's albulm.


## Authors

* **[Paul Foley](https://github.com/paulfoley)**
* [Udacity](https://www.udacity.com/)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


## Acknowledgments

* [MusicBrainz](https://musicbrainz.org/)
* [AudioScrobbler](http://www.audioscrobbler.net/)
