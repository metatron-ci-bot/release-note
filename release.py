#!/usr/bin/python

import sys
import urllib2
import json

# Setup for using github api
url = 'https://api.github.com/search/issues?q=project:' + sys.argv[1]
label_url = 'https://api.github.com/repos/'+sys.argv[2]+'/'+ sys.argv[3]+'/labels'

headers = {'Authorization': sys.argv[4]}

# Request for GET Project Issues List
req = urllib2.Request(url, headers=headers)
res = urllib2.urlopen(req)

json_obj = json.load(res)

sorted_obj = sorted(json_obj['items'], key=lambda k: k['number'])

# Request for GET Labels
req = urllib2.Request(label_url, headers=headers)
res = urllib2.urlopen(req)

json_obj = json.load(res)

labels = list()

for i in json_obj:
        if "@" in i['name']:
                labels.append(i['name'])

# Write results file
result_file = open('resultfile', 'w')

for label in labels:
        print label
        result_file.write("## ")
        result_file.write(label[1:].capitalize())
        result_file.write("\n")
        for issue in sorted_obj:
                for names in issue['labels']:
                        if names['name'] == label:
                                print issue['number'], issue['title']
                                result_file.write("> #")
                                result_file.write(str(issue['number']))
                                result_file.write(" "+issue['title'])
                                result_file.write("\n")
print "### Additional Changes"
result_file.write("## Additional Changes\n")
label_break = True
for issue in sorted_obj:
        for names in issue['labels']:
                if names['name'].find("@"):
                        label_break = False
                        break
                else:
                        print issue['number'], issue['title']
                        result_file.write("> #")
                        result_file.write(str(issue['number']))
                        result_file.write(" "+issue['title'])
                        result_file.write("\n")
        if (label_break == False):
                break
result_file.close()
