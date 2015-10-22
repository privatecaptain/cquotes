import requests
from lxml import html 
import json

f = open('data.json','w')


def make_tree(url):
    headers = {'User-Agent':'Mozilla/5.0'}
    page = requests.get(url,headers=headers)
    return html.fromstring(page.text)


urls = []

def getQuotes(url):
	tree = make_tree(url)
	quotes = tree.xpath('//*[@title="view quote"]/text()')
	authors = tree.xpath('//*[@title="view author"]/text()')
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
			l.append(url+str(n))
	print l
	return l

urls = generateURLs(main_url,pages)

data = []

for i in urls:
	data.append(getQuotes(i))

f.write(json.dumps(data))

f.close()
	
