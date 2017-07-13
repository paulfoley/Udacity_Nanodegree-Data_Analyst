# Data Audit - Auto Data

In this project we'll take in the Auto's CSV file, provided by [DBpedia](http://wiki.dbpedia.org/) and audit the data for data that needs be updated. We'll output the data into two files, the good data will go into `autos-valid.csv` and the bad data will be placed in `FIXME-autos.csv`

## Getting Started

### Prerequisites

You'll need to install:

* [Anaconda](https://www.continuum.io/downloads)
* [Python (Minimum 3)](https://www.continuum.io/blog/developer-blog/python-3-support-anaconda)

### Data Files

* `autos.csv` - Auto Data for processing


## Running Data Audit

The `audit_production_start_year.py` will take in the `autos.csv` and output valid data into `autos-valid.csv` and data that needs cleaning into 'FIXME-autos.csv'

### Function:

* `process_file(input_file, output_good, output_bad)` - Takes in the auto datas and separates the data into valid and FIXME files.

### Outputs:

* `autos-valid.csv` - Valid Auto Data
* `FIXME-autos.csv` - Data that needs fixing


## Authors

* **Paul Foley** - [paulfoley](https://github.com/paulfoley)

See also the list of [contributors](https://github.com/paulfoley/data-analyst/tree/master/Auto_Data-Audit) who participated in this project.


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


## Acknowledgments

* [DBpedia](http://wiki.dbpedia.org/)
* [Udacity](https://www.udacity.com/)
