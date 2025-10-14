'''
1. Understand
https://leetcode.com/problems/rotate-image/

You are given an n x n 2D int matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Input:
matrix = [
[1,2,3],
[4,5,6],
[7,8,9]]
Output: [
[7,4,1],
[8,5,2],
[9,6,3]]

1 <= n <= 20

'''
'''
2. Diagram (linear space)


      [7,4,1],
      [8,5,2],
      [9,6,3]]

list: [1 2 3]

Input:
      [5,1,9,11],
      [2,4,8,10],
      [13,3,6,7],
      [15,14,12,16]]

list: 5 1 9 11
       v        v
    >  [15,13,2,5],
       [14,4,8,1],
       [12,3,6,9],
>      [16,7,10,11]]


Output:

      [15,13,2,5],
      [14,3,4,1],
      [12,6,8,9],
      [16,7,10,11]]


Input:
      [5,1,9,11],
      [2,4,8,10],
      [13,3,6,7],
      [15,14,12,16]

temp: 5

      [15,13,2,5],
      [14,4,8,1],
      [12,3,6,9],
      [16,7,10,11]



'''
'''
3. Pseudocode

start_row = 0
start_col = 0
n = number of rows
final_row = start_row + (n-1)
final_col = start_col + (n-1)

while n > 0

      // process one "ring" of the matrix
      for offset from 0 thru n-2
               
            set temp to matrix[start_row][start_col+offset]
            set matrix[start_row][start_col+offset] to matrix[final_row-offset][start_col]
            set matrix[final_row-offset][start_col] to matrix[final_row][final_col-offset]
            set matrix[final_row][final_col-offset] to matrix[start_row+offset][final_col]
            set matrix[start_row+offset][final_col] to temp
      
      start_row += 1
      start_col += 1
      n -= 2
      final_row = start_row + (n-1)
      final_col = start_col + (n-1)

Input:
            [5,1,9,11],      15  13       5
            [2,4,8,10],                   1
            [13,3,6,7],      12
            [15,14,12,16]    16     10   11
start_row = 0   start_col = 0  n = 4  final_row = 3 final_col = 3  offset = 1  temp: 1

'''


# another solution is :
"""
Input:
      [5,1,9,11],
      [2,4,8,10],
      [13,3,6,7],
      [15,14,12,16]]

Output:
      [15,13,2,5],
      [14,3,4,1],
      [12,6,8,9],
      [16,7,10,11]]

Transpose:

      [5,2,13, 15],
      [1,4,3,  14],
      [9,8,  6 ,12],
      [11,10,7,16]

Reverse each row:

      [15,13,2,5],
      [14,4,8,1],
      [12,3,6,9],
      [16,7,10,11]
    """


matrix = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]]


def rotate_image(matrix):
    # Transpose the matrix
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(len(matrix)):
        matrix[i].reverse()
    return matrix


print(rotate_image(matrix))
