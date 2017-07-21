# Project - DBpedia Auto Data

[DBpedia](http://wiki.dbpedia.org/) is building public data infrastructure for a large, multilingual, semantic knowledge graph! They have a ton of data sets, and as with most data sets, they could use some cleaning.

## Project Overview

To help [DBpedia](http://wiki.dbpedia.org/), we're going to audit one of their data sets for cleanliness.

Specifically, we'll take in the `autos.csv` file and output the already clean data into `autos-valid.csv` and then output data that needs fixing into `FIXME-autos.csv`.

## Getting Started

### Prerequisites

You'll need to install:

* [Anaconda](https://www.continuum.io/downloads)
* [Python (Minimum 3)](https://www.continuum.io/blog/developer-blog/python-3-support-anaconda)

### Data Files

* `autos.csv` - Auto Data for processing


## Script

* `audit_production_start_year.py` - Takes in the `autos.csv` and outputs already valid data into `autos-valid.csv`, the data that needs to be cleaned will go into `FIXME-autos.csv`

### Script Function:

* `process_file(input_file, output_good, output_bad)` - Takes in the auto datas and separates the data into valid and FIXME files.

### Outputs:

* `autos-valid.csv` - Valid Auto Data
* `FIXME-autos.csv` - Data that needs fixing


## Authors

* **[Paul Foley](https://github.com/paulfoley)**
* [Udacity](https://www.udacity.com/)


## License

* <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/"> Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>

<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/">
	<img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" />
</a>


## Acknowledgments

* [DBpedia](http://wiki.dbpedia.org/)
