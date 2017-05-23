## Rename by removing the digits from all file names in the directory

import os
from string import digits

directory = "./prank"

# get a list of all file names
files = os.listdir(directory)
#print files

cwd = os.getcwd()
os.chdir(directory)

for file_name in files :
	print("Old name : " + file_name)
	print("New name : " + file_name.translate(None, digits))
	os.rename(file_name, file_name.translate(None, digits))

os.chdir(cwd)
#print os.listdir("./prank")

