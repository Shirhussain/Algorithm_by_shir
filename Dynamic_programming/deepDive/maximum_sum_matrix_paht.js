/*
Given an n*m matrix, the task is to find the maximum sum of elements of cells 
starting from  (0, 0) to (n-1, m-1). You can only move right, down,
or diagonally right-down.

Find the maximum sum of elements satisfying the allowed moves.


Input:
mat[][] = {{100, -350, -200},
           {-100, -300, 700}}
Output: 500
100 -> -300 -> 700


Input:
mat[][] = {{500, 100, 230},
           {1000, 300, 100},
           {200, 1000, 200}}
Output: 3000
500 -> 1000 -> 300 -> 1000 -> 200
*/

let dp = new Array()

function maxSumPath(i, j, matrix) {
  n = matrix.length
  m = matrix[0].length
  if (i == n - 1 && j = m) {
    return matrix[i][j]
  }
  
  let sum = 0
  
  if(dp[i][j]) {
    return dp[i][j]
  }
  
  if (i < n - 1 && j < m - 1) {
    sum = Math.max(Math.max(maxSumPath(i, j + 1, matrix), maxSumPath(i + 1, j, matrix)), maxSumPath(i + 1, j + 1, matrix)) + matrix[i][j]
  }
  else if (i == n - 1) {
    sum = maxSumPath(i, j + 1, matrix) + matrix[i][j]
  }
  else {
    sum = maxSumPath(i + 1, j, matrix) + matrix[i][j]
  }
  
  dp[i][j] = sum
  
  return sum
}

maxSumPath(0, 0, {{500, 100, 230}, {1000, 300, 100}, {200, 1000, 200}})

/*
 * Recursive:
 * Time: O(3^n*m)
 * Space: O(n+m)
 * 
 * Memo:
 * Time: O(n*m)
 * Space: O(n+m) + O(n*m) => O(n*m)
 * */

/*

this is how you do tabulation : 
first base case :
    - first row and first column
    - then for other cells : 
        - sum = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + matrix[i][j]


dp = [[0] * m for _ in range(n)]

for i in range(1, n):
    dp[i][0] = dp[i-1][0] + matrix[i][0]
for j in range(1, m):
    dp[0][j] = dp[0][j-1] + matrix[0][j]
for i in range(1, n):
    for j in range(1, m):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + matrix[i][j]




{{500, 100, 230},
{1000, 300, 100},
{200, 1000, 200}}

Maximum sum up to that cell
{{500, 600, 830},
 {1500, 1800, 1900}
 {1700, 2800, 3000}}





*/



