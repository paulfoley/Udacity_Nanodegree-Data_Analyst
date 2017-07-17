# Data Analysis - Lahman Baseball Data

The [Lahman Baseball Dataset](http://www.seanlahman.com/baseball-archive/statistics/) contains complete batting and pitching statistics from 1871 to 2014, plus fielding statistics, standings, team stats, managerial records, post-season data, and more.

We'll use this data to analyze a few questions we have about [Major League Baseball](https://www.mlb.com/) (MLB).


## Questions for Analysis
Below are the questions we are going to answer using the [Lahman Baseball Dataset](http://www.seanlahman.com/baseball-archive/statistics/): 

### Question 1
As a University of Michigan Alumni (Go Blue!) I'm always curious which universities produce top talent. Let's look at which Universities produce the most MLB All-Stars.

* Which University did All Stars attend most?

### Question 2
Sports have been growing as an industry, and the salaries that MLB players seem to get, compared to the general population, are astronomically high. Let's look at how salaries have changed over time.

* How has Total Salary Spend changed each Year? 

### Question 3
What's also interesting, is the best players get paid disportionately high compared to the rest of the normal players. Let's look at the salaries of All-Stars versus the average counterparts.

* What is the mean Salary of All Stars VS. the mean salary of all players in 2016?


## Getting Started

### Prerequisites
You'll need to install:

* [Anaconda](https://www.continuum.io/downloads)
* [Python (Minimum 3)](https://www.continuum.io/blog/developer-blog/python-3-support-anaconda)
* [Pandas](https://anaconda.org/anaconda/pandas)
* [Numpy](https://anaconda.org/anaconda/numpy)
* [Matplotlib](https://anaconda.org/anaconda/matplotlib)


### Data Files
* `Master.csv` - Full Set of Baseball Data
* `AllstarFull.csv` - A CSV file of MLB All-Star Players
* `CollegePlaying.csv` - A CSV file of MLB Players and their Colleges
* `Salaries.csv` - A CSV file of MLB Players and their Salaries
* `Schools.csv` - A CSV file of MLB Players and their School ID's


### Analysis Files

* `Baseball_Data-Analysis.ipynb` - IPython notebook that contains the analysis
* `baseball_data-audit.py` - Audits the baseball data for cleanliness

### Opening the Jupyter Notebook
The project `Baseball_Data-Analysis.ipynb` can be read using a Jupyter Notebook. There's also an HTML version `Baseball_Data-Analysis.html` included for easier viewability.

* Download the `Baseball_Data-Analysis.ipynb`
* Open your Command Prompt (PC) or terminal (Mac or Linux).
* On a PC click the Start button and search for "Command Prompt".
* On a Mac type command + spacebar. Then, type "terminal" in the Spotlight Search. You can also search for "terminal" in finder.
* Navigate to the directory where you downloaded the Jupyter notebook file.
* On a PC you might type: cd C:\Users\username\Downloads\, replacing your username. Learn more about basic terminal commands.
* On Mac or Linux you might type: cd ~/Downloads.
* Run the command `jupyter notebook Baseball_Data-Analysis.ipynb` in your terminal.

The Jupyter Notebook `Baseball_Data-Analysis.ipynb` has all analysis information.

#### Special Note
If you try running a code block in the notebook and get an error message like no module named matplotlib, then your distribution of Anaconda may be missing a package used in the project. That's okay, there's an easy way that you can install these packages. Take a look at Google for easy to use guides on installation!


## Authors

* **[Paul Foley](https://github.com/paulfoley)**
* [Udacity](https://www.udacity.com/)


## Acknowledgments

* [Lahman Baseball Dataset](http://www.seanlahman.com/baseball-archive/statistics/)


## Licenses

Baseball Databank is a compilation of historical baseball data in a convenient, tidy format, distributed under Open Data terms.

This work is licensed under a Creative Commons Attribution-ShareAlike 3.0 Unported License. For details see:
* http://creativecommons.org/licenses/by-sa/3.0/

Person identification and demographics data are provided by [Chadwick Baseball Bureau](http://www.chadwick-bureau.com), from its Register of baseball personnel.

Player performance data for 1871 through 2014 is based on the [Lahman Baseball Database](http://www.seanlahman.com/baseball-archive/statistics/), version 2015-01-24, which is Copyright (C) 1996-2015 by Sean Lahman.
