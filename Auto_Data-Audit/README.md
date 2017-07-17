# Data Audit - Auto Data

It's often important to clean data before use. In this project we'll use the Auto data provided by [DBpedia](http://wiki.dbpedia.org/) and audit the data for cleanliness. 

We'll take in the 'autos.csv' file and output the already clean data into `autos-valid.csv` and then output data that needs fixing into `FIXME-autos.csv`.

This project is just an example of how to audit data.

## Getting Started

### Prerequisites

You'll need to install:

* [Anaconda](https://www.continuum.io/downloads)
* [Python (Minimum 3)](https://www.continuum.io/blog/developer-blog/python-3-support-anaconda)

### Data Files

* `autos.csv` - Auto Data for processing


## Running Data Audit

The script `audit_production_start_year.py` will take in the `autos.csv` and output already valid data into `autos-valid.csv`, the data that needs to be cleaned will go into 'FIXME-autos.csv'

### Script Function:

* `process_file(input_file, output_good, output_bad)` - Takes in the auto datas and separates the data into valid and FIXME files.

### Outputs:

* `autos-valid.csv` - Valid Auto Data
* `FIXME-autos.csv` - Data that needs fixing


## Authors

* **[Paul Foley](https://github.com/paulfoley)**
* [Udacity](https://www.udacity.com/)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


## Acknowledgments

* [DBpedia](http://wiki.dbpedia.org/)
