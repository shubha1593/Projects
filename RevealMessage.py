## Reveal the secret message and tell me of what it reminds you !!
## Make sure in finder in secretMessage folder, you have files sorted by names and in the folder you have a grid view.

import os
from string import digits

directory = "./secretMessage"

# get a list of all file names
files = os.listdir(directory)
#print files

cwd = os.getcwd()
os.chdir(directory)

for file_name in files :
	#print("Old name : " + file_name)
	#print("New name : " + file_name.translate(None, digits))
	os.rename(file_name, file_name.translate(None, digits))

os.chdir(cwd)
#print os.listdir("./secretMessage)