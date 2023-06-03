/*
Number of Rectangle Islands
Given a rectangular matrix containing only the values “0” and “1”, where the values of “1” always appear in the form of a rectangular island and the islands are always separated row-wise and column-wise by at least one line of “0”s, count the number of islands in the given matrix. Note that the islands can diagonally adjacent.

Input: Matrix of elements with values either 0 or 1
Output: An integer which is the count of all rectangular islands

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

matrix = [
[1, 1, 0, 1],
[1, 1, 0, 1],
[0, 1, 1, 0],
[1, 1, 1, 0]]



if (matrix[row][col] == 1) {
  if ((row == 0 && col == 0)) {
    // top left corner
  }
  else if(row != 0 && col == 0 && matrix[row - 1][col] == 0)) {
   // top left corner
  }
  else if((row == 0 && col != 0 && matrix[row][col - 1])) {
   // top left corner
  } 
  else if (matrix[row - 1][col] == 0 && matrix[row][col - 1] == 0) {
    // top left corner
  }
}

if (matrix[row][col] === 1 &&
    (row - 1 < 0 || matrix[row - 1][col] === 0) &&
    (col - 1 < 0 || matrix[row][col - 1] === 0)
    )


function dfs(...) {
  result = []

  function helper(...) {
    // base case(s)

    // recursive case(s)
  }

  return helper()

  
  helper()
  return result
}

function bfs(...) {
  queue = []

  queue.push(...)
  while (i,j = queue.pop()) {
    // computation
    
    queue.add(matrix[i - 1][j])
    queue.add(matrix[i + 1][j])
    queue.add(matrix[i][j - 1])
    queue.add(matrix[i][j + 1])
  }
}

*/

function findNextRect(matrix, i, j) {
  for (let row = i; row < matrix.length; row++) {
    for (let col = j; col < matrix.length; col++) {
      if (
        matrix[row][col] === 1 &&
        (row - 1 < 0 || matrix[row - 1][col] === 0) &&
        (col - 1 < 0 || matrix[row][col - 1] === 0)
      ) {
        return [row, col];
      }
    }
  }

  return null;
}

function dfs(matrix, i, j) {
  function helper(matrix, i, j) {
    console.log(i, j);
    // Base case
    // if row and col are out of bound, or value is zero
    if (i >= matrix.length || j >= matrix[0].length || matrix[i][j] === 0) {
      return [i, j];
    }

    matrix[i][j] = 0;

    // Traverse down
    [new_row, temp] = helper(matrix, i + 1, j);
    // Traverse right
    [temp, new_col] = helper(matrix, i, j + 1);
    // Traverse up
    [new_row, temp] = helper(matrix, i - 1, j);
    // Traverse left
    [temp, new_col] = helper(matrix, i, j - 1);
    console.log(new_row, new_col);
    return [new_row, new_col];
  }

  return helper(matrix, i, j);
}

function rectangularIslands(matrix) {
  result = [];

  // Find top left coordinate for next rect
  let start = findNextRect(matrix, 0, 0);

  while (start != null) {
    let row = start[0];
    let col = start[1];

    // Find bottom right coordinate of this rect
    end = dfs(matrix, row, col);

    result.push([start, end]);

    if (row == matrix.length - 1) {
      col++;
    } else {
      row++;
    }
    coord = findNextRect(matrix, row, col);
  }
}

// [[[0,0],[1,1]], [[0,3],[1,3]], [[2,2],[3,2]]]
matrix = [
  [1, 1, 0, 1],
  [1, 1, 0, 1],
  [0, 0, 1, 0],
  [0, 0, 1, 0],
];

console.log(rectangularIslands(matrix));
