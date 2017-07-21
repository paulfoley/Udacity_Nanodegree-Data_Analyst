# Project - Music API's

Music is amazing. With the rise of the internet, there are a ton of sites that have an encyclopedia worth of music data, two of which are [MusicBrainz](https://musicbrainz.org/) and [AudioScrobbler](http://www.audioscrobbler.net/).

These sites also have API's which allow us to connect and extract their music data. 


## Project Overview

In this project, we'll be using the [MusicBrainz](https://musicbrainz.org/) and [AudioScrobbler](http://www.audioscrobbler.net/) API's to get info about our favorite artists and their albums.

### MusicBrainz

We'll be using the [MusicBrainz](https://musicbrainz.org/) to pull in data about an artist and output a .csv file of all their album titles.

### AudioScrobbler

We'll be using the [AudioScrobbler](http://www.audioscrobbler.net/) to pull in data about an album and output the album description to a .txt file.


## Getting Started

### Prerequisites

You'll need to install:

* [Anaconda](https://www.continuum.io/downloads)
* [Python (Minimum 3)](https://www.continuum.io/blog/developer-blog/python-3-support-anaconda)


## Scripts

* `music_brainz_api.py` - Pulls in data about a musical artist from the [MusicBrainz](https://musicbrainz.org/) API and outputs a .csv file of their albums.
* `audio_scrobbler_api.py` - Pulls in data from the [AudioScrobbler](http://www.audioscrobbler.net/) about a specific album and outputs album info in a .txt file.

### Outputs:

* `%_titles.csv` - A .csv file listing all the albums by a certain artist.
* `%_%_Info.txt` - A .txt file with the album information of a certain artist's album.


## Authors

* **[Paul Foley](https://github.com/paulfoley)**
* [Udacity](https://www.udacity.com/)


## License

* <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/"> Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>

<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/">
	<img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" />
</a>


## Acknowledgments

* [MusicBrainz](https://musicbrainz.org/)
* [AudioScrobbler](http://www.audioscrobbler.net/)
