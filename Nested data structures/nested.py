import ensembl_rest 
import requests, sys
from pyensembl import EnsemblRelease
from collections import OrderedDict
import json
data=EnsemblRelease(95)
keys=['id','description','display_name','biotype']
ids=data.gene_names()
keys1=['display_name','len']
out=[]
dom=[]
for id in ids:
  try:
    a=ensembl_rest.symbol_lookup('homo sapiens', id)
    res = dict((k, a[k]) for k in keys if k in a) 
    inp=res['id']
    server = "https://rest.ensembl.org"
    ext = "/sequence/id/"+inp+"?"
 
    r = requests.get(server+ext, headers={ "Content-Type" : "text/plain"})
    if not r.ok:
        r.raise_for_status()
        sys.exit()
    a=r.text
    res['seq']=a
    res['len']=len(res['seq'])
    gene_len = dict((k, res[k]) for k in keys1 if k in res)
    print(gene_len)
    out.append(res)
    dom.append(gene_len)
  except :
      continue
genes=out
def arrayofhashes():
    with open('aoh.txt', 'w') as f:
     f.write(repr(genes))
    f.close()
    return genes
def arrayofarrays():
 aoa=[]
 for idx, sub in enumerate(genes, start = 0): 
    if idx == 0: 
        aoa.append(list(sub.keys())) 
        aoa.append(list(sub.values())) 
    else: 
        aoa.append(list(sub.values())) 
    with open('aoa.txt','a+') as out:
        out.write(json.dumps(aoa))
    out.close()
    return aoa
#dictionary of dictionaries
def hashofhashes():
    hoh = {}
    for i, d in enumerate(genes):
     hoh[i] = d
    with open('hoh.txt','a+') as out:
        out.write(json.dumps(hoh))
    out.close()
    return hoh
#dictoflists
def hashofarrays():
    hoa={k: [dic[k] for dic in genes] for k in genes[0]}
    with open('hoa.txt','a+') as out:
        out.write(json.dumps(hoa))
    out.close()
    return hoa
dictionary = {}
for i, d in enumerate(dom):
    dictionary[i] = d
top=dict(sorted(dictionary.items(), key=lambda x: x[1]['len'], reverse=True)[:10])
arrayofarrays()
arrayofhashes()
hashofhashes()
hashofarrays()
print(top)