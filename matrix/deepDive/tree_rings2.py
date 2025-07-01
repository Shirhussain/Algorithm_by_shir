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

queue: [((1,1),1),((0,2),1),((1,3),1),((2,2),1)]

node: (1,2)
ring_value: 0


-1  0  1 -1 -1
 0  1  x -1  0
 0  0  1 -1  0
-1 -1  0  0  0

changed: true

ring: 1

changed: false

-1  2  1 -1 -1
 2  1  x -1  0
 0  2  1 -1  0
-1 -1  2  0  0

changed: true

ring: 2
changed: false
-1  2  1 -1 -1
 2  1  x -1  0
 3  2  1 -1  0
-1 -1  2  3  0
changed: true

ring: 3
changed: false
-1  2  1 -1 -1
 2  1  x -1  0
 3  2  1 -1  0
-1 -1  2  3  4
changed: true

ring: 4


-1  2  1 -1 -1
 2  1  x -1  0
 3  2  1 -1  5
-1 -1  2  3  4


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

Input: (1,2) center
-1  0  1 -1 -1
 0  0  0 -1  0
 0  0  0 -1  0
-1 -1  0  0  0


'''

'''
Pseudocode

place a -1 at the center
set changed to false
try to change all of the 0's that are neighbors of the center to 1, and
  set changed to true if any 1's were written
set ring to 1
while the last step changed an element : number of tree rings
  set changed to false
  for each element of the array : O(size of matrix)
    if current element has value ring
      for each neighbor of element
        if neighbor is in the matrix and has value 0
          set neighbor to ring+1
          set changed to true
  increment ring
place a 0 at the center



place a -1 at the center
create an empty queue
for each neighbor of center
  if neighbor is in matrix and has value 0
    write value 1 in neighbor
    add neighbor to queue
while queue is not empty : O(size of matrix)
  remove node from front of queue
  get ring value for this node
  for each neighbor of node
    if neighbor is in the matrix and has value 0
      set neighbor value to ring value + 1
      add neighbor to queue
place a 0 at the center


create an empty queue
add center node to queue
while queue is not empty : O(size of matrix)
  remove node from front of queue
  get ring value for this node
  if ring value is 0 (or if node is center)
    write -1 at this node
  for each neighbor of node
    if neighbor is in the matrix and has value 0
      set neighbor value to ring value + 1
      add neighbor to queue
place a 0 at the center

'''