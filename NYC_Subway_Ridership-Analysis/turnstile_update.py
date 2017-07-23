'''
    There are numerous data points included in each row 
    of the a MTA Subway turnstile text file. 

    This script will update each row in the text file
    so there is only one entry per row. 

    A few examples below:
    A002,R051,02-00-00,05-28-11,00:00:00,REGULAR,003178521,001100739
    A002,R051,02-00-00,05-28-11,04:00:00,REGULAR,003178541,001100746
    A002,R051,02-00-00,05-28-11,08:00:00,REGULAR,003178559,001100775
'''

## Imports
import csv

## Data
filename = 'turnstile.txt'

## Function
def fix_turnstile_data(filename):
    # Fixes Turnstile txt data so there is only one row per entry
    # Outputs an updated txt file
    with open(filename, 'r') as file_in:
        reader = csv.reader(file_in, delimiter=',', quotechar='|')
            
        file_output = "turnstile_updated.txt"
        with open(file_output, 'w') as file_out:
            writer = csv.writer(file_out, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for row in reader:
                column_1 = row[0]
                cloumn_2 = row[1]
                column_3 = row[2]
                        
                for i in range(3, len(row)-1, 5):
                    line = [column_1, cloumn_2, column_3, row[i], row[i+1], row[i+2], row[i+3], row[i+4]]
                    writer.writerow(line)

## Output
fix_turnstile_data(filename)