# Project - New York City Subway Ridership Analysis

The Metropolitan Transportation Authority [MTA](http://web.mta.info/developers/) provides transportation data, free, to the public so they can build better transportation applications.


## Project Overview

In this project we're interested in analyzing the New York city subway data to derive insights, particularly how weather is going to effect subway ridership.


## Getting Started

### Prerequisites

You'll need to install:

* [Anaconda](https://www.continuum.io/downloads)
* [Python (Minimum 3)](https://www.continuum.io/blog/developer-blog/python-3-support-anaconda)
* [pandaSQL](https://anaconda.org/anaconda/pandasql)

### Data Files

* `turnstile.txt` - [MTA](http://web.mta.info/developers/) New York city subway ridership data.
* `turnstile_updated.txt` - [MTA](http://web.mta.info/developers/) New York city subway ridership data has been cleaned to contain all data in one row for easier analysis.
* `turnstile_data_master_with_weather.csv` - Turnstile data that has been combined with weather data, this is the master file that will allow us to derive insights into how weather effects ridership.

#### Turnstile and Weather Variables

* `UNIT` - Remote unit that collects turnstile information. Can collect from multiple banks of turnstiles. Large subway stations can have more than one unit.
* `DATEn` - Date in “yyyymmdd” (20110521) format.
* `TIMEn` - Time in “hh:mm:ss” (08:05:02) format.
* `ENTRIESn` - Raw reading of cummulative turnstile entries from the remote unit. Occasionally resets to 0.
* `EXITSn` - Raw reading of cummulative turnstile exits from the remote unit. Occasionally resets to 0.
* `ENTRIESn_hourly` - Difference in ENTRIES from the previous REGULAR reading.
* `EXITSn_hourly` - Difference in EXITS from the previous REGULAR reading.
* `datetime` - Date and time in “yyyymmdd hh:mm:ss” format (20110501 00:00:00). Can be parsed into a Pandas datetime object without modifications.
* `hour` - Hour of the timestamp from TIMEn. Truncated rather than rounded. 
* `day_week` - Integer (0 6 Mon Sun) corresponding to the day of the week.
* `weekday` - Indicator (0 or 1) if the date is a weekday (Mon Fri).
* `station` - Subway station corresponding to the remote unit.
* `latitude` - Latitude of the subway station corresponding to the remote unit.
* `longitude` - Longitude of the subway station corresponding to the remote unit.
* `conds` - Categorical variable of the weather conditions (Clear, Cloudy etc.) for the time and location.
* `fog` - Indicator (0 or 1) if there was fog at the time and location.
* `precipi` - Precipitation in inches at the time and location.
* `pressurei` - Barometric pressure in inches Hg at the time and location.
* `rain` - Indicator (0 or 1) if rain occurred within the calendar day at the location.
* `tempi` - Temperature in ℉ at the time and location.
* `wspdi` - Wind speed in mph at the time and location.
* `meanprecipi` - Daily average of precipi for the location.
* `meanpressurei` - Daily average of pressurei for the location.
* `meantempi` - Daily average of tempi for the location.
* `meanwspdi` - Daily average of wspdi for the location.
* `weather_lat` - Latitude of the weather station the weather data is from.
* `weather_lon` - Longitude of the weather station the weather data is from.


## Scripts

### Clean Data

* `turnstile_update.py` - Cleans the `turnstile.txt` data and puts all relevant turnstile in data in their respective rows. This cleaning step is so we can use the data for later scripts.

#### Output:

* `turnstile_updated.txt` - [MTA](http://web.mta.info/developers/) New York city subway ridership data has been cleaned to contain all data in one row for easier analysis.

### Explore Data

* `get_turnstile_data.py` - Returns a CSV file of the data while adding in hourly exits, hourly entries, and filtering by regular data. This allows us to get ridership data and features that we will use in the predictions and plot script.

#### Output:

* `turnstile_regular.csv` - CSV file of New York City ridership with the addtion of hourly entries, hourly exits, and filtered by regular. This CSV file will be combined with weather data and then we'll use the plots and predictions scrip to derive insights.


### Predict using Data

* `nyc_subway_ridership-analysis.py` - Uses turnstile data combined with weather data to predict subway ridership in New York city.

### Outputs:

* `TBC`


## Authors

* **[Paul Foley](https://github.com/paulfoley)**
* [Udacity](https://www.udacity.com/)


## License

* <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/"> Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>

<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/">
	<img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" />
</a>


## Acknowledgments

* [Metropolitan Transportation Authority](http://web.mta.info/developers/)
