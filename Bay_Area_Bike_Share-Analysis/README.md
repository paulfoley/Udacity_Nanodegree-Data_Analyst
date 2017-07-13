# Data Analysis - Bay Area Bike Share Data.

## Introduction
Bay Area Bike Share is a company that provides on-demand bike rentals for customers in San Francisco, Redwood City, Palo Alto, Mountain View, and San Jose. Users can unlock bikes from a variety of stations throughout each city, and return them to any station within the same city. Users pay for the service either through a yearly subscription or by purchasing 3-day or 24-hour passes. Users can make an unlimited number of trips, with trips under thirty minutes in length having no additional charge; longer trips will incur overtime fees.

In this project, we will perform data wrangling as well as an exploratory analysis on the Bay Area Bike Share data.


## Questions

Before we even start looking at data, let's think of some questions that we want to understand about the bike share users.

### Question 1

Currently, there is an overage fee for rides longer then 30 minutes. Is this optimal though? What does the typical ride time look like? It could benefit Bay Area Bike Share to change their overage fees based on the typical ride of a user.

* Are there any usage trends in the data for length of ride times?

### Question 2

Right now packages are broken out into yearly, 24-hour, as well as 3-day passes. Is this optimal though? In order to improve the bike service pricing package let's look at usage trends to see if there are peak days where the bike share is being used more often.

* Are there any usage trends in the data for specific days of the week where bike share is utilized the most?

### Question 3

It's also important for us to understand how the bike share is being used in various cities. Let's explore the data and see if there are certain cities where the bikes are being used more often. From understanding this we can add more bikes in certain cities as well as change pricing based on demand.

* Are there specific cities where bike share is used more then other cities?


## Files:
* Bay_Area_Bike_Share-Analysis.ipynb - Main project file, an IPython Notbook that contains the analysis for the project

* babs_datacheck.py; babs_visualizations.py - Supplemental scripts for checking data wrangling, reporting of basic statistics, and creation of exploratory bar charts and histograms.

Data is split among twelve other files, organized into three sets of four files
each. Prefixing each set is one of three datestamps, showing the end month for
each data collection period (201402, 201408, 201508). Suffixes for each file
indicate contents:


* \*\_README.txt - Information about contents of data files.

* \*\_station_data.csv - Basic information about station locations and
capacities.

* \*\_trip_data.csv - Information about each trip taken using the bike share
system.

* \*\_weather_data.csv - Weather information by day for one station in each
city in the bike share program.


## Getting Started
Here is a walk through of the steps necessary to get Python up and running on your machine. You'll also get up and running with the Jupyter notebook, which you'll use to complete the project. Below are quick instructions for installing Anaconda, Python, and Jupyter notebooks.

### Installing Python
For both this project you’ll need to install Python on your computer.

We’ll do so using an Anaconda distribution, which comes with many popular Python packages for data analysis, as well as Jupyter Notebook. Some of these packages can be difficult to install otherwise, so we highly recommend installing Anaconda to make life easier. 

To do so, complete the following:
* Navigate to http://continuum.io/downloads in your browser.
* Install Python 2.7 using the Anaconda distribution, which comes with Jupyter.
* On a PC, click the Windows icon and select "Windows 64-Bit Python 2.7 Graphical Installer". You can also select the 32-bit installer if you have a 32-bit machine. Then run the installer and follow the instructions on the screen.
* On Mac or Linux, follow the same process but select the appropriate installer for your platform.

### Opening the Jupyter Notebook
As mentioned earlier, the project can be read using a Jupyter Notebook. There's also an HTML version.

* Download the Jupyter Notebook
* Open your Command Prompt (PC) or terminal (Mac or Linux).
* On a PC click the Start button and search for "Command Prompt".
* On a Mac type command + spacebar. Then, type "terminal" in the Spotlight Search. You can also search for "terminal" in finder.
* Navigate to the directory where you downloaded the Jupyter notebook file.
* On a PC you might type: cd C:\Users\username\Downloads\, replacing your username. Learn more about basic terminal commands.
* On Mac or Linux you might type: cd ~/Downloads. Learn more about basic terminal commands.
* Run the command jupyter notebook Bay_Area_Bike_Share-Analysis.ipynb in your terminal.

The Jupyter Notebook has all project information.

### Special Note
If you try running a code block and get an error message like no module named seaborn, then your distribution of Anaconda may be missing a package used in the project. That's okay – there's an easy way that you can install this package. In the Command Prompt or terminal, run the command conda install seaborn. This should add the package. If this doesn't work, take a look at Google for additional tips!
