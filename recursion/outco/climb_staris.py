"""You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step




                    n=3 --> (n-1) and (n-2) 
                1/      2\ 
                2         1
            1/    2\   1/   2\
            1     0    0      -1
          1/ 2\ 
          0   -1       
    
    [1,1,1]         [2,1]   [1,2]
"""


class Solution:
    def fib(self, n):
        if n in [1, 2]:
            return 1
        if n == 0:
            return 0
        return 0 if n == 0 else self.fib(n-1) + self.fib(n-2)

    def climb_stairs(self, n):
        return self.fib(n)


s = Solution()
result = s.climb_stairs(10)
print(result)


class Solution_memo:
    # def __init__(self):
    #     self.state = {}
    state = {}

    def fib(self, n):
        if n in self.state:
            return self.state[n]

        if n in [1, 2]:
            return 1
        if n == 0:
            return 0

        self.state[n] = self.fib(n-1) + self.fib(n-2)
        return self.state[n]

    def climb_stairs(self, n):
        return self.fib(n)


s_memo = Solution_memo()
result = s_memo.climb_stairs(10)
print(result)


class Solution_in_fn_memo:

    def fib(self, n, memo):
        if n in memo:
            return memo[n]

        if n in [1, 2]:
            return 1
        if n == 0:
            return 0
        memo[n] = self.fib(n-1, memo) + self.fib(n-2, memo)
        return memo[n]

    def climbing_stairs(self, n):
        return self.fib(n, {})


s_fn_memo = Solution_in_fn_memo()
result = s_fn_memo.climbing_stairs(10)

print(result)


class Solution_in_fn_tabulation(object):
    def climb_stairs(self, n):
        dp = [0] * n
        dp[1] = dp[2] = 1
        for i in range(3, range(n)):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]


s_with_tabulation = Solution_in_fn_tabulation
result = s.climb_stairs(10)
print(result)
