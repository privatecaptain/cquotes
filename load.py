import json
from views import db,Quote

f = open('data.json','r')
l = f.readlines()
l = l[0]
q = json.loads(l)




def loadData(q):
	for i in q:
		for j in i:
			quote = Quote()
			quote.content = j
			quote.author = i[j]
			db.session.add(quote)
			db.session.commit()

loadData(q)
