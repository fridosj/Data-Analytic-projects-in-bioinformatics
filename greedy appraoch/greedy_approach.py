from numpy import random
from binarytree import build

class node:
    def __init__(self, data):
        self.data=data
        self.left=self.right=None
def insert(arr,root,i,n):
    if i<n:
        temp=node(arr[i])
        root=temp
        root.left=insert(arr,root.left,2*i+1,n)
        root.right=insert(arr,root.right,2*i+2,n)
    return root
def roottoleafSum(root):
 
    # base case: tree is empty
    if root is None:
        return 0, []
 
   
    left_sum, left_path = roottoleafSum(root.left)
 
    right_sum, right_path = roottoleafSum(root.right)
 
    if left_sum > right_sum:
        max_sum = left_sum
        max_path = left_path
    else:
        max_sum = right_sum
        max_path = right_path
        

    max_path.append(root.data)
    max_sum = max_sum + root.data
    
    return max_sum, max_path

def findMaxSumPath(root):
 
    max_sum, path = roottoleafSum(root)
    print("Maximum sum is", max_sum)
    print("Maximum sum path is: ", path, end='')
level=int(input("enter the level of binary tree: "))
num=(2**level)-1    
arr=random.randint(100,size=(num))
tree=build(arr)
print(tree)
n=len(arr)
root=None
root=insert(arr,root,0,n)
findMaxSumPath(root)