import urllib

def read_text() :
	file = open("./movie_quotes.txt")
	file_content = file.read()
	#print file_content.translate(None, '-()').split()
	file.close()
	check_profanity(file_content)

def check_profanity(text) :
	connection = urllib.urlopen(" http://www.wdylike.appspot.com/?q=" + text)
	output = connection.read()
	#print output
	connection.close()
	if "true" in output :
		print "Profanity Alert !!!"
	elif "false" in output :
		print "You are safe, no curse word found !"
	else :
		print "Document couldn't be scanned."

read_text()
