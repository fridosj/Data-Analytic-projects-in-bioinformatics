Greedy Approach or Technique:

As the name implies, this is a simple approach which tries to find the best solution at every step. Thus, it aims to find the local optimal solution at every step so as to find the global optimal solution for the entire problem.

Consider that there is an objective function that has to be optimized (maximized/ minimized). This approach makes greedy choices at each step and makes sure that the objective function is optimized.

The greedy algorithm has only one chance to compute the optimal solution and thus, cannot go back and look at other alternate solutions. However, in many problems, this strategy fails to produce a global optimal solution. Let's consider the following binary tree to understand how a basic greedy algorithm works:



Since we need to maximize the objective function, a Greedy approach can be used. Following steps are followed to find the solution:

Step 1: Initialize sum = 0

Step 2: Select the root node, so its value will be added to sum, sum = 0+8 = 8

Step 3: The algorithm compares nodes at next level, selects the largest node which is 12, making the sum = 20.

Step 4: The algorithm compares nodes at the next level, selects the largest node which is 10, making the sum = 30.

Thus, using the greedy algorithm, we get 8-12-10 as the path. But this is not the optimal solution, since the path 8-2-89 has the largest sum ie 99.

This happens because the algorithm makes decisions based on the information available at each step without considering the overall problem.

Write a PYTHON program to find the path with the largest sum. Tree should have

5 levels 

Extend the program to do for N level