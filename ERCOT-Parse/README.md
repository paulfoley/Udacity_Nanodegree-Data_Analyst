# Data Audit - ERCOT Data

Electric Reliability Council of Texas [ERCOT](http://www.ercot.com/mktinfo/data_agg) provides an open source version of their data.

## Project Overview

We'll be using 2013 [ERCOT](http://www.ercot.com/mktinfo/data_agg) hourly load data to find the Maximum, Minimum, and Average loads of energy output in each station they have around the country.

## Getting Started

### Prerequisites

You'll need to install:

* [Anaconda](https://www.continuum.io/downloads)
* [Python (Minimum 3)](https://www.continuum.io/blog/developer-blog/python-3-support-anaconda)

### Data Files

* `2013_ERCOT_hourly_Load_data.xls` - [ERCOT](http://www.ercot.com/mktinfo/data_agg) hourly load data, that provides energy data for various stations across the country.


## Scripts

* `get_min_max_average.py` - Get the Minimum, Maximum, and Average hourly load data for each [ERCOT](http://www.ercot.com/mktinfo/data_agg) energy station

### Functions

* `parse_file(datafile)` - Parses the xls file and finds the minimum, maximum, and average hourly energy loads for each ERCO station.

* `save_file(data, filename)` - Outputs the minimum, maximum, and average hourly energy load values in a CSV.

### Outputs:

* `2013_max_min_loads.csv` - CSV file of minimum, maximum, and average hourly energy load values for ERCOT stations across the country.


## Authors

* **Paul Foley** - [paulfoley](https://github.com/paulfoley)

* Other [contributors](https://github.com/paulfoley/data-analyst/tree/master/ERCOT-Parse) who participated in this project.


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


## Acknowledgments

* [ERCOT](http://www.ercot.com/mktinfo/data_agg)
* [Udacity](https://www.udacity.com/)
