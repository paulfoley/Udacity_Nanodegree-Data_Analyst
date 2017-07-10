# Decode Secreate Message 2

# Imports
import os

# Function
def rename_files():
	#(1) get file names from a folder
	file_list = os.listdir("/")
	os.chdir("/")

	#(2) for each file, rename filename
	for file_name in file_list:
		os.rename(file_name,file_name.translate("0123456789"))

	os.chdir(saved_path)

	return file_list

# Output
print(rename_files())
