# Data Audit - City Data

As a project, to show off data wrangling skills, we'll use the City data provided by [DBpedia](http://wiki.dbpedia.org/) to do some auditing and cleaning.

In the following scripts we'll take in the 'cities.csv' file, and either audit it for accuracy and completeness, or we'll clean the data and re-output the clean data only into a csv file for use later.

## Getting Started

### Prerequisites

You'll need to install:

* [Anaconda](https://www.continuum.io/downloads)
* [Python (Minimum 3)](https://www.continuum.io/blog/developer-blog/python-3-support-anaconda)

### Data Files

* `cities.csv` - City data for auditing


## Scripts

### Exploration

* `get_field_types.py` - Explore the cities.csv data file by getting each fields data types.

### Audit Names

* `audit_name.py` - Script that takes in the name of each area, cleans the name field and outputs a list of all area names.

### Audit Location

* `audit_city_location.py` - Script that goes through the location data and outputs a count of how many cities are missing location data.
* `verify_city_location.py` - To further audit the city location, this script outputs a CSV file of all locations that either have Null values, or have values that aren't verified by a cross check on latitude and longitude. The output data can be used to clean the location data at later time.

### Audit Number of Acres

* `audit_acres.py` - Script that audits the number of acres for each area. Takes in the number of acres for each area and either outputs a float value containing the number of acres or `None` for empty or "Null" values.


### Outputs:

* `field_types.csv` - List of Field Types for each field in the `cities.csv` file
* `area_names.csv` - List of cleaned area Names
* `locations_to_check.csv` - List of areas with locations that need to be updated
* `area_land.csv` - List of areas with the number of acres they have


## Authors

* **Paul Foley** - [paulfoley](https://github.com/paulfoley)

See also the list of [contributors](https://github.com/paulfoley/data-analyst/tree/master/City_Data-Audit) who participated in this project.


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


## Acknowledgments

* [DBpedia](http://wiki.dbpedia.org/)
* [Udacity](https://www.udacity.com/)
