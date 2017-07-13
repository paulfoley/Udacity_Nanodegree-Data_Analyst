'''
    Filenames is a list of MTA Subway turnstile text files. A link to an example
    MTA Subway turnstile text file can be seen at the URL below:
    http://web.mta.info/developers/data/nyct/turnstile/turnstile_110507.txt
    
    As you can see, there are numerous data points included in each row of the
    a MTA Subway turnstile text file. 

    You want to write a function that will update each row in the text
    file so there is only one entry per row. A few examples below:
    A002,R051,02-00-00,05-28-11,00:00:00,REGULAR,003178521,001100739
    A002,R051,02-00-00,05-28-11,04:00:00,REGULAR,003178541,001100746
    A002,R051,02-00-00,05-28-11,08:00:00,REGULAR,003178559,001100775
    
    Write the updates to a different text file in the format of "updated_" + filename.
    For example:
        1) if you read in a text file called "turnstile_110521.txt"
        2) you should write the updated data to "updated_turnstile_110521.txt"

    The order of the fields should be preserved. Remember to read through the 
    Instructor Notes below for more details on the task.
    
    You can see a sample of the turnstile text file that's passed into this function
    and the the corresponding updated file by downloading these files from the resources:
'''
#imports
import csv

# Functions
def fix_turnstile_data(name):
    with open(name, 'r') as file_in:
        reader_in = csv.reader(file_in, delimiter=',', quotechar='|')
            
        file_output = "turnstile_output_1.txt"
        with open(file_output, 'w') as file_out:
            writer_out= csv.writer(file_out, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for row in reader_in:
                column_1 = row[0]
                cloumn_2 = row[1]
                column_3 = row[2]
                    
                for i in range(3, len(row)-1, 5):
                    line = [column_1, cloumn_2, column_3, row[i], row[i+1], row[i+2], row[i+3], row[i+4]]
                    writer_out.writerow(line)

fix_turnstile_data('turnstile.txt')
