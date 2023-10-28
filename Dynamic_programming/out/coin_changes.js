/*
Template for memoization
std::unordered_map<int, int> memo;
int Fibonacci(int n) {
 // Take care of base cases
 if (n == 0 || n == 1) {
   return 1;
 }

 // Check the memo, if it a hit, return from memo
 if (memo.count(n) > 0) {
   return memo[n];
 } else {
  // Otherwise, call the recusive function and update the memo
   memo[n] = Fibonacci(n - 1) + Fibonacci(n - 2);
 }
 return memo[n];
}
*/

/*
  Example 1: Coin Changing Problem
Given different coins and a total amount of money, find minimum number of coins to make up that amount.
We can have infinite number of each coin.

Example:
Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Another example: 11 = 5 + 2 + 2 +1 +1
Another example: 11 = 1+1+1+1+ … +1 (11 times)


*/

/*
Greedy approach:
Take the largest value coin that is less than or equl to the amount

// const coins4 = [1, 3, 4];
// const amount = 6;
Greedy suggests this [4, 1, 1] but the optimal answer is [3,3].


Recursion?
- Always start from a tree!
  */
/*
for coins [0,...m]
F(n) = Min(F(n-ci)) + 1   (for coins i = 0 to m)
F(0) =0
F(i<0) = -1
*/

// function coinChange(coins, amount){

//   if(amount == 0){
//     return 0;
//   }

//   if(amount < 0){
//     return -1;
//   }

//   let result = Infinity;
//   for (let coin of coins){
//     let r = coinChange(coins, amount - coin);
//     if(r >=0 ){
//       result = Math.min(result, r);
//     }
//   }

//   return result + 1;
// }

function coinChangeMemo(coins, amount) {
  let memo = new Map();
  return coinChange(amount);

  function coinChange(amountHelper) {
    if (amountHelper == 0) {
      return 0;
    }

    if (amountHelper < 0) {
      return -1;
    }

    if (memo.has(amountHelper)) {
      return memo.get(amountHelper);
    }

    let result = Infinity;
    for (let coin of coins) {
      let r = coinChange(amountHelper - coin);
      if (r >= 0) {
        result = Math.min(result, r);
      }
    }

    // All children retrun a negative value
    if (result === Infinity) {
      return -1;
    }

    memo.set(amountHelper, result + 1);
    return result + 1;
  }
}

let coins = [1, 2, 5];
console.log(coinChangeMemo(coins, 11)); // Output: 3

const coins4 = [1, 3, 4];
const amount = 6;
console.log(coinChangeMemo(coins4, amount)); // Output: 2
