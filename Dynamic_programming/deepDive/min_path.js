// Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

// Note: You can only move either down or right at any point in time.

// Example 1:
// Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
// Output: 7
// Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

// Example 2
// Input: grid = [
//                 [1,2,3],
//                 [4,5,6]
// ]
// Output: 12

// Approach 1: (Exhaustive search): Find all paths and take the minimum.
// There is too many paths (exponential).

// Approach 2:
// F(i, j) = Min( F(i, j-1), F(i-1, j)) + grid[i,j]
// F( i<0, j<0 ) = Infinity
// F(0, 0) = grid[0][0]
var minPathSum = function (grid) {
  function dp(i, j) {
    if (i < 0 || j < 0) {
      return Infinity;
    }

    if (i === 0 && j === 0) {
      return grid[0][0];
    }

    return Math.min(dp(i - 1, j), dp(i, j - 1)) + grid[i][j];
  }

  const m = grid.length;
  const n = grid[0].length;
  return dp(m - 1, n - 1);
};

var minPathSum_memo = function (grid) {
  const m = grid.length;
  const n = grid[0].length;

  let memo = new Array(m).fill(null).map(() => new Array(n).fill(null));

  function dp(i, j) {
    if (i < 0 || j < 0) {
      return Infinity;
    }

    if (i === 0 && j === 0) {
      return grid[0][0];
    }

    if (memo[i][j] !== null) {
      return memo[i][j];
    }

    memo[i][j] = Math.min(dp(i - 1, j), dp(i, j - 1)) + grid[i][j];
    return memo[i][j];
  }

  return dp(m - 1, n - 1);
};

const grid = [
  [1, 3, 1],
  [1, 5, 1],
  [4, 2, 1],
];
console.log(minPathSum_memo(grid));

// in Tabulation :

var minPathSum_tabulation = function (grid) {
  const m = grid.length;
  const n = grid[0].length;

  // Create a 2D table to store minimum path sums
  const dp = new Array(m).fill(null).map(() => new Array(n).fill(0));

  // Initialize the top-left cell with its value
  dp[0][0] = grid[0][0];

  // Initialize the first column
  for (let i = 1; i < m; i++) {
    dp[i][0] = dp[i - 1][0] + grid[i][0];
  }

  // Initialize the first row
  for (let j = 1; j < n; j++) {
    dp[0][j] = dp[0][j - 1] + grid[0][j];
  }

  // Fill the rest of the table by choosing the minimum path
  for (let i = 1; i < m; i++) {
    for (let j = 1; j < n; j++) {
      dp[i][j] = Math.min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j];
    }
  }

  // The bottom-right cell contains the minimum path sum
  return dp[m - 1][n - 1];
};

const g = [
  [1, 3, 1],
  [1, 5, 1],
  [4, 2, 1],
];

console.log(minPathSum_tabulation(g)); // Output: 7
