import sys
import json
import urllib.parse
import urllib.request
import re

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv[1]))


infile = str(sys.argv[1])
database = str(sys.argv[2])

#with some files which have accented names reading error occurs sometime
f = open(infile,'r',encoding="latin-1")

check_term = ""
id_col = 0
desc_col = 0
cat_term = ""
if database=="PANTHER":
    check_term = "NOT NAMED"
    cat_term = ""
    id_col = 0
    desc_col = 1
elif database == "Pfam":
    check_term = "9999999999999999"
    cat_term = ""
    id_col = 0
    desc_col = 3
elif database == "Gene3D":
    check_term = "9999999999999999"
    cat_term = "G3DSA:"
    id_col = 0
    desc_col = 3
elif database == "SUPERFAMILY":
    check_term = "\spx\s|\ssp\s"
    cat_term = "SSF"
    id_col = 0
    desc_col = 4
elif database == "PIRSF":
    check_term = "9999999999999999"
    cat_term = ""
    id_col = 0
    desc_col = 1

exist_records = 0
add_records = 0
i = 0
for line in f:
    cols = line.split('\t')
    pattern = re.compile(check_term)
    #print(pattern)
    matching = pattern.search(line)
    #print(matching)
    if matching == None and line.find("#") != 0:
        base_data = {
            'db':database,
            'db_id':cat_term+cols[id_col],
            'id_desc':cols[desc_col],
        }
        data = urllib.parse.urlencode(base_data)
        data = data.encode('utf-8')
        req = urllib.request.Request("http://localhost:8000/parse_id/add/",data)
        try:
            urllib.request.urlopen(req)
        except urllib.error.HTTPError as e:
            if e.code == 400:
                exist_records = exist_records + 1
            else:
                print(e.code,e.reason,end='\n')
        else:
            add_records = add_records + 1

        #the_page = response.read().decode('utf-8')
        #print(the_page)
        #j = j + 1
        #print(line,end='\n')
        #print(data)
    #else:
        #print("Line contained filter term " + line,end='\n')

    i = i + 1
    if i % 10 == 0:
        print("Processed ", i ," records and added ", add_records, " to the database",end="\n")
