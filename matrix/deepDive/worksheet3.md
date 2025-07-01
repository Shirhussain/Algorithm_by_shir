How do I know that I should be using a Matrix solution?

- "matrix", there's a grid, ...

How is a matrix problem different from a graph problem?

- how the graph is specified
  -- typical graph problem, you're given nodes and edges (adjacency list, edge list)
  -- given a matrix, neighbors are defined geometrically

How do I solve a matrix problem?

- typically, the same you solve a graph problem: depth-first and breadth-first search
  -- often, the matrix itself can provide visited set information
- sometimes, a simple traversal is adequate

Write a template for backtracking (DFS) on a matrix

dfs(matrix, start, finish)

define answer variable
def helper(node, path)
if node is finish
add node to path
copy path to answer variable
return true
if node is outside matrix
return false
add node to path
for each neighbor

    remove node from path

if helper(start, []) then
return answer variable
else
return "failure"

Write a template for BFS on a matrix

create an empty queue
store initial element coordinates in queue
somehow mark element as visited
while queue is not empty
remove node from front of queue
process node
add neighbors to queue and to visited set (or mark in matrix)

What is the runtime and space complexity of a Matrix traversal
(nested loop) algorithm?

Assuming N by M matrix

- Time:
- Space:

What is runtime and space complexity for BFS?

- Time:
- Space:

What is the runtime and space complexity of a Matrix backtracking algorithm?

- Time:
- Aux. Space:
