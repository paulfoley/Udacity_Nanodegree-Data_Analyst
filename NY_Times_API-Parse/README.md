# Project - NY Times API

The [The New York Times](https://developer.nytimes.com/) is a source of news and information. But now it's a source of data, too. [The New York Times](https://developer.nytimes.com/), as well as other publishers, provide API's to their site to allow developers to extract articles from their database.


## Project Overview

We're going to use [The New York Times](https://developer.nytimes.com/) API to get the top technology stories.

Specifially we'll focus on getting:

* The titles of the top technology stories organized by section
* The url's of the top technology stories in list form


## Getting Started

### Prerequisites

You'll need to install:

* [Anaconda](https://www.continuum.io/downloads)
* [Python (Minimum 3)](https://www.continuum.io/blog/developer-blog/python-3-support-anaconda)
* [requests](https://anaconda.org/anaconda/requests)


## Scripts

* `ny_times_api.py` - Pulls in data about top technology stories from the [The New York Times](https://developer.nytimes.com/), outputs the story titles and urls.

### Outputs:

* `topstories_technology.json` - JSON file of the top technology stories on [The New York Times](https://developer.nytimes.com/).
* `article_titles.csv` - CSV file of the top technology story titles organized by section.
* `article_urls.csv` - CSV file of the top technology story url's.


## Authors

* **[Paul Foley](https://github.com/paulfoley)**
* [Udacity](https://www.udacity.com/)


## License

* <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/"> Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>

<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/">
	<img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" />
</a>


## Acknowledgments

* [The New York Times](https://developer.nytimes.com/)
