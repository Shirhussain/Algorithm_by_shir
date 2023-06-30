/*
Matrix Spiral
Given an (MxN) matrix of integers, return an array in spiral order.

Input: Array of integers
Output: Array of integers
Example
Input: [[1,2,3],
        [4,5,6],
        [7,8,9]]

Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]

[[]]

Input: [[1]
        [2]]

Output: [1,2]

Whiteboarding
---
Understand
Time/Space complexity constraints?
Make it optimal

Edge cases?
What can you think of as edge cases?


Diagram

       [[1,2,3],
        [4,5,6],
        [7,8,9]]

        [1,2,3,6,9,8,7,4,5]

xMin = 1
xMax = 1
yMin = 1
yMax = 1

Pseudocode

function matrixSpiral(matrix) {
  if (matrix.length === 0) {
    return []
  }

  xMin = 0
  yMin = 0

  xMax = matrix[0].length - 1
  yMax = matrix.length - 1

  result = []

  while(xMin <= xMax && yMin <= yMax) {
    // Traverse right
    for (i = xMin; i <= xMax; i++) {
      result.push(matrix[yMin][i])
    }
    yMin++
    

    // Traverse down
    for (i = yMin; i <= yMax; i++) {
      result.push(matrix[i][xMax])
    }
    xMax--

    // Traverse left
    for (i = xMax; i >= xMin; i--) {
      result.push(matrix[yMax][i])
    }
    yMax--

    // Traverse up
    for (i = yMax; i >= yMin; i--) {
      result.push(matrix[i][xMin])
    }
    
    xMin++
  
  }

  return result

}

Code

*/

function matrixSpiral(matrix) {
  if (matrix.length === 0) {
    return [];
  }

  xMin = 0;
  yMin = 0;

  xMax = matrix[0].length - 1;
  yMax = matrix.length - 1;

  result = [];

  while (xMin <= xMax && yMin <= yMax) {
    // Traverse right
    for (i = xMin; i <= xMax; i++) {
      result.push(matrix[yMin][i]);
    }
    yMin++;

    // Traverse down
    if (xMin <= xMax && yMin <= yMax) {
      for (i = yMin; i <= yMax; i++) {
        result.push(matrix[i][xMax]);
      }
      xMax--;
    }

    // Traverse left
    if (xMin <= xMax && yMin <= yMax) {
      for (i = xMax; i >= xMin; i--) {
        result.push(matrix[yMax][i]);
      }
      yMax--;
    }

    // Traverse up
    if (xMin <= xMax && yMin <= yMax) {
      for (i = yMax; i >= yMin; i--) {
        result.push(matrix[i][xMin]);
      }

      xMin++;
    }
  }

  return result;
}

function matrixSpiralRecursive(matrix) {
  if (matrix.length === 0) {
    return [];
  }

  xMin = 0;
  yMin = 0;

  xMax = matrix[0].length - 1;
  yMax = matrix.length - 1;

  result = [];

  function spiralHelper(xMin, xMax, yMin, yMax) {
    // Base case(s)
    if (xMin > xMax || yMin > yMax) {
      return;
    }

    // Traverse right
    for (i = xMin; i <= xMax; i++) {
      result.push(matrix[yMin][i]);
    }
    yMin++;

    // Traverse down
    if (xMin <= xMax && yMin <= yMax) {
      for (i = yMin; i <= yMax; i++) {
        result.push(matrix[i][xMax]);
      }
      xMax--;
    }

    // Traverse left
    if (xMin <= xMax && yMin <= yMax) {
      for (i = xMax; i >= xMin; i--) {
        result.push(matrix[yMax][i]);
      }
      yMax--;
    }

    // Traverse up
    if (xMin <= xMax && yMin <= yMax) {
      for (i = yMax; i >= yMin; i--) {
        result.push(matrix[i][xMin]);
      }

      xMin++;
    }

    // Recursive case(s)
    spiralHelper(xMin, xMax, yMin, yMax);
  }

  spiralHelper(xMin, xMax, yMin, yMax);
  return result;
}

matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12],
];

console.log(matrixSpiral(matrix));
