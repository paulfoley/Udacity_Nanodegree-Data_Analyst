# Data Extract - Research Articles

In the academic community, especially the medical community, research is paramount. We'll be using a research article from [BioMed Central](https://www.biomedcentral.com/) to parse relevant data from the paper.


## Project Overview

In this project, we're curious who are the authors of the research article? We'll use code to parse the paper, provided by [BioMed Central](https://www.biomedcentral.com/), and get the authors as well as get their email addresses.


## Getting Started

### Prerequisites

You'll need to install:

* [Anaconda](https://www.continuum.io/downloads)
* [Python (Minimum 3)](https://www.continuum.io/blog/developer-blog/python-3-support-anaconda)

### Data Files

* `research_article-example.xml` - An example research paper from [BioMed Central](https://www.biomedcentral.com/)


## Scripts

* `get_authors.py` - This script will output a CSV file of the authors of the academic research paper.

### Functions

* `get_authors(root)` - Parses the xml research paper and finds the authors.

### Outputs:

* `authors.csv` - CSV file of authors who wrote the research paper.


## Authors

* **[Paul Foley](https://github.com/paulfoley)**
* [Udacity](https://www.udacity.com/)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


## Acknowledgments

* [BioMed Central](https://www.biomedcentral.com/)
