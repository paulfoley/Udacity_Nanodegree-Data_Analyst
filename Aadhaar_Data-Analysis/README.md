# Data Analysis - Aadhaar Enrolment

[Aadhaar Enrolment](https://uidai.gov.in/enrolment-update/aadhaar-enrolment.html) is an initiative by the India Government to better register their citizens. As India has over a billion people, keeping track of citizens is a major problem.


## Getting Started

### Prerequisites
You'll need to install:

* [Anaconda](https://www.continuum.io/downloads)
* [Python (Minimum 3)](https://www.continuum.io/blog/developer-blog/python-3-support-anaconda)
* [Pandas](https://anaconda.org/anaconda/pandas)
* [PandaSQL](https://anaconda.org/anaconda/pandasql)

### Data Files

* `aadhaar_data.csv` - Aadhaar Data Set


## Running the Script
In this script we'll use pandas and pandasql to analyze the Aadhaar data using SQL queries.

* `aadhaar-analysis.py` - Has functions to easily sort and filter the Aadhaar data

### Functions:

* `describe(aadhaar_data)` - Describes the Data Set
* `select_first_50(aadhaar_data)` - Gives us a sample of 50 id's understand the data better
* `select_state(aadhaar_data)` - A function that will allow us to query by state
* `select_district(aadhaar_data)` - A function that will allow us to query by district
* `select_gender(aadhaar_data)` - A function that will allow us to query by gender


## Authors

* [**Paul Foley**](https://github.com/paulfoley)
* See also the list of [contributors](https://github.com/paulfoley/data-analyst/tree/master/Aadhaar_Data-Analysis) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* [Unique Identification Authority of India](https://uidai.gov.in/)
* [Udacity](https://www.udacity.com/)
