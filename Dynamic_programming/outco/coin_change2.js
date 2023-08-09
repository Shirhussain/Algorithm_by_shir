// Given different coins and a total amount of money, find minimum number of coins to make up that amount.
// We can have infinite number of each coin.

// Input: coins = [1, 2, 5], amount = 11
// Output: 3
// Explanation: 11 = 5 + 5 + 1
// Another example: 11 = 5 + 2 + 2 +1 +1
// Another example: 11 = 1+1+1+1+ … +1 (11 times)

// ALWAYS START FROM A TREE!
// Three questoins
// 1. What is the root?
//    F(n)
// 2. How do I generate the children of a node?
//   F(n) = Min[ F(n-c[0]), F(n-c[1]), F(n-c[2]), ... ] + 1
// 3. Leaves (AKA base cases)
//    F(k<0) = -1 // Invalid
//    F(0) = 0
function coinChange(coins, n) {
  // Base cases
  if (n == 0) {
    return 0;
  }

  if (n < 0) {
    return -1;
  }

  // recursive relationship
  let min = Infinity;
  for (let coin of coins) {
    let r = coinChange(coins, n - coin);
    if (r >= 0) {
      min = Math.min(min, r);
    }
  }

  if (min == Infinity) {
    return -1;
  }

  return min + 1;
}

let memo = {};
function coinChangeMemo(coins, n) {
  // Base cases
  if (n == 0) {
    return 0;
  }

  if (n < 0) {
    return -1;
  }

  if (n in memo) {
    return memo[n];
  }

  // recursive relationship
  let min = Infinity;
  for (let coin of coins) {
    let r = coinChangeMemo(coins, n - coin);
    if (r >= 0) {
      min = Math.min(min, r);
    }
  }

  if (min == Infinity) {
    memo[n] = -1;
  } else {
    memo[n] = min + 1;
  }
  return memo[n];
}

function coinChangeTabulation(coins, n) {
  const dp = new Array(n + 1).fill(Infinity); // return dp[n]

  // Base cases
  dp[0] = 0;

  for (let i = 1; i <= n; i++) {
    for (let coin of coins) {
      if (i - coin >= 0) {
        dp[i] = Math.min(dp[i], dp[i - coin]) + 1;
      }
    }
  }
  return dp[n] === Infinity ? -1 : dp[n];
}

// let coins = [1, 2, 5];
// console.log(coinChangeMemo(coins, 11)); // Output: 3

//  coins = [2, 4];
// console.log(coinChangeMemo(coins, 100));

let coins = [2, 4];
console.log(coinChangeTabulation(coins, 100));

coins = [1, 2, 5];
console.log(coinChangeTabulation(coins, 11)); // Output: 3
