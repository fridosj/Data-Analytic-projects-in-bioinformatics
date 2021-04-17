from selenium import webdriver
from bs4 import BeautifulSoup
driver = webdriver.Chrome("C:\Program Files/chromedriver")
driver.get('https://www.genecards.org/cgi-bin/cardlisttxt.pl')
content = driver.page_source
soup1 = BeautifulSoup(content,"html.parser")
out=soup1.pre.string
outfile=open("parsed_genes.txt","a+")
outfile.write(''.join('{}'.format(x) for x in out))
outfile.close()
genes=open("parsed_genes.txt","r")
for gene in genes:
    url="https://www.genecards.org/cgi-bin/carddisp.pl?gene="+gene
    print(url)
    driver.get(url)
    content = driver.page_source
    soup2 = BeautifulSoup(content,"html.parser")
    out=soup2.find("div","col-xs-12 col-sm-4").get_text()
    print(out)
    outfile1=open("gene_with_location.txt",'a+')
    outfile1.write(''.join('{}'.format(gene)))
    outfile1.write(out)
outfile1.close()