"""
Check the "productionStartYear" of the Autos datafile for valid values.

The script does the following:
- Check if the field "productionStartYear" contains a year
- Check if the year is in range 1886-2014
- Convert the value of the field to be just a year (not full datetime)
- The rest of the fields and values should stay the same
- If the value of the field is a valid year in the range as described above,
  write that line to the output_good file
- If the value of the field is not a valid year as described above, 
  write that line to the output_bad file
- Discard rows (neither write to good nor bad) if the URI is not from dbpedia.org
- You should use the provided way of reading and writing data (DictReader and DictWriter)
  They will take care of dealing with the header.
"""

## Import CSV
import csv

## Function
def process_file(input_file, output_good, output_bad):
    # Takes in a the Autos CSV file and outputs good data and FIXME data
    data_bad = []
    data_good = []
    data_extra = []
    with open(input_file, "r") as file:
        reader = csv.DictReader(file)
        header = reader.fieldnames
        for row in reader:
            if 'dbpedia' not in row['URI']:
                data_extra.append(row)
            year = row['productionStartYear'][:4]
            try: 
                year = int(year)
                row['productionStartYear'] = year
                if year >= 1886 and year <= 2014:
                    data_good.append(row)
                else:
                    data_bad.append(row)
            except ValueError:
                if year == 'NULL':
                    data_bad.append(row)

    # Output Good Data
    with open(output_good, "w") as good:
        writer = csv.DictWriter(good, delimiter=",", fieldnames= header)
        writer.writeheader()
        for data_row in data_good:
            writer.writerow(data_row)

    # Output Bad Data
    with open(output_bad, "w") as bad:
        writer = csv.DictWriter(bad, delimiter=",", fieldnames= header)
        writer.writeheader()
        for data_row in data_bad:
            writer.writerow(data_row)

## Run
process_file('autos.csv', 'autos-valid.csv', 'FIXME-autos.csv')
