// F(n) = Min ( F(n-1) , F(n-2) , F(n-5) ) + 1
function coinChange(coins, amount) {
  if (amount === 0) {
    return 0;
  }

  if (amount < 0) {
    return -1;
  }

  let result = Infinity;
  for (let coin of coins) {
    let n = coinChange(coins, amount - coin);

    if (n >= 0) {
      result = Math.min(result, n);
    }
  }

  return result < Infinity ? 1 + result : -1;
}

function coinChangeTabulation(coins, amount) {
  let dp = new Array(amount + 1).fill(Infinity);
  dp[0] = 0;

  for (i = 1; i <= amount; i++) {
    for (let coin of coins) {
      if (i - coin >= 0) {
        dp[i] = Math.min(dp[i], dp[i - coin] + 1);
      }
    }
  }

  return dp[amount] === Infinity ? -1 : dp[amount];
}

const coins2 = [2, 5, 10];
console.log(coinChangeTabulation(coins2, 1));
console.log(coinChangeTabulation(coins2, 3));
console.log(coinChangeTabulation(coins2, 27));
