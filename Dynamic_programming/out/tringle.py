'''
                    7
                  3   8
                8   1    0
              2   7    4    4
            4   5   2    6    5

[
[7],
[3, 8],
[8, 1, 0],
[2, 7, 4, 4],
[4, 5, 2, 6, 5]
]

If depth of the tree is d
then number of nodes N in the tree is d(d+1)/2 ~ d^2.


Given a number triangle like the one above, calculate the hihest sum of numbers passed on a route that starts at the top and ends somewhere on the bottom. Each step can go either diagonally down to the left of diagonally down to the right.

Brute force:

let triangle be the input array
i represents row in triangle,
j represents column

def max_sum(i,j):
  if i >= length of triangle 
    return 0
  return triangle[i][j] +
         max (max_sum(i+1, j), max_sum(i+1, j+1))

print(max_sum(0,0))

N = number of nodes in the triangle
depth is sqrt(N)

Brute force run time: O(2^sqrt(N))


              7
         3         8
      8      1    0
  2,7   7,12    4    4
4,4   5,5  2,2    6    5

DP solution (memoization)

Run time is O(N)


DP Solution: bottom up

              7
            3   8
          8   1    0
        2   7    4    4
      4   5   2    6    5

      
0
1
2  20  13   10
3  7   12   10   10
4  20   13   10   10    5

initialize last row of table with last row of triangle
for each row of table from next to last back to the first
   for each column of this row
      set (row, column) of table to 
         triange[row][column] + 
         max table[row+1][column], table[row+1][column+1]
print table[0][0]

'''


triangle = [
    [7],
    [3, 8],
    [8, 1, 0],
    [2, 7, 4, 4],
    [4, 5, 2, 6, 5]
]

'''
cache = { }

def max_sum(i,j):
  if i >= len(triangle):
    return 0
  if (i,j) in cache:
    return cache[(i,j)]
  ans = (triangle[i][j] +
         max (max_sum(i+1, j), max_sum(i+1, j+1)))
  cache[(i,j)] = ans
  return ans

print(max_sum(0,0))
'''

table = []
N = len(triangle)
for row in range(len(triangle)):
    table.append([0 for j in range(row+1)])
table[N-1] = triangle[N-1]
row = N-2
while row >= 0:
    for column in range(row+1):
        table[row][column] = (triangle[row][column] +
                              max(table[row+1][column],
                                  table[row+1][column+1]))
    row -= 1
print(table)
'''
initialize last row of table with last row of triangle
for each row of table from next to last back to the first
   for each column of this row
      set (row, column) of table to 
         triange[row][column] + 
         max table[row+1][column], table[row+1][column+1]
print table[0][0]
'''
