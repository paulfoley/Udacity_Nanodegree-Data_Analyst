# Data Wrangling - Airport Data

In this project we will be using the [United State Bureau of Transportation Statistics](https://www.transtats.bts.gov/) API to receive flight data, we'll then parse the data and return flights that go from one airport to another.

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


## Running the Scripts
The following scripts use the [United State Bureau of Transportation Statistics](https://www.transtats.bts.gov/) API for various purposes, each script is described below.

### Scripts:

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
* See also the list of [contributors](https://github.com/paulfoley/data-analyst/tree/master/Airport_Data-Wrangle) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* [United State Bureau of Transportation Statistics](https://www.transtats.bts.gov/)
* [Udacity](https://www.udacity.com/)
