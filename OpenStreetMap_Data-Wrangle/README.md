# Data Wrangling - OpenStreetMap Data

[OpenStreetMap](https://www.openstreetmap.org) is a map of the world, created by people for free, to use under an open license, and to build amazing projects.

We're going to give back to this open source project [OpenStreetMap](https://www.openstreetmap.org/), by using data munging techniques to clean the data.


## Project Overview

We're going to focus on clearning the [OpenStreetMap Denver/Boulder, CO Area](https://mapzen.com/data/metro-extracts/metro/denver-boulder_colorado/). This data set contains, my hometown of Louisville, CO, which I love. It's a budding community in between Boulder and Denver, which are two cities I've thoroughly enjoyed living in as well. 

In this projce we're going to asses the quality of the data for:

* Validity
* Accuracy
* Completeness
* Consistency
* Uniformity


## Files
### Data Files:

* `Project_Summary.docx` - A Word Doc of Project Findings
* `denver_sample.csv` - CSV file with samples of Denver OSM data
* `denver_sample.osm` - OSM file that is a sample of the much larger Denver OSM data

### File Sizes

* `denver_sample.osm` – 9.2 MB
* `nodes.csv` – 3.5 MB
* `nodes_tags.csv` – 128 KB
* `ways.csv` – 282 KB
* `ways_tags.csv` – 647 KB
* `ways_nodes.csv` – 1.1 MB


## Python Scripts:

* `explore_users.py` - Python script finding out how many users contributed to a particular area
* `number_of_elements.py` - Python script to find the type and number of tags in the OSM file
* `output_csv.py` - Outputs the CSV Files "nodes", "nodes_tags", "ways", "ways_nondes", and "way_tags" to be imported into the database
* `tag_types.py` - Function to identify certain tags and problem characters
* `update_street_names.py` - Audit and update street names


## Instructions to get CSV Files into an SQL database
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


## Explore the OSM Data

After initially downloading the Denver/Boulder OSM file, the OSM file is very large, so the ‘sample_output_osm.py’ script was written to output a sample file of the data that was 1/100th the size. The data output is named `denver_sample.osm`, but to clarify the sample data includes samples from both Boulder, Denver, and the metro areas. The abbreviated file name was chosen for ease of typing.

This project Focuses on the below (all written up in the project summary):

• Understanding the ‘Elements’ in the OSM File
• Understanding the ‘Tags’ in the OSM File
• Exploring and Auditing Street Names
• Exploring and Auditing Postal Codes
• Understanding Users

## Authors

* [**Paul Foley**](https://github.com/paulfoley)
* See also the list of [contributors](https://github.com/paulfoley/data-analyst/tree/master/OpenStreetMap_Data-Wrangle) who participated in this project.


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


## Acknowledgments

* [OpenStreetMap](https://www.openstreetmap.org) is a map of the world, created by people for free, and to use under an open license to build amazing projects.
* [Udacity](https://www.udacity.com/)
