from numpy import random
class stack:
    def __init__(self):
        self.stack=[]
        self.size=100
        self.top1=0
        self.top2=60
        
    def push1(self,data):
        if self.top1>=60:
            return("pushing value in stack 1 is {} \nstack full! Cannot push".format(data))
        self.stack.append(data)
        self.top1+=1
        return("value pushed in stack 1 is {}".format(data))  
    def push2(self,data):
        if self.top2>=self.size:
            return("pushing value in stack 2 is {} \nstack full! Cannot push".format(data))
        self.stack.append(data)
        self.top2+=1
        return("value pushed in stack 2 is {}".format(data))  
    def pop1(self):
        if self.top1<=0:
            return("stack empty! Cannot pop")
        item=self.stack.pop(-41)
        self.top1-=1
        return("{} is being popped from Stack 1".format(item))
    def pop2(self):
     try:
        if self.top2<=self.top1:
            return("stack empty! Cannot pop")
        item=self.stack.pop()
        self.top2-=1
        return("{} is being popped from Stack 2".format(item))
     except IndexError:
        return("stack empty! Cannot pop")
    def size(self):
        return self.top
s=stack()
pv1=[]
pv2=[]
for i in random.randint(100,size=(75)):
    print(s.push1(i))
    pv1.append(i)
for i in random.randint(100,size=(75)):
    print(s.push2(i))
    pv2.append(i)
print("pushed values:")
print("stack 1:",end=" ")
for i in pv1:
    print(i,end=" ")
print("\n")
print("stack 2:",end=" ")
for i in pv2:
    print( i,end=" ")
print("\n")
print(s.push1(50))
for i in range(1,70,1):
    print(s.pop1())