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

You can assume that the matrix is at least 1-by-1 and that the
given center is in the matrix and is a 0 cell.

You can assume that the tree slice is connected (in a graph sense).

Time constraint: O(size of matrix)
Space constaint: O(size of matrix)

Example:

0
center: (0,0)

Output:
0

Example:

Input: 
-1  0  0 -1 -1
 0  0  0 -1  0
 0  0  0 -1  0
-1 -1  0  0  0

Center: (1,2)

-1  0  0 -1 -1
 0  0  x -1  0
 0  0  0 -1  0
-1 -1  0  0  0

-1  0  1 -1 -1
 0  1  0 -1  0
 0  0  1 -1  0
-1 -1  0  0  0

-1  2  1 -1 -1
 2  1  0 -1  0
 0  2  1 -1  0
-1 -1  2  0  0

-1  2  1 -1 -1
 2  1  0 -1  0
 3  2  1 -1  0
-1 -1  2  3  0

-1  2  1 -1 -1
 2  1  0 -1  0
 3  2  1 -1  0
-1 -1  2  3  4

-1  2  1 -1 -1
 2  1  0 -1  0
 3  2  1 -1  5
-1 -1  2  3  4

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

Center: (1,2)

-1  0  1 -1 -1
 0  1  2 -1  0
 0  0  1 -1  0
-1 -1  0  0  0


'''
'''
Sketch
  start at center
  draw the 1 ring: for each neighbor of center, if 0 store 1
  continue (draw 2 ring, 3 ring, etc.) until no growth


Note: each node is a coordinate pair in the matrix plus a ring number
create a queue
store (center,0) in the queue
while queue is not empty
  remove pair and ring_number from front of the queue
  process node: store ring_number at this pair in matrix
  add 0 neighbors of pair to end of the queue with ring_number+1
write 0 at center
'''
