#!/usr/bin/python
import sys
import urllib2
import json

url = 'https://api.github.com/search/issues?q=project:' + sys.argv[1] + '%20is:issue'
headers = {'Authorization': sys.argv[2]}

req = urllib2.Request(url, headers=headers)
res = urllib2.urlopen(req)

json_obj = json.load(res)

a={}
lines = sorted(json_obj['items'], key=lambda k: k['number'])

for line in lines:
        for label in line['labels']:
                if "@" not in label['name']:
                        if label['name'] not in a.keys():
                                a[label['name']]=['#'+str(line['number'])+' '+line['title']]
                        else:
                                a[label['name']].append('#'+str(line['number'])+' '+line['title'])

#Write results file
result_file = open('resultfile', 'w')

for key in a.keys():
        print '##'+key.capitalize()
        result_file.write('## ')
        result_file.write(key.capitalize())
        result_file.write('\n')
        for val in a.get(key):
                print val
                result_file.write(val)
                result_file.write('\n')
        result_file.write('\n')

result_file.close()
