https://docs.google.com/document/d/12qaJzM86o246srLVKnob4ywhZnpbhaCA6vWxVRL9t9Q/edit?usp=sharing

Matrix
How do I solve a Matrix problem?
A large class of matrix problems can be mapped to graphs
Algorithms you should think about:
BFS
DFS
What is the graph? (For any problem that you map to graphs)
V= Each cell in the matrix is a node
E= Adjacent cells (depending on the problem):
Suppose you can only go right and down: there is an edge between each cell to the right one and the bottom one.
Sometimes the problem mentions some cells are blocked (i.e. they have 0 value). In this case

2 for loops to iterate through all cells
Examples:
Rotate a matrix (not a graph problem)
Finding islands (can be mapped on graphs)
Shortest paths (graph problem)
Snake and ladder (graph problem)
Spiral path in a matrix (can be done without graphs)

Write a template for backtracking on a matrix
Iterating all paths in the matrix.
That means we will have a decision tree
If we can only go down and right, the decision tree is a finite tree
The height of this tree is: m+n
If we can go all directions, the decision tree is infinite.
You need to have some pruning conditions
e.g. mark visited cells and never go back to them:

Write DFS/BFS on a matrix (assuming you can all four directions)
In these problems we start from one node and run DFS/BFS to get to the destination and along the path might gather some information.

Backtrack(c){

for (each neighbor n of c){
if(prune(n)) { // Backtracking optimization
continue;
}
Backtrack(n);
}

}
What is the runtime and space complexity of a Matrix traversal algorithm?
Runtime:
Iterate through the matrix: O(mxn)
Backtracking when you can only go down and right: O(2^(m+n))
Backtracking when you can go in all four directions: No bound unless there is some pruning condition in the algorithm.
If we visit each cell only once at each branch of the tree, then the runtime would be O(4^(m*n))
DFS/BFS: O(m*n)
Memory:
DFS:
Call stack: O(m*n).
BFS:
Max queue size: O(m*n).

What is the runtime and space complexity of a Matrix backtracking algorithm?

How do I know that I should be using a Matrix solution?

- Says "matrix" or looks like a matrix

How do I solve a matrix problem?

- Just do it: use loops (straightforward, brute force)
- Solve it like a graph problem (backtracking)
  - Depth-first and breadth-first search
  - Dynamic programming
  - Difference:
    definition of "neighbor"
    "visited" set can often be maintained by modifying the matrix

Write a template for backtracking on a matrix

maze(matrix, start, end)
initialize path to []
initialize memo_set to empty set

define helper(location):

    if location is in memo_set return false

    if location is end then return true

    if location is in a wall or outside the matrix
      return false

    mark location in the matrix as a wall
    for each neighbor
      add neighbor direction to path
      if helper(neighbor) then return true
      remove neighbor direction from
    unmark (clear) location

    add location to memo_set
    return false

call helper(start)
return path

What is the runtime and space complexity of a Matrix traversal
(nested loop) algorithm?

O(size of matrix)

What is the runtime and space complexity of a Matrix backtracking algorithm?

O(4^(size of matrix)) without Dynamic Programming
