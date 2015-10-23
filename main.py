import requests
from lxml import html 
import json
from views import db,Quote




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


def getQuotes(url):
	print url
	tree = make_tree(url)
	q = tree.xpath('//*[@class="quoteText"]')
	quotes = []
	quotes = [i.text.strip() for i in q]
	authors = tree.xpath('//*[@class="quoteText"]/a/text()')
	d  = dict(zip(quotes,authors))
	return d






def generateURLs(url,n):
	l  = []
	for i in range(1,n+1):
		if i == 1:
			l.append(url)
		else:
			l.append(url+ '?page=' +str(i))
	return l

def do():
	main_url = raw_input('Enter URL : ')
	pages = int(raw_input('Enter the no. of pages : '))
	f = open('data.json','w')
	urls = []
	urls = generateURLs(main_url,pages)

	data = []
	for i in urls:
		data.append(getQuotes(i))

	f.write(json.dumps(data))

	f.close()
	
