## Decode A Message

# Imports
import os

# Function
def rename_files():
	#(1) get file names from a folder
	file_list = os.listdir("/Users/Nexu/Desktop/Bill_Gates/Coding/Udacity/1. Programming/Decode_Message/secret_message")
	os.chdir("/Users/Nexu/Desktop/Bill_Gates/Coding/Udacity/1. Programming/Decode_Message/secret_message")
	#(2) for each file, rename filename
	for file_name in file_list:
		os.rename(file_name, file_name.translate("0123456789"))
  	
  	os.chdir("/Users/Nexu/Desktop/Bill_Gates/Coding/Udacity/1. Programming/Decode_Message/")
  	
  	return file_list

# Output
print(rename_files())
