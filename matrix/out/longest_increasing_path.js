/*
Given an integer matrix, find the length of the longest increasing path.

Given each cell, you can either move to four directions, left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).


Example 1:
Input:

nums = [
[9, 9, 4],
[6, 6, 8],
[2, 10, 1]
]

Output: 4

Example 2:
Input:

nums = [
[3, 4, 5],
[3, 2, 6],
[2, 2, 1]
]

Output: 4

Approach 1: exhaustive search: Check all possible paths, find the increasing ones, return the longest.


Approach 2:
 if m[i][j] < m[i-1][j]:  top = LIP(i-1,j) , otherwise 0
 if m[i][j] < m[i+1][j]:  bottom = LIP(i+1,j) ,  otherwise 0
 if m[i][j] < m[i][j-1]:  left = LIP(i,j-1) ,  otherwise 0
 if m[i][j] < m[i][j+1]:  right = LIP(i,j+1), otherwise 0

 LIP(i,j) = max(top, bottom, left, right) + 1
 
*/
function longestIncreasingPath(maze) {
  const m = maze.length;
  const n = maze[0].length; // assume maze is non-empty

  function OutOfBount(i, j) {
    if (i < 0 || i >= m) {
      return true;
    }

    if (j < 0 || j >= n) {
      return true;
    }

    return false;
  }

  function LIP(i, j) {

    let top = (OutOfBount(i - 1, j) || maze[i][j] >= maze[i - 1][j]) ? 0 : LIP(i - 1, j);
    let down = (OutOfBount(i + 1, j) || maze[i][j] >= maze[i + 1][j]) ? 0 : LIP(i + 1, j);
    let left = (OutOfBount(i, j - 1) || maze[i][j] >= maze[i][j - 1]) ? 0 : LIP(i, j - 1);
    let right = (OutOfBount(i, j + 1) || maze[i][j] >= maze[i][j + 1]) ? 0 : LIP(i, j + 1);

    return 1 + Math.max(left, right, top, down);
  }

  let max = 0;
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      max = Math.max(max, LIP(i, j));
    }
  }
  return max;
}

const maze1 = [
  [3, 4, 5],
  [3, 2, 6],
  [2, 2, 1]
];


console.log(longestIncreasingPath(maze1));

const maze2 = [
  [3, 4, 5],
  [3, 2, 6],
  [2, 2, 1]
];

console.log(longestIncreasingPath(maze2));

// It can be further optimize by Dynamic programming 
