Write a PYTHON Program to Implement two Stacks using a Single Array & Check for Overflow & Underflow

This Program Implements two Stacks using a Single Array & Check for Overflow & Underflow. A Stack is a linear data structure in which a data item is inserted and deleted at one record. A stack is called a Last In First Out (LIFO) structure. Because the data item inserted last is the data item deleted first from the stack.

To implement two stacks in one array, there can be two methods.

First is to divide the array into two equal parts and then give one half two each stack. But this method wastes space.

So a better way is to let the two stacks to push elements by comparing tops of each other, and not up to one half of the array.

Push and Pop functions of both stack in the following code have their Time Complexity as O(1). They take constant time.

Print is O(n), where n is the number of elements in the stack.

The program has an array of size 100. 60 random integer values are pushed in stack 1 and 40 random integer values in two. All conditions are being checked.

Expected output:

We can push a total of 100 values

Value Pushed in Stack 1 is 1

Value Pushed in Stack 1 is 2

Value Pushed in Stack 1 is 3

Value Pushed in Stack 1 is 4

.....

Value Pushed in Stack 1 is 60

Value Pushed in Stack 2 is 1

..........

Value Pushed in Stack 2 is 40

 

Print Pushed Values:

60 59 58 57..... 6 5 4 3 2 1 

40 39 38.... 3 2 1 

 

Pushing Value in Stack 1 is 101

Stack Full! Cannot Push

 

60 is being popped from Stack 1

59 is being popped from Stack 1

58 is being popped from Stack 1

...........

...........

3 is being popped from Stack 1

2 is being popped from Stack 1

1 is being popped from Stack 1

Stack Empty! Cannot Pop