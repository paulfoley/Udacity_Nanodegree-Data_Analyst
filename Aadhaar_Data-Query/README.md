# Project - Aadhaar Enrolment

[Aadhaar Enrolment](https://uidai.gov.in/enrolment-update/aadhaar-enrolment.html) is an initiative by the India Government to register their citizens. As India has over a billion people, keeping track of residents is a major problem.

## Project Overview

In this project we're going to create a python script that can perform queries on the [Aadhaar Enrolment](https://uidai.gov.in/enrolment-update/aadhaar-enrolment.html) data set, such as:

* Query residents By State
* Query residents by District
* Query residents by Gender


## Getting Started

### Prerequisites
You'll need to install:

* [Anaconda](https://www.continuum.io/downloads)
* [Python (Minimum 3)](https://www.continuum.io/blog/developer-blog/python-3-support-anaconda)
* [Pandas](https://anaconda.org/anaconda/pandas)
* [PandaSQL](https://anaconda.org/anaconda/pandasql)

### Data Files

* `aadhaar_data.csv` - Aadhaar Data Set


## Script

* `aadhaar-analysis.py` - Python script with functions to easily sort and filter the Aadhaar data.

### Functions:

* `describe(aadhaar_data)` - Describes the Data Set
* `select_first_50(aadhaar_data)` - Gives us a sample of 50 id's understand the data better
* `select_state(aadhaar_data)` - A function that will allow us to query by state
* `select_district(aadhaar_data)` - A function that will allow us to query by district
* `select_gender(aadhaar_data)` - A function that will allow us to query by gender


## Authors

* **[Paul Foley](https://github.com/paulfoley)**
* [Udacity](https://www.udacity.com/)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


## Acknowledgments

* [Unique Identification Authority of India](https://uidai.gov.in/)
