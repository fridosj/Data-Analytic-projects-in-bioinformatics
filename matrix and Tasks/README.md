You are given an integer N  denoting an N×N  matrix. Initially, each cell of the matrix is empty. You are given K  tasks. In each task, you are given a cell (i,j)  where cell (i,j)  represents the 

ith  row and jth  column of the given matrix.

 

Input format:

The first line contains two space-separated integers N and K where N is the number of rows and columns in the given matrix and K is the number of tasks respectively.

Next K lines contain two space-separated integers i and j.

Output format:

Print K space-separated integers denoting the number of empty cells in the matrix.

Constraints:

1≤N≤105

1≤K≤1000

1≤i,j≤N

 

Sample Input

3 3

1 1

1 3

3 2


Sample Output

4 2 0

Explanation

Initially all the cells [{1, 1}, {1, 2}, {1, 3}, {2, 1}, {2, 2}, {2, 3}, {3, 1}, {3, 2}, {3, 3}] are empty.

After the first task:

Empty cells are [{2, 2}, {2, 3}, {3, 2}, {3, 3}]. Therefore, the answer is 4.

After the second task:

Empty cells are [{2, 2}, {3, 2}]. Therefore, the answer is 2.

After the third task:

No cells remain empty. Therefore, the answer is 0.

Write a PYTHON program to replicate this for the NxN matrix.