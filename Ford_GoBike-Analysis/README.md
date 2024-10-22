# Project - Ford GoBike Data

[Ford GoBike](https://www.fordgobike.com/) is a company that provides on-demand bike rentals for customers in San Francisco, Redwood City, Palo Alto, Mountain View, and San Jose. Users can unlock bikes from a variety of stations throughout each city, and return them to any station within the same city. Users pay for the service either through a yearly subscription or by purchasing 3-day or 24-hour passes. Users can make an unlimited number of trips, with trips under thirty minutes in length having no additional charge; longer trips will incur overtime fees.

## Project Overview

In this project, we will analyze the [Ford GoBike](https://www.fordgobike.com/) data to answer specific questions (see below) about their pricing model.

### Areas of Analysis

#### Analysis 1

Currently, there is an overage fee for rides longer then 30 minutes. Is this optimal though? What does the typical bike ride time look like? It could benefit FordGo to change their overage fees based on the typical ride of a user.

* Are there any usage trends in the data for length of ride times?

#### Analysis 2

Right now packages are broken out into yearly, 24-hour, as well as 3-day passes. Is this optimal though? In order to improve the bike service pricing package let's look at usage trends to see if there are peak days where the bike share is being used more often.

* Are there any usage trends in the data for specific days of the week where bike share is utilized the most?

#### Analysis 3

It's also important for us to understand how the bike share is being used in various cities. Let's explore the data and see if there are certain cities where the bikes are being used more often. From understanding this we can add more bikes in certain cities as well as change pricing based on demand.

* Are there specific cities where the bike share is used more then other cities?


## Getting Started

### Prerequisites

You'll need to install:

* [Anaconda](https://www.continuum.io/downloads)
* [Python (Minimum 3)](https://www.continuum.io/blog/developer-blog/python-3-support-anaconda)
* [Pandas](https://anaconda.org/anaconda/pandas)
* [Numpy](https://anaconda.org/anaconda/numpy)
* [Matplotlib](https://anaconda.org/anaconda/matplotlib)

### Data Files

Data is split among twelve files, organized into three sets of four files
each. Prefixing each set is one of three datestamps, showing the end month for
each data collection period (201402, 201408, 201508). Suffixes for each file
indicate contents:

* `\*\_README.txt` - Information about contents of data files.
* `\*\_station_data.csv` - Basic information about station locations and
capacities.
* `\*\_trip_data.csv` - Information about each trip taken using the bike share
system.
* `\*\_weather_data.csv` - Weather information by day for one station in each
city in the bike share program.


## Python Notebook and Scripts

* `Ford_GoBike-Analysis.ipynb` - Main project file, an IPython Notbook that contains the analysis for the project.

* `datacheck.py`; `visualizations.py` - Additional scripts for checking data wrangling, reporting of basic statistics, and creation of exploratory bar charts and histograms.

### Opening the Jupyter Notebook

The project `Ford_GoBike-Analysis.ipynb` can be read using a Jupyter Notebook. There's also an HTML version `Ford_GoBike-Analysis.html` included for easier viewability.

* Open your Command Prompt (PC) or terminal (Mac or Linux).
* On a PC click the Start button and search for "Command Prompt".
* On a Mac type command + spacebar. Then, type "terminal" in the Spotlight Search. You can also search for "terminal" in finder.
* Navigate to the directory where you downloaded the Jupyter notebook file.
* On a PC you might type: cd C:\Users\username\Downloads\, replacing your username. Learn more about basic terminal commands.
* On Mac or Linux you might type: cd ~/Downloads.
* Run the command `jupyter notebook Ford_GoBike-Analysis.ipynb` in your terminal.

#### Special Note

If you try running a code block and get an error message like 'no module named matplotlib', then your distribution of Anaconda may be missing a package used in the project. That's okay – there's an easy way that you can install these packages. It's as simple as Googling the library for easy to use guides on installation!


## Authors

* **[Paul Foley](https://github.com/paulfoley)**
* [Udacity](https://www.udacity.com/)


## License

* <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/"> Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>

<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/">
	<img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" />
</a>


## Acknowledgments

* [Ford GoBike](https://www.fordgobike.com/)
