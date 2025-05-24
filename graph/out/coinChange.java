import java.util.HashMap;
import java.util.Map;
class Solution {
    public int coinChange(int[] coins, int amount) {

        return dpHelper(coins, amount)
        // Map<Integer, Integer> memo = new HashMap<>();
        // return helper(coins, amount, memo);

    }

    private int[] dpHelper(coins, amount){
        int [] dp = new int[amount+1]

        Arrays.fill(dp, Integer.MAX_VALUE)
        dp[0] = 0

        for (int target = 1; target<amount; target++){
            for (int coin: coins){
                if (target >= coin && dp[target - coin] != Integer.MAX_VALUE) {
                    dp[target] = Math.min(dp[target], dp[target - coin] + 1);
                }
            }
        }

        return dp[amount] == Integer.MAX_VALUE ? -1 : dp[amount]
    }

    private int helper(int[] coins, int amount, Map<Integer, Integer> memo) {

        int min = Integer.MAX_VALUE;
        int count = 0 ;

        if (amount == 0){
            return 0;
        }

        if (amount < 0){
            return -1;
        }

        if (memo.containsKey(amount)) {
            return memo.get(amount);
        }

        for (int coin: coins){
            int curr_value = helper(coins, amount-coin, memo);

            if (curr_value >= 0){
                min = Math.min(min, curr_value+1);
            }
        }


        int result = (min == Integer.MAX_VALUE) ? -1 : min;
        memo.put(amount, result);
        return result;

    }
}