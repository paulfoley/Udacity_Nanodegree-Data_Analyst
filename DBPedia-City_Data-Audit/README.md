# Project - DBpedia City Data

[DBpedia](http://wiki.dbpedia.org/) is building public data infrastructure for a large, multilingual, semantic knowledge graph! They have a ton of data sets, and as with most data sets, they could use some cleaning.


## Project Overview

To help [DBpedia](http://wiki.dbpedia.org/), we're going to audit one of their data sets for cleanliness.

Specifically, we'll look at the `cities.csv` file and audit the data for accuracy and completeness. After fixing the data we'll re-output the clean data into a new CSV file.


## Getting Started

### Prerequisites

You'll need to install:

* [Anaconda](https://www.continuum.io/downloads)
* [Python (Minimum 3)](https://www.continuum.io/blog/developer-blog/python-3-support-anaconda)

### Data Files

* `cities.csv` - [DBpedia](http://wiki.dbpedia.org/) city data for auditing.


## Scripts

### Exploration

* `get_field_types.py` - Explore the cities.csv data file by getting each fields data types.

### Audit City Names

* `audit_name.py` - Script that takes in the name of each area, cleans the name field and outputs a list of all area names.

### Audit City Location

* `audit_city_location.py` - Script that goes through the location data and outputs a count of how many cities are missing location data.
* `verify_city_location.py` - To further audit the city location, this script outputs a CSV file of all locations that either have Null values, or have values that aren't verified by a cross check on latitude and longitude. The output data can be used to clean the location data at later time.

### Audit Number of Acres in Area

* `audit_acres.py` - Script that audits the number of acres for each area. Takes in the number of acres for each area and either outputs a float value containing the number of acres or `None` for empty or "Null" values.

### Outputs:

* `field_types.csv` - List of Field Types for each field in the `cities.csv` file
* `area_names.csv` - List of cleaned area Names
* `locations_to_check.csv` - List of areas with locations that need to be updated
* `area_land.csv` - List of areas with the number of acres they have


## Authors

* **[Paul Foley](https://github.com/paulfoley)**
* [Udacity](https://www.udacity.com/)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


## Acknowledgments

* [DBpedia](http://wiki.dbpedia.org/)
