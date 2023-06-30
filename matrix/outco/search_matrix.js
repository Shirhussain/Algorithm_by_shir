/*
Search a 2D matrix
Write an efficient algorithm that searches for a value in an M x N matrix. This matrix has the following properties:

Integers in each row are sorted from left to right
The first integer of each row is greater than the last integer of the previous row.
Input: Matrix of Integers, Target Integer
Output: Boolean
Example
Example 1:
Input:

matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

[1,3,5,7,10,11,16,20,23,30,34,50]

target = 3
Output: True

Example 2:
Input:

matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

target = 13
Output: False

for (i = 0; i < matrix.length; i++) {
  for (j =0; j < matrix[0].length; j++) {
    if (matrix[i][j] == val) {
      return true
    }
  }
}

return false

Time: O(ij)

Whiteboard
---
Understand
What is max size of matrix?
Fit in memory

Diagram

target = 3

[1,3,5,7,10,11,16,20,23,30,34,50]

matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

matrix = [
  [1,   2,  3,  4], // 1
  [1,   2,  3,  4], // 2 [2,2]
  [1,   2,  3,  4], // 3
]

matrix = [
  [1,   2,  3,  4], 
  [5,   6,  7,  8], 
  [9,   10,  11, 12], 
]

beginning = 1
end = 2

midpoint = beginning + floor((end - beginning) / 2) => 2
[floor(midpoint / num of rows)][midpoint % num of cols]
[0][2]



Pseudocode

function searchMatrix(matrix, target) {
  // Edge cases

  numRows = matrix.length
  numCols = matrix[0].length

  beg = 0
  end = numRows * numCols - 1

  while (beg <= end) {
    midpoint = beg + Math.floor((end - beg) / 2)
    candidate = matrix[Math.floor(midpoint / numRows)][midpoint % numCols]

    if (target === candidate) {
      return true
    }
    else if (candidate < target) {
      beg = midpoint + 1
    }
    else {
      end = midpoint - 1
    }
  }

  return false
}

Code

*/

function searchMatrix(matrix, target) {
  // Edge cases

  numRows = matrix.length;
  numCols = matrix[0].length;

  beg = 0;
  end = numRows * numCols - 1;

  while (beg <= end) {
    midpoint = beg + Math.floor((end - beg) / 2);

    candidate = matrix[Math.floor(midpoint / numRows) - 1][midpoint % numCols];
    console.log(candidate);

    if (target === candidate) {
      return true;
    } else if (candidate < target) {
      beg = midpoint + 1;
    } else {
      end = midpoint - 1;
    }
  }

  return false;
}

matrix = [
  [1, 3, 5, 7],
  [10, 11, 16, 20],
  [23, 30, 34, 50],
];

console.log(searchMatrix(matrix, 100));

// Time: O(log(nm))
// Space: O(1)
