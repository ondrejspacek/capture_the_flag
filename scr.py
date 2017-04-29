import requests
from lxml import html

secrets=[]
pages=['qds']
i=0

while i < len(pages):
	data=requests.get('https://cdn.hackerrank.com/hackerrank/static/contests/capture-the-flag/infinite/'+pages[i]+'.html')
	tree=html.fromstring(data.content)
	secret=tree.xpath('//font/text()')
	if len(secret) != 0:
		assert len(secret) > 0
		secrets.append(secret[0])
	paths=tree.xpath('//a/text()')
	for path in paths:
		if(path not in pages):
			pages.append(path)
	print "Links searched/known number of links ",str(i+1)+'/'+str(len(pages))
	i += 1

print "Secret phrases:"
for sec in sorted(secrets):
	print sec