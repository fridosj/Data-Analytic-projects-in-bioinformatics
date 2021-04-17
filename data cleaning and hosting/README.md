http://charts.genome.com/gwas/<acceptorchrrsid.txt>

acc_rsid_chr1.txt

acc_rsid_chr2.txt

acc_rsid_chr3.txt

acc_rsid_chr4.txt

acc_rsid_chr5.txt

acc_rsid_chr6.txt

acc_rsid_chr7.txt

acc_rsid_chr8.txt

acc_rsid_chr9.txt

acc_rsid_chr10.txt

acc_rsid_chr11.txt

acc_rsid_chr12.txt

acc_rsid_chr13.txt

acc_rsid_chr14.txt

acc_rsid_chr15.txt

acc_rsid_chr16.txt

acc_rsid_chr17.txt

acc_rsid_chr18.txt

acc_rsid_chr19.txt

acc_rsid_chr20.txt

acc_rsid_chr21.txt

acc_rsid_chr22.txt

acc_rsid_chr23.txt


Table with columns: ChromosomeNumber, Gene, GeneInfo,Transcript,rsID,REF,ALT, Refseq,AltSeq,RefScore,AltScore,Score Difference and Type






Ref the above table and

1. Store this file into a folder of your choice in your AWS Linux MACHINE

2. Write a BASH script to fetch the specified columns if column 11 >10 in length

3. Write into a file name CHR$.txt

4. Develop a PYTHON program to create a single JSON of each chromosome 1..23 and store the details for each rsID as a key for the array.

%data = ( $org => {

$chr => {

$rsid => 

[ $gene, $gene_info, {$transcript_id => [ 

{Ref,Alt,RefSeq,AltSeq, },

{ '$score => [ refscore,altscore ] },

]}}]});


5. Develop a PHP+HTML+JS to fetch the JSON and load it using JQ Data table and provide column based search.

6. Host it using your AWS server and provide me the URL

7. Test it by yourself

8. Will improve the visuals later 

Reference:

http://asia.ensembl.org/info/docs/tools/vep/vep_formats.html


 

Expected output + Visualization

1. Proper Column Name

2. Enable Column Search for each column 

3. Display data of  all the chromosome  with Pagination

4. Plot the Top 10 Genes/rsID based on top score difference between REF and ALT score


BAR CHART should be SVG based and you should create it by learning how to  code for SVG.


Refer:https://www.harvardpilgrim.org/i/doc/bldapp_chrt_svg.htm