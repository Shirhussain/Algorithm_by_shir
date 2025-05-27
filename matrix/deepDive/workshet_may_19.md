How do I know that I should be using a Matrix solution?

- Given a matrix(!)
- Or something that looks like a matrix/can be stored in a 2D array

How is a matrix problem different from a graph problem?

- Graph has nodes and edges defining neighbors,
- matrix has elements with geometry defining neighbors

How do I solve a matrix problem?

- Often, use a graph algorithm
- Sometimes, solution is (or involves) or more geometric approach

Write a template for backtracking (DFS) on a matrix

// find if there is a path from upper left to lower right of a maze (o is clear, x is a wall)
// define neighbors up, down, left, right only
def maze(matrix):

def dfs(i,j):
if (i,j) is outside the matrix
return false
if matrix(i,j) is an x
return false
if (i,j) is lower right corner
return true # if visited (i,j) return false

    mark matrxi(i,j) as visited: store an 'x' in matrix(i,j),
    for each neighbor of (i,j)
      if dfs(neighbor)
        return true
    unmark matrix(i,j) as visited: store an 'o' in matrix(i,j)
    return false

return dfs(0,0)

Write a template for BFS on a matrix

What is the runtime and space complexity of a Matrix traversal
(nested loop) algorithm?

Assuming N by M matrix

- Time: O(NM)
- Space: O(1)

What is runtime and space complexity for BFS?

- Time:
- Space:

What is the runtime and space complexity of a Matrix backtracking algorithm?

- Time: O(4^(max depth of search) + output size)
- Aux. Space: O(max depth of search + output size)
