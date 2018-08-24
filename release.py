#!/usr/bin/python

import sys
import urllib2
import json

url = 'https://api.github.com/search/issues?q=project:' + sys.argv[1]

headers = {'Authorization': sys.argv[2]}

req = urllib2.Request(url, headers=headers)
res = urllib2.urlopen(req)

json_obj = json.load(res)

sorted_obj = sorted(json_obj['items'], key=lambda k: k['number'])

f = open('result', 'w')
for item in sorted_obj:
    f.write("#")
    f.write(str(item['number']))
    f.write(" "+item['title'])
    f.write("\n")
f.close()
