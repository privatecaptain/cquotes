import requests
from lxml import html 
import json

f = open('data.json','w')


def make_tree(url):
    headers = {'User-Agent':'Mozilla/5.0'}
    page = requests.get(url,headers=headers)
    return html.fromstring(page.text)

def cleanUp(el):
	el = el.strip()
	state = False
	for i in el:
		if i.isalpha():
			state = True
	if state:
		return el
	else:
		return False

urls = []

def getQuotes(url):
	print url
	tree = make_tree(url)
	q = tree.xpath('//*[@class="quoteText"]/text()')
	quotes = []
	for i in q:
		if cleanUp(i):
			quotes.append(cleanUp(i))
	authors = tree.xpath('//*[@class="quoteText"]/a/text()')
	d  = dict(zip(quotes,authors))
	return d

main_url = raw_input('Enter URL : ')
pages = int(raw_input('Enter the no. of pages : '))


def generateURLs(url,n):
	l  = []
	for i in range(1,n+1):
		if i == 1:
			l.append(url)
		else:
			l.append(url+ '?page=' +str(i))
	return l

urls = generateURLs(main_url,pages)

data = []

for i in urls:
	data.append(getQuotes(i))

f.write(json.dumps(data))

f.close()
	
