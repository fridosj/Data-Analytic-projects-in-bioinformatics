import numpy as np
tasks=[]
while True:
  try:
    N,K= input("enter N and K seperated by two spaces:").split("  ")
    N=int(N)
    K=int(K)
    if 1<=N<=(10*5) and 1<=K<=1000:
        break
    else:
        print('enter N<=10^5 and K<=1000 ')
  except:
        continue
matrix=np.arange(1,(N**2)+1).reshape(N,N)
num=1
while num<=K<=1000 :
    i,j=input("enter i and j seperated by two spaces:").split("  ")
    i=int(i)
    j=int(j)
    task=(i,j)
    if 1<=i<=N and 1<=j<=N:
        tasks.append(task)
        num+=1
    else:
        print('i,j must be less than or equal to N')
for i,j in tasks:
    matrix[i-1]=0
    matrix[:,j-1]=0
    count=np.count_nonzero(matrix)
    print(count,end=" ")