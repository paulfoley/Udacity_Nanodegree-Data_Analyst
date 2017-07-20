# Project - Weather Data

Who doesn't want to know the weather? [Weather Underground](https://www.wunderground.com/) provides weather data for areas across the world.


## Project Overview

In this project we'll be using sample weather data for the month of May from [Weather Underground](https://www.wunderground.com/). We are interested in querying the data to answer various questions. We'll specifically look at:

* Max temperature on foggy and non-foggy days
* Number of rainy days
* Average temperature on the weekends
* Average temperatures on rainy days where the minimum temperature is greater then 55


## Getting Started

### Prerequisites

You'll need to install:

* [Anaconda](https://www.continuum.io/downloads)
* [Python (Minimum 3)](https://www.continuum.io/blog/developer-blog/python-3-support-anaconda)
* [pandas](http://pandas.pydata.org/)
* [pandaSQL](https://pypi.python.org/pypi/pandasql)


### Data Files

* `weather.csv` - [Weather Underground](https://www.wunderground.com/) sample data for the month of May.


## Scripts

* `weather.py` - Takes in the [Weather Underground](https://www.wunderground.com/) data, and uses SQL queries to answer various questions about the weather.

### Functions

* `max_temp_aggregate_by_fog(weather_data)` - Returns Max Temperature when Foggy or Non-Foggy

* `num_rainy_days(weather_data)` - Count the number rainy days.

* `avg_weekend_temperature(weather_data)` - Returns the average temperature on the weekends

* `avg_min_temperature(weather_data)` - Returns the average temperatures on rainy days where the minimum temperature is greater then 55


## Authors

* **[Paul Foley](https://github.com/paulfoley)**
* [Udacity](https://www.udacity.com/)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.


## Acknowledgments

* [Weather Underground](https://www.wunderground.com/)
