# Project - Transtats API

The [United State Bureau of Transportation Statistics](https://www.transtats.bts.gov/) provides an API that developers can use to query flight data for their projects.


## Project Overview

In this project we want get a list of flights going from one airport to another. We'll use the [United State Bureau of Transportation Statistics](https://www.transtats.bts.gov/) API to receive flight data, parse the data, and then get a list of flights that go from one airport to another.


## Getting Started

### Prerequisites

You'll need to install:

* [Anaconda](https://www.continuum.io/downloads)
* [Python (Minimum 3)](https://www.continuum.io/blog/developer-blog/python-3-support-anaconda)
* [BeautifulSoup](https://anaconda.org/anaconda/beautiful-soup)
* [Requests](https://anaconda.org/anaconda/requests)

### Data Files

* `airport_and_carrier.html` - HTML File of Airports and Carriers
* `fl-atl.html` - HTML file of flights from Florida to Atlanta
* `virgin_and_logan_airport.html` - HTML file of Virgin flights from Logan Airport


## Scripts

* `airports.py` - Provides a list of aiport codes available through the API
* `carriers.py` - Provides a list of airline carrier codes available through the API
* `transtats_api.py` - Returns an html file of all flights out an aiport on a specific carrier
* `flights.py` - Outputs a CSV of flights from one aiport to another

### Output Files:

* `airports.csv` - A CSV file of Airports
* `carriers.csv` - A CSV file of Carriers
* `view_state.txt` - API field needed to query transtats API
* `event_validation.txt` - API field needed to query transtats API
* `fights.csv` - A CSV file of flights from one airport to another


## Authors

* [**Paul Foley**](https://github.com/paulfoley)
* [Udacity](https://www.udacity.com/)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


## Acknowledgments

* [United State Bureau of Transportation Statistics](https://www.transtats.bts.gov/)
