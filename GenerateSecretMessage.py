## Fun secret message. Another memory test, this time a lot easier ;P

import os
import random

files = os.listdir("./secretMessage")
randomList = [i for i in range(1, len(files) + 1)]
random.shuffle(randomList)

cwd = os.getcwd()
os.chdir("./secretMessage")
for i in range(0, len(files)) :
	os.rename(files[i], str(randomList[i]) + files[i])
	
os.chdir(cwd)