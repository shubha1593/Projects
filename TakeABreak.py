## Keep forgetting to take a break. I'm there to help. Start me when you start your day.

import time
import random
import webbrowser
import urllib2
from bs4 import BeautifulSoup

## Link of the playlist you would want the videos to play from in your break time
playlist_url = 'https://www.youtube.com/playlist?list=FLzvPhPaj_Nz2YH0ocmgi7tg'

html = urllib2.urlopen(playlist_url)
response = html.read()
soup = BeautifulSoup(response)
#res=soup.find_all('tr',class_="pl-video yt-uix-tile ")
res = soup.find_all('a', attrs={'class':'pl-video-title-link'})


## Build a list of links to all your playlist videos
playlist = []

## Also we want to just play one video and not the complete playlist 
## so from all the links remove the playlist part which starts with "&index=" 
pl_part = "&index="
for video in res :
	link = video.get("href")
	index = link.find(pl_part)
	if index != -1 :
		playlist.append(link[:index])
	else :
		playlist.append(link)

## I am assuming that you spend 10 hours on your lappy and I think you should be taking break after every hour
total_breaks = 10
breaks_count = 0
print "This program started at " + time.ctime()
while breaks_count < total_breaks :
	# wait for one hour : 1hr = 60min * 60sec = 3600sec
	time.sleep(3600)
	# select randomly any video from the playlist to play
	v = random.randint(0, len(playlist) - 1)
	link = "https://www.youtube.com" + playlist[v]
	webbrowser.open(link)
	breaks_count += 1