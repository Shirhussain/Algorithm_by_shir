class Solution:
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dfs(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return -1

            result = float("inf")
            for coin in coins:
                tmp = dfs(amount - coin)
                if tmp != -1:
                    result = min(result, tmp)

            return result + 1 if result != float("inf") else -1
        return dfs(amount)