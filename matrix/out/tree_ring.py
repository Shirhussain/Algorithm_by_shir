'''
You are given an image of a "slice" of a physical tree
represented by 0's in an integer matrix. Areas not covered by
the tree are represented by -1's.  Given the coordinates
of the center of the tree, label the "rings" of the tree.
The first ring consists of those matrix elements adjacent
(left, right, up, down) to the center.  These cells should
be assigned the value 1.  The second ring
consists of those cells that are not in the center or first
right that are adjacent ot first-ring cells.  These cells
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

Is the tree always "connected"? Yes.
Can we assume that the "center" is in the tree? Yes.


Diagramming

Input: 
-1  0  1 -1 -1
 0  1  -2 -1  0
 0  0  0 -1  0
-1 -1  0  0  0

queue:  ((2,2), 1), ((0,1), 2), ((0,1), 2), ((1,0), 2), ((2,1), 2)
node: (1,1)
ring: 1


'''

'''
Pseudocode

tree_rings(matrix, center):

  create an empty queue
  store -2 at matrix center
  enqueue (center, 0) in queue
  while queue is not empty
    dequeue node, ring
    for each neighbor
      if neighbor is in the matrix and is a 0
        enqueue (neighbor, ring+1)
    if node is not center
      set matrix[node] to ring

  store 0 at matrix center

'''
