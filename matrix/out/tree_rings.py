'''
You are given an image of a "slice" of a physical tree
represented by 0's in an integer matrix. Areas not covered by
the tree are represented by -1's.  Given the coordinates
of the center of the tree, label the "rings" of the tree.
The first ring consists of those matrix elements adjacent
(left, right, up, down) to the center.  These cells should
be assigned the value 1.  The second ring
consists of those cells that are not in the center or first
ring that are adjacent to first-ring cells.  These cells
should be assigned the value 2. And so on. Change the
matrix in place.

Example:

Input: 
-1  0  0 -1 -1
 0  0  0 -1  0
 0  0  0 -1  0
-1 -1  0  0  0

Center: (1,2)

Output: 
-1  2  1 -1 -1
 2  1  0 -1  6
 3  2  1 -1  5
-1 -1  2  3  4

'''

'''
Understanding

Constraints:
Time: O(size of the matrix)
Space: O(size of matrix)

Can we assume that we are given a non-empty tree? Yes
Is the tree always "connected"? Yes.
Can we assume that the "center" is in the tree? Yes.
Can we assume that the center is a 0?  Yes.


Diagramming

Input: 
-1  0  1 -1 -1
 0  0  0 -1  0
 0  0  0 -1  0
-1 -1  0  0  0

queue:  ((1,1),1), ((2,2), 1), ((0,1),2)
visited: (0,2), (1,1), (2,2), (0,1)
row: 0
col: 2
level: 1

                ((1,2),0)
    ((0,2),1)   ((1,1),1)   ((2,2), 1)
    ((0,1),2)
'''

'''
Pseudocode

def bfs((i,j)):
  create an empty queue
  create a visited set
  add ((i,j), 0) to the queue
  while queue is not empty
    remove ((row, col), level) from the queue
    process((row,col), level): write level in matrix[row][col]
    for each neightbor of (row, col)
      if neighbor is in bounds and neighbor value is not -1 and neighbor not in visited
        add (neighbor,level+1) to queue
        add neighbor to visited



'''
