""" 
Range Sum Query 2D - Immutable


Given a 2D matrix matrix, handle multiple queries of the following type:

    Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Implement the NumMatrix class:

    NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
    int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

You must design an algorithm where sumRegion works on O(1) time complexity.

 

Example 1:

Input
["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
[[[[3, 0, 1, 4, 2], 
   [5, 6, 3, 2, 1],
   [1, 2, 0, 1, 5],
   [4, 1, 0, 1, 7],
   [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
Output
[null, 8, 11, 12]

Explanation
NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)


"""

# explanation:
# https://leetcode.com/problems/range-sum-query-2d-immutable/solutions/2104244/python-easy-with-explanation/


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.dp = [[0]*(len(matrix[0])+1) for _ in range(len(matrix)+1)]

        for r in range(len(self.dp)-1):
            for c in range(len(self.dp[0])-1):
                self.dp[r+1][c+1] = self.matrix[r][c] + self.dp[r +
                                                                1][c] + self.dp[r][c+1] - self.dp[r][c]

    def sumRegion(self, row1, col1, row2, col2):
        return self.dp[row2+1][col2+1] - self.dp[row1][col2+1] - self.dp[row2+1][col1] + self.dp[row1][col1]


matrix = [[3, 0, 1, 4, 2],
          [5, 6, 3, 2, 1],
          [1, 2, 0, 1, 5],
          [4, 1, 0, 1, 7],
          [1, 0, 3, 0, 5]]

obj = Matrix(matrix)
result = obj.sumRegion(2, 1, 4, 3)
print(result)

result = obj.sumRegion(1, 1, 2, 2)
print(result)

result = obj.sumRegion(1, 2, 2, 4)
print(result)
