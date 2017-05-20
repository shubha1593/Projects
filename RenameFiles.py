## Rename by removing the digits from all file names in the directory

import os
from string import digits

# get a list of all file names
files = os.listdir("./prank")
#print files

for file_name in files :
	print("Old name : " + file_name)
	print("New name : " + file_name.translate(None, digits))
	os.rename("./prank/" + file_name, "./prank/" + file_name.translate(None, digits))

#print os.listdir("./prank")

