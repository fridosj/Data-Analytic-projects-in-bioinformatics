from Bio.Seq import Seq
import secrets
def dna(len):
    return "".join(secrets.choice('ATGC') for i in range(len))
base=int(input("enter the number of bases"))
a=dna(base)
b=a[::-1]
start={'ATG':0}
stop={'TAA':0,'TAG':0,'TGA':0}
seq_1="".join([a[i:i+3] for i in range(0, len(a),3)])
seq_2="".join([b[i:i+3] for i in range(0, len(a),3)])
seq_3="".join([a[i+1:i+4] for i in range(0, len(a),3)])
seq_4="".join([b[i+1:i+4] for i in range(0, len(a),3)])
seq_5="".join([a[i+2:i+5] for i in range(0, len(a),3)])
seq_6="".join([b[i+2:i+5] for i in range(0, len(a),3)])
seqs=[seq_1,seq_2,seq_3,seq_4,seq_5,seq_6]

pr_1=Seq(seq_1).translate()
pr_2=Seq(seq_2).translate()
pr_3=Seq(seq_3).translate()
pr_4=Seq(seq_4).translate()
pr_5=Seq(seq_5).translate()
pr_6=Seq(seq_6).translate()
prs=[pr_1,pr_2,pr_3,pr_4,pr_5,pr_6]
c=0
for pr in prs:
    print("protein sequence in reading frame",c,'\n',pr)
    c+=1
n=1
for seq in seqs:

    for codon in start:
         start[codon]=0
    for codon in stop:
         stop[codon]=0
    for codon in start:
         for i in range(0,len(seq),3):
            str=seq[i:i+3]
            count1=str.count(codon)
            start[codon]+=count1
            if count1>0:
                pos1=i
                from_start=Seq(seq[pos1:]).translate()
                break
            else:
                pos1=0
    for codon in stop:
         for i in range(0,len(seq),3):
            str=seq[i:i+3]
            count=str.count(codon)
            stop[codon]+=count
    print("In reading frame",n)
    print(start)
    print(stop)
    if count1>0:
     print(from_start)
    n+=1