Problem Description

A hash table is a data structure used to implement an associative array, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots. Quadratic Probing is similar to Linear Probing. The difference is that if we try to insert into a space that is filled we would first check 1^1=1 element away then 2^2=4 elements away, then 3^2=9 elements away then 4^2=16 elements away and so on.

Steps:

1.Create an array of structure (i.e a hash table).

2.Take a key and a value to be stored in a hash table as input.

3.Corresponding to the key, an index will be generated i.e every key is stored in a particular array index.

4.Using the generated index, access the data located in that array index.

5.In case of absence of data, create one and insert the data item (key and value) into it and increment the size of the hash table.

6.In case the data exists, probe through the subsequent elements (looping back if necessary) for free space to insert new data items.

	a.Note: This probing will continue until we reach the same element again (from where we began probing)

	b.Note: Here, unlike Linear Probing, probing will be done according to the following formula –

	c.(currentPosition + h) % arraySize => Linear Probing

	d.(currentPosition + (h * h)) % arraySize => Quadratic Probing

	e.where h = 1, 2, 3, 4 and so on.

7.To display all the elements of the hash table, an element at each index is accessed (via for loop).
8.To remove a key from a hash table, we will first calculate its index and delete it if the key matches, else probe through elements until we find the key or an empty space where not a single data has been entered (means data does not exist in the hash table).
9.Exit

Expected Output

Visualization: Leaving to you but please check https://visualgo.net/en/hashtable before you proceed

Implementation of Hash Table in PYTHON with Quadratic Probing

MENU-:

1. Inserting item in the Hash table

2. Removing item from the Hash table

3. Check the size of Hash table

4. Display Hash table

 

Please enter your choice-: 3

Size of hash table is-: 0

 

Do you want to continue-:(press 1 for yes) 1

Implementation of Hash Table in PYTHON with Quadratic Probing

MENU-:

1. Inserting item in the Hash table

2. Removing item from the Hash table

3. Check the size of Hash table

4. Display Hash table

 

Please enter your choice-: 1

Inserting element in Hash table

Enter key and value-:   12 	10

 

 Key (12) has been inserted

 

Do you want to continue-:(press 1 for yes) 1

Implementation of Hash Table in PYTHON with Quadratic Probing

MENU-:

1. Inserting item in the Hash table

2. Removing item from the Hash table

3. Check the size of Hash table

4. Display Hash table

 

Please enter your choice-: 1

Inserting element in hash table

Enter key and value-:   122 	4

 

 Key (122) has been inserted

 

Do you want to continue-:(press 1 for yes) 1

Implementation of Hashtable in PYTHONwith Quadratic Probing

MENU-:

1. Inserting item in the Hash table

2. Removing item from the Hash table

3. Check the size of Hash table

4. Display Hash table

 

Please enter your choice-: 1

Inserting element in hash table

Enter key and value-:   82 	5

 

 Key (82) has been inserted

 

 

Do you want to continue-:(press 1 for yes) 1

Implementation of Hashtable in PYTHONwith Quadratic Probing

MENU-:

1. Inserting item in the Hash table

2. Removing item from the Hash table

3. Check the size of Hash table

4. Display Hash table

 

Please enter your choice-: 3

Size of hash table is-: 3

 

Do you want to continue-:(press 1 for yes) 1

Implementation of Hashtable in PYTHONwith Quadratic Probing

MENU-:

1. Inserting item in the Hash table

2. Removing item from the Hash table

3. Check the size of Hash table

4. Display Hash table

 

Please enter your choice-: 4

Array[0] has  no elements

 

Array[1] has no elements

 

Array[2] has elements-:

12 (key) and 10 (value)

 

Array[3] has elements-:

122(key) and 4(value)

 

Array[4] has no elements

 

Array[5] has no elements

 

Array[6] has no elements

 

Array[7] has no elements

82(key) and 5(value)

Array[8] has no elements

 

Array[9] has no elements

 

 

Do you want to continue-:(press 1 for yes) 1

Implementation of Hashtable in PYTHONwith Quadratic Probing

MENU-:

1. Inserting item in the Hash table

2. Removing item from the Hash table

3. Check the size of Hash table

4. Display Hash table

 

Please enter your choice-: 2

Deleting in hash table

Enter the key to delete-: 122

 

 Key (122) has been removed

 

Do you want to continue-:(press 1 for yes) 1

Implementation of Hashtable in PYTHONwith Quadratic Probing

MENU-:

1. Inserting item in the Hash table

2. Removing item from the Hash table

3. Check the size of Hash table

4. Display Hash table

 

Please enter your choice-: 2

Deleting in hash table

Enter the key to delete-: 56

 

 This key does not exist

 

Do you want to continue-:(press 1 for yes) 2