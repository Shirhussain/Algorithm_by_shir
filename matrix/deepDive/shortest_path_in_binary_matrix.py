'''
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).


[[1,1,1],
 [1,1,1,
 [1,1,0]]

 
'''
'''


                 (0,0),0
                   
    (1,0),1       (1,1),1          (0,1),1
       X            X       (1,2),2      (0,2),2



visited: (0,0), (0,1), (0,2), (1,2), (2,2)
queue: ((1,2),2), ((2,2), 3)
node: (0,2)
path_length: 2
'''
'''

initialize visited to empty set
create an empty queue

if upper left corner is a 1, then return -1

push ((0,0),0) onto queue
add (0,0) to visited set

while queue is not empty

  pop (node, path_length) from queue
  
  if node is bottom right corner then return path_length
  
  for each neighbor
  
    if neighbor is in boundaries, a 0, and is not in visited set 
      push (neighbor, path_length+1) onto queue
      add neighbor to visited set
    
return -1
    

'''
