# Data Analysis - Bay Area Bike Share Data

[Ford GoBike](https://www.fordgobike.com/) is a company that provides on-demand bike rentals for customers in San Francisco, Redwood City, Palo Alto, Mountain View, and San Jose. Users can unlock bikes from a variety of stations throughout each city, and return them to any station within the same city. Users pay for the service either through a yearly subscription or by purchasing 3-day or 24-hour passes. Users can make an unlimited number of trips, with trips under thirty minutes in length having no additional charge; longer trips will incur overtime fees.

In this project, we will analyze the Bay Area Bike Share data to answer specific questions (see below) about their pricing model.


## Questions for Analysis
Below are the questions we are going to answer using the [Ford GoBike](https://www.fordgobike.com/) data set. 

### Question 1

Currently, there is an overage fee for rides longer then 30 minutes. Is this optimal though? What does the typical ride time look like? It could benefit Bay Area Bike Share to change their overage fees based on the typical ride of a user.

* Are there any usage trends in the data for length of ride times?

### Question 2

Right now packages are broken out into yearly, 24-hour, as well as 3-day passes. Is this optimal though? In order to improve the bike service pricing package let's look at usage trends to see if there are peak days where the bike share is being used more often.

* Are there any usage trends in the data for specific days of the week where bike share is utilized the most?

### Question 3

It's also important for us to understand how the bike share is being used in various cities. Let's explore the data and see if there are certain cities where the bikes are being used more often. From understanding this we can add more bikes in certain cities as well as change pricing based on demand.

* Are there specific cities where bike share is used more then other cities?


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

### Analysis Files

* `Bay_Area_Bike_Share-Analysis.ipynb` - Main project file, an IPython Notbook that contains the analysis for the project.

* `babs_datacheck.py`; `babs_visualizations.py` - Additional scripts for checking data wrangling, reporting of basic statistics, and creation of exploratory bar charts and histograms.

### Opening the Jupyter Notebook

The project `Bay_Area_Bike_Share-Analysis.ipynb` can be read using a Jupyter Notebook. There's also an HTML version `Bay_Area_Bike_Share-Analysis.html` included.

* Download the `Bay_Area_Bike_Share-Analysis.ipynb`
* Open your Command Prompt (PC) or terminal (Mac or Linux).
* On a PC click the Start button and search for "Command Prompt".
* On a Mac type command + spacebar. Then, type "terminal" in the Spotlight Search. You can also search for "terminal" in finder.
* Navigate to the directory where you downloaded the Jupyter notebook file.
* On a PC you might type: cd C:\Users\username\Downloads\, replacing your username. Learn more about basic terminal commands.
* On Mac or Linux you might type: cd ~/Downloads.
* Run the command `jupyter notebook Bay_Area_Bike_Share-Analysis.ipynb` in your terminal.

The Jupyter Notebook `Bay_Area_Bike_Share-Analysis.ipynb` has all project information.

#### Special Note

If you try running a code block and get an error message like no module named matplotlib, then your distribution of Anaconda may be missing a package used in the project. That's okay – there's an easy way that you can install these packages. Take a look at Google for easy to use guides on installation!


## Authors

* [**Paul Foley**](https://github.com/paulfoley)
* See also the list of [contributors](https://github.com/paulfoley/data-analyst/tree/master/Bay_Area_Bike_Share-Analysis) who participated in this project.


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


## Acknowledgments

* [Ford GoBike](https://www.fordgobike.com/)
* [Udacity](https://www.udacity.com/)