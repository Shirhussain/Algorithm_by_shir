// 200. Number of Islands
// Medium

// Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

// An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

// Example 1:

// Input: grid = [
//   ["1","1","1","1","0"],
//   ["1","1","0","1","0"],
//   ["1","1","0","0","0"],
//   ["0","0","0","0","0"]
// ]
// Output: 1
// Example 2:

// Input: grid = [
//   ["1","1","0","0","0"],
//   ["1","1","0","0","0"],
//   ["0","0","1","0","0"],
//   ["0","0","0","1","1"]
// ]
// Output: 3

// Constraints:

// m == grid.length
// n == grid[i].length
// 1 <= m, n <= 300
// grid[i][j] is '0' or '1'.

/*
Approach: go through all elements, 
  if we find 1, we run DFS
  All 1's that are connected, we change to 0 (AKA mark as visited)
  Each time we begin DFS, we increment a cou nter.
*/
function numIslands(maze) {
  let result = 0;
  let di = [1, 0, -1, 0];
  let dj = [0, 1, 0, -1];
  function dfs(row, col) {
    // Mark visited
    maze[row][col] = "0";

    for (let k = 0; k < di.length; k++) {
      let newRow = row + di[k];
      let newCol = col + dj[k];

      // Rejects out of bound
      if (
        newRow < 0 ||
        newCol < 0 ||
        newRow >= maze.length ||
        newCol >= maze[0].length
      ) {
        continue;
      }

      // Reject the visited or water
      if (maze[newRow][newCol] === "0") {
        continue;
      }

      dfs(newRow, newCol);
    }
  }

  for (let i = 0; i < maze.length; i++) {
    for (let j = 0; j < maze[0].length; j++) {
      if (maze[i][j] === "1") {
        dfs(i, j);
        result++;
      }
    }
  }
  return result;
}

// Runtime Complexity: O(m*n)

const maze1 = [
  ["1", "1", "0", "0", "0"],
  ["1", "1", "0", "0", "0"],
  ["0", "0", "1", "0", "0"],
  ["0", "0", "0", "1", "1"],
];

console.log(numIslands(maze1));
