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
id_col = 0
desc_col = 0
if database=="PANTHER":
    check_term = "NOT NAMED"
    id_col = 0
    desc_col = 1
elif database == "Pfam":
    check_term = "9999999999999999"
    id_col = 0
    desc_col = 3

i = 0
for line in f:
    cols = line.split('\t')

    if cols[1].find(check_term) < 0:
        base_data = {
            'db':database,
            'db_id':cols[id_col],
            'id_desc':cols[desc_col],
        }
        data = urllib.parse.urlencode(base_data)
        data = data.encode('utf-8')

        with urllib.request.urlopen("http://localhost:8000/parse_id/add/",data) as f:
            f.read().decode('utf-8')
        #print(data)
    else:
        print(cols[id_col],cols[desc_col],end='\n')

    i = i + 1
    if i % 10 == 0:
        print("Processed ",i," records",end="\n" )
