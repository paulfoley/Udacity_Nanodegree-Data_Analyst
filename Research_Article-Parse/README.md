# Project - Research Articles

In the academic community, especially the medical community, research is paramount. We'll be using a research article from [BioMed Central](https://www.biomedcentral.com/) to parse relevant data from the paper.


## Project Overview

In this project, we're curious as to who are the authors of a research article. We'll use code to parse the paper, provided by [BioMed Central](https://www.biomedcentral.com/), and get the authors as well as get their email addresses so we can potentially send them follow up questions.


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

* <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/"> Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>

<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/">
	<img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" />
</a>


## Acknowledgments

* [BioMed Central](https://www.biomedcentral.com/)
