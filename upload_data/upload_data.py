import sys
import json
import urllib.parse
import urllib.request
import re

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv[1]))


infile = str(sys.argv[1])
database = str(sys.argv[2])
f = open(infile,'r')

check_term = ""
if database=="PANTHER":
    check_term = "NOT NAMED"

i = 0
for line in f:
    cols = line.split('\t')
    #print(cols[0],end='\n')

    if cols[1].find(check_term) < 0:
        base_data = {
            'db':database,
            'db_id':cols[0],
            'id_desc':cols[1],
        }
        data = urllib.parse.urlencode(base_data)
        data = data.encode('ascii')
    #with urllib.request.urlopen("http://localhost:8000/parse_id/add",data) as f:
    #    f.read().decode('utf-8')
        print(data)
    i = i + 1
    if i == 10:
        break
