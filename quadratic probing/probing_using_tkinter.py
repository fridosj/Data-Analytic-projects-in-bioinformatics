from tkinter import *
root=Tk()

root.geometry("600x600")
add_key_var=StringVar()
rm_key_var=StringVar()
value_var=StringVar()
length=StringVar()
size_var=StringVar()
arr=[(-1,-1)]*7
def create():
    N=length.get()
    N=int(N)
    arr=[(-1,-1)]*N
    print(arr)
def insert():
    k=add_key_var.get()
    v=value_var.get()
    k=int(k)
    v=int(v)
    hv1=k % len(arr)
    kv=k,v
    if (arr[hv1]==(-1,-1)):
        arr[hv1]=kv
    else:
        for j in range(len(arr)):
            hv2=(hv1+j*j)%len(arr)
            if (arr[hv2]==(-1,-1)):
                arr[hv2]=kv
                break
    print(arr)
    print("key{} has been inserted".format(k))
def delete():
    key=rm_key_var.get()
    for (k,v) in arr:
        if int(key)==k:
            for i in range(len(arr)):
                    if (arr[i]==(k,v)):
                        arr[i]=(-1,-1)
                        print("key {} has been removed".format(key))
        
def size():
    count=0
    for (k,v) in arr:
        if k!=-1:
            count+=1
    print("Size of hash table is {}".format(count))
    size_var.set(count)
def display():
   n=length.get()
   n=int(n)
   for i in range(n):
    k,v=arr[i]
    Label(root,text="H:{}".format(i)).grid(row=i+4,column=0)
    Label(root,text="K:{},V:{}".format(k,v)).grid(row=i+4,column=1)
            

#create
hash_label = Label(root, text = 'Length hash', font=('calibre',10, 'bold'))
hash_entry = Entry(root,textvariable = length, font=('calibre',10,'normal'))
create_btn=Button(root,text = 'Create empty hash', command = create)
#insert
kv_label = Label(root, text = 'Enter key and value', font=('calibre',10, 'bold'))
key_entry = Entry(root,textvariable = add_key_var, font=('calibre',10,'normal'))
value_entry = Entry(root,textvariable = value_var, font=('calibre',10,'normal'))
insert_btn=Button(root,text = 'Insert', command = insert)
#remove
remove_label = Label(root, text = 'Enter key', font=('calibre',10, 'bold'))
remove_entry = Entry(root,textvariable = rm_key_var, font=('calibre',10,'normal'))
remove_btn=Button(root,text = 'Delete', command = delete)
#size
size_label = Label(root, text = 'Size of hash table is', font=('calibre',10, 'bold'))
size_btn=Button(root,text = 'Check', command = size)
size_fld=Entry(root,textvariable=size_var)
display_btn=Button(root,text = 'Check', command = display)
#grid
hash_label.grid(row=0,column=0)
hash_entry.grid(row=0,column=1)
create_btn.grid(row=0,column=2)
kv_label.grid(row=1,column=0)
key_entry.grid(row=1,column=1)
value_entry.grid(row=1,column=2)
insert_btn.grid(row=1,column=3)
remove_label.grid(row=2,column=0)
remove_entry.grid(row=2,column=1)
remove_btn.grid(row=2,column=2)
size_label.grid(row=3,column=0)
size_btn.grid(row=3,column=1)
size_fld.grid(row=3,column=2)
display_btn.grid(row=4,column=5)
root.mainloop()