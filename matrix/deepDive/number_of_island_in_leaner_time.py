'''
Given a 0/1 matrix, return the number of rectangular 
"islands" of 1's.

Input: [[1, 1, 0, 1],    
        [1, 1, 0, 1],    
        [0, 0, 1, 0],    
        [0, 0, 1, 0]]

Output: 3

Input: [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 0, 1],
        [0, 0, 0, 1]]

Output: 2

Input: [[1, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 1],
        [0, 0, 0, 1]]

Output: 3

'''

'''
How many islands in an empty input? [[]]
0

Time: O(N*M)
Aux space: O(1)
Not allowed to modify the input array

Every island is rectangular.
'''
'''
Diagram

             j
i [[1, 1, 0, 1],    
   [1, 1, 0, 1],    
   [0, 0, 1, 0],    
   [0, 0, 1, 0]]

count: 1

'''


'''

define islands(matrix):
   set count to 0
   for i from 0 through number of rows-1
      for j from 0 through number of cols - 1
         if matrix[i][j+1] is not a 1 (either b/c outside matrix or 0) and
            matrix[i+1][j] is not a 1 then
              increment count
   return count

'''


def islands(matrix):
    if not matrix or not matrix[0]:
        return 0

    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # Check if current cell is 1
            if matrix[i][j] == 1:
                # Check if it's a top-left corner of a rectangle, it means that the cell is not connected to any other 1s
                # it means this is the first cell which is 1 and it is not connected to any other 1s before that
                if (j == 0 or matrix[i][j-1] == 0) and (i == 0 or matrix[i-1][j] == 0):
                    count += 1
    return count


matrix = [[1, 1, 0, 1],
          [1, 1, 0, 1],
          [0, 0, 1, 0],
          [0, 0, 1, 0]]

print(islands(matrix))
