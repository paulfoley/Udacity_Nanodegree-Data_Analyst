"""
This and the following exercise are using US Patent database. The patent.data
file is a small excerpt of much larger datafiles that are available for
download from US Patent website. These files are pretty large ( >100 MB each).
The original file is ~600MB large, you might not be able to open it in a text
editor.

The data itself is in XML, however there is a problem with how it's formatted.
Please run this script and observe the error. Then find the line that is
causing the error. You can do that by just looking at the datafile in the web
UI, or programmatically. For quiz purposes it does not matter, but as an
exercise we suggest that you try to do it programmatically.

NOTE: You do not need to correct the error - for now, just find where the error
is occurring.

# So, the problem is that the gigantic file is actually not a valid XML, because
# it has several root elements, and XML declarations.
# It is, a matter of fact, a collection of a lot of concatenated XML documents.
# So, one solution would be to split the file into separate documents,
# so that you can process the resulting files as valid XML documents.
"""

# Functions
def split_file(filename):
    """
    Split the input file into separate files, each containing a single patent.
    As a hint - each patent declaration starts with the same line that was
    causing the error found in the previous exercises.
    
    The new files should be saved with filename in the following format:
    "{}-{}".format(filename, n) where n is a counter, starting from 0.
    """
    with open(filename, 'r') as file:
    		splitter = file.readline()
    		file_list = file.read().split(splitter)
    		for n, lines in enumerate(file_list):
    			with open("{}-{}".format(filename, n),'w') as file:
    				file.write(splitter)
    				file.write(lines.strip())
    pass

def output():
    split_file('patent.xml')
    for n in range(4):
        try:
            filename = "{}-{}".format("patent.xml", n)
            file = open(filename, "r")
            print('Success')
            if not file.readline().startswith("<?xml"):
                print("You have not split the file {} in the correct boundary!".format(filename))
            file.close()
        except:
            print("Could not find file {}. Check if the filename is correct!")

output()
