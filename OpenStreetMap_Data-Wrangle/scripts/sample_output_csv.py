## Takes a large OSM file and outputs a CSV File

# Imports
import xml.etree.ElementTree as ET  # Use cElementTree or lxml if too slow

# Parameter: take every k-th top level element
k = 100

# Function
def get_element(osm_file, tags=('node', 'way', 'relation')):
    # Yield element if it is the right type of tag
    context = iter(ET.iterparse(osm_file, events=('start', 'end')))
    _, root = next(context)
    for event, elem in context:
        if event == 'end' and elem.tag in tags:
            yield elem
            root.clear()


with open("denver_sample.csv", 'wb') as output:
    # Outputs a sample CSV File
    output.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    output.write('<osm>\n  ')

    # Write every kth top level element
    for i, element in enumerate(get_element("denver.osm")):
        if i % k == 0:
            output.write(ET.tostring(element, encoding='utf-8'))

    output.write('</osm>')