from bs4 import BeautifulSoup
from requests import get
import json
import httplib2
import time

newfile = open ('ObjectDetails_secondhalf.json', 'w')
i = 1

with open('metmuseumurls2.txt', 'r') as URLS:
	for line in URLS:

		objectURL = line.strip()

		h = httplib2.Http()

		resp, htmldoc = h.request(objectURL, "GET")

		soup = BeautifulSoup(htmldoc)

		div = soup.find_all("div", class_= "text-box first cleared ")[0]
		title = div.find_all('h2')[0].string.strip() 

		dl  = soup.find_all("dl", class_="tombstone cleared")[0]
		dts = [dt.string.strip() for dt in dl.find_all('dt')]
		dds = [dd.string.strip() for dd in dl.find_all('dd')]

		div2 = soup.find("div", class_="image-container hero inline")
		img1 = div2.find("img")
		
		
		infos = dict(zip(dts, dds))

		infos['Title'] = title
		infos['URI'] = line
		infos['imageUrl'] = img1["src"]

		prettypretty = json.dumps(infos)

		print prettypretty

		newfile.write(prettypretty + ',')

		i +=1
		print "I'm okay %d: %s" % (i, line)

		time.sleep(1)

newfile.close()





