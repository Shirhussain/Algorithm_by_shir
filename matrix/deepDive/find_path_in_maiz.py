'''
Given an m-by-n matrix that contains 0's and 1's and represents a maze, with 
1's being the walls, find any path from (0,0) to (m-1, n-1) or return "none"
if no such path exists.
'''
'''

00111111
10000001
10000000
11111110

4-by-8 matrix

output: (0,0), (0,1), (1,1), ..., (2,7), (3,7)

Matrix will be at least 2-by-2
Upper left and lower right corners will both be 0

Constraints: Run time exponential and space O(mn)

'''
'''
Diagram:

00001111
10100001
10100000
11111110

(i,j): (0,0)
visited: (0,0), (0,1), (0,2)]

                                 (0,0), [(0,0)]
                                 (0,1), [(0,0), (0,1)]
                   ...
  ((2,1), [(0,0), (0,1), (1,1), (2.1)])  ((0,2), [(0,0), (0,1), (0,2)]
                            
'''
'''
Pseudocode

def maze(matrix):
  create an empty output variable
  store "none" in this variable
  create a visited list containing (0,0)
  def dfs((i,j), path)
    if (i,j) is outside the matrix or matrix[i][j] is a 1 or (i,j) is in visited set
      return false
    if (i,j) is the lower right corner
      store a copy of path in output variable
      return true
    for each neighbor
      add neighbor to path
      add neighbor to visited set
      if dfs(neighbor, path) return true
      remove neighbor from path
      # remove neighbor from visited set
    return false
    
  dfs((0,0), [(0,0)])

  return output variable

'''
