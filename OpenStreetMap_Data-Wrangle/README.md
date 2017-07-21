# Project - OpenStreetMap Data

[OpenStreetMap](https://www.openstreetmap.org) is a map of the world, created by people for free, to use under an open license, and to build amazing projects.

We're going to give back to this open source project [OpenStreetMap](https://www.openstreetmap.org/), by using data munging techniques to clean the data.


## Project Overview

We're going to focus on clearning the [OpenStreetMap Denver/Boulder, CO Area](https://mapzen.com/data/metro-extracts/metro/denver-boulder_colorado/). This data set contains, my hometown of Louisville CO, which I love. It's a budding community in between Boulder and Denver, which are two cities I've thoroughly enjoyed living in as well. 

In this project we're going to asses the quality of the data for:

* Validity
* Accuracy
* Completeness
* Consistency
* Uniformity


## Files

### Data Files:

* `denver_sample.csv` - CSV file with samples of Denver OSM data
* `denver_sample.osm` - OSM file that is a sample of the much larger Denver OSM data

#### File Sizes

* `denver_sample.osm` – 9.2 MB
* `nodes.csv` – 3.5 MB
* `nodes_tags.csv` – 128 KB
* `ways.csv` – 282 KB
* `ways_tags.csv` – 647 KB
* `ways_nodes.csv` – 1.1 MB

### OSM Sample File

After initially downloading the [OpenStreetMap Denver/Boulder, CO Area](https://mapzen.com/data/metro-extracts/metro/denver-boulder_colorado/), the OSM file is very large. So the ‘sample_output_osm.py’ script was written to output a sample file of the data that is 1/100th the size. The data output is named `denver_sample.osm`, but to clarify the sample data includes samples from Boulder, Denver, and the metro areas. The abbreviated file name was chosen for ease of typing.

### Instructions to get CSV Files into an SQL Database

1) In your terminal type:

`sqlite3 osm`

will bring you create an sqlite3 database called 'osm'

2) Next type the commands:

```
.mode csv
.import path/nodes.csv nodes
```

This will create a table called nodes

3) To verify the import, type:

`.schema nodes`

4) Repeat steps 2 and 3 for the other csv files (ways, nodes_tags, ways_nodes, and ways_tags)

Make sure to name each table respectively!


## Python Scripts:

* `explore_users.py` - Python script finding out how many users contributed to a particular area
* `number_of_elements.py` - Python script to find the type and number of tags in the OSM file
* `output_csv.py` - Outputs the CSV Files "nodes", "nodes_tags", "ways", "ways_nondes", and "way_tags" to be imported into the database
* `tag_types.py` - Function to identify certain tags and problem characters
* `update_street_names.py` - Audit and update street names

### Explore the OSM Data

This project focuses on the below, all written up in the `Project_Summary.docx`:

* Understanding the `Elements` in the OSM File
* Understanding the `Tags` in the OSM File
* Exploring and Auditing Street Names
* Exploring and Auditing Postal Codes
* Understanding Users


## Authors

* **[Paul Foley](https://github.com/paulfoley)**
* [Udacity](https://www.udacity.com/)


## License

* <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/"> Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>

<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/">
	<img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" />
</a>


## Acknowledgments

* [OpenStreetMap](https://www.openstreetmap.org) is a map of the world, created by people for free, and to use under an open license to build amazing projects.
