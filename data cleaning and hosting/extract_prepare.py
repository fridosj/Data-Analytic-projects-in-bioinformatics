import urllib.error, urllib.parse, urllib.request
import numpy as np
import pandas as pd
import csv
import json
a=np.arange(1,24,1)
headers=['CHROMOSOMES','A','GENE','GENE_INFO','B','TRANS','C','D','E','F','RSID','G','H','REF','ALT','REFSEQ','ALTSEQ','REFSCORE','ALTSCORE','I','J','K','TYPE']
lo=[]   
data={"data":[]}
for i in a:
    i=str(i)
    url = "http://charts.genome.com/gwas/acc_rsid_chr"+i+".txt"
    file = urllib.request.urlopen(url)
    name="chro"+i
    with open("{}.txt".format(name),"w") as out:
     for line in file:
        decoded_line = line.decode()
        decoded_line=decoded_line.replace("X","23")
        out.write(decoded_line)
    out.close()
    print(name)
print("done")

for i in a:
    i=str(i)
    name="chro"+i
    file=pd.read_csv("{}.txt".format(name),delimiter='\t',names=headers)
    file=file.drop(columns=['A','B','C','D','E','F','G','H','I','J','K'])
    file['SCORE']=file['REFSCORE']-file['ALTSCORE']
    file.to_csv('{}.csv'.format(name),index=None)
    print(name)
print("done")
for i in range(1,24):
    with  open('chro'+str(i)+'.csv','r') as f:
        reader=csv.reader(f)
        next(reader)
        for row in reader:
            if row:
                data["data"].append({"RSID":row[4],"CHROMOSOMES":"CHR"+str(row[0]),"GENE":row[1],"GENE_INFO":row[2],"TRANS":row[3],"REF":row[5],"ALT":row[6],"REFSEQ":row[7],"ALTSEQ":row[8],"REFSCORE":row[9],"ALTSCORE":row[10],"TYPE":row[11],"SCORE":row[12]})
   
with open('CHROMOSOMES.json','w')as f1:
        f1.write(json.dumps(data, indent=4))
print("Json created")
