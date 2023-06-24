/*

// We define:
// Rules of the climb stairs:
// You are climbing a staircase. Each time you can either climb 1 or 2 or 3
// steps. It takes n steps to reach the top. Your function takes n as input.

// If there are 0 stairs, return 0. For negative input, please
// return -1.
// For example, if the stairs number is 3, (n = 3), it should have 4 ways to the
// top:

// 1 + 1 + 1
// 1 + 2
// 2 + 1
// 3
*/

// A mapping from the intput of the function to the output
// f(n) ==> Map <int, int> --> or use a one dimentional array if n is non-negative integer: table[key] = value
// e.g. knapsack: f(n, m) ==> Map < (int, int), int> or use a two dimentional array table[m,n] = value
// e.g. knapsack: f(n, m, q) ==> Map < (int, int, int), int>

function climbStairsTabulation(n) {
  // Define your table
  let d = new Array(n + 1);

  // Initialize the table
  for (let i = 0; i <= n; i++) {
    d[i] = 0;
  }

  // Continue initialization with your base case
  d[0] = 0;
  d[1] = 1;
  d[2] = 2;
  d[3] = 4;

  // Write the recursion relationship in a loop (from after your base cases)
  for (let i = 4; i <= n; i++) {
    // Convert the recursion to table loopup!
    // F(n) = F(n-1) + F(n-2) + F(n-3)
    d[i] = d[i - 1] + d[i - 2] + d[i - 3];
  }

  return d[n];
}

console.log(
  "Number of ways to climb the stairs (n = 3):",
  climbStairsTabulation(3)
);
console.log(
  "Number of ways to climb the stairs (n = 4):",
  climbStairsTabulation(4)
);
