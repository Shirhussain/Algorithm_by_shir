# https://leetcode.com/problems/coin-change/
"""
https://docs.google.com/document/d/1Uhnldz90UuZU5vDdVRAQgV49aKyR7ieafbmJTrVAH0U/edit?usp=sharing
11 = 1+1+....1 (11 tiems)
11 = 5+5+1 -> The minimum number of coins.
11 = 2+2+2+2+2 + 1
11 = 2+ 2+ 2 + 5
"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        if amount < 0:
            return -1

        result = float("inf")
        for coin in coins:
            branch = self.coinChange(coins, amount - coin)
            if branch != -1:
                result = min(result, branch + 1)

        return result if result != float("inf") else -1


# With memoization:

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def f(amount: int) -> int:
            if amount == 0:
                return 0

            if amount < 0:
                return -1

            result = float("inf")
            for coin in coins:
                branch = f(amount - coin)
                if branch != -1:
                    result = min(result, branch + 1)
            return result

        result = f(amount)
        return result if result != float("inf") else -1
