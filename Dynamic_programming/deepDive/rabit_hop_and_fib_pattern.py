from typing import List
from functools import lru_cache

def rabbit_hop(n):
    
    @lru_cache
    def helper(i):
        if i==n:
            return 1
        if i>n:
            return 0
        return helper(i+1) + helper(i+2)
    
    return helper(0)


print(rabbit_hop(5))



# def rabbit_hop_dp(n):
#     dp =  [0] * n
#     dp[0]=1


#     for i in range(3, n):


""" 
                    

"""



class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        if n ==1:
            return nums[0]
        
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0] , nums[1])

        for i in range(2, n):
            """
            if i robe a hose so the value of me + the sum all value up ot (n-2)
            if not robe a house so the value is the sum of one prevouse house (n-1)


            space = O(n)
            times = O(n)
            """
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        
        return dp[n-1]


class Solution2:
    def rob(self, nums: List[int]) -> int:
        prev2 = 0 #dp[i-2]
        prev1 = 0 #dp[i-1]

        for x in nums:
            """
            if i robe a hose so the value of me + the sum all value up ot (n-2)
            if not robe a house so the value is the sum of one prevouse house (n-1)

            space O(1)
            time O(n)
            """
            curr = max(prev1, prev2+x)
            prev2 = prev1
            prev1 = curr
        
        return prev1
        


s = Solution2()
nums = [1,2,3,1]
s.rob(nums)


from functools import cache

@cache
def volleyball_score(a,b):
    if a == 0 and b == 0:
        return 1
    
    if a < 0 or b < 0:
        return 0
    
    return volleyball_score(a-1,b) + volleyball_score(a,b-1)

print(volleyball_score(26,24))

def volleyball_score_dp(a,b):
    dp = [[0]* (b+1) for _ in range(a+1)]
    dp[0][0] = 1

    print(dp)

    for i in range(a+1):
        for j in range(b+1):
            if i == 0 and j == 0:
                continue

            # think like how robopath works in a matrix.
            up = dp[i-1][j] if i > 0 else 0
            left = dp[i][j-1] if j > 0 else 0 
            dp[i][j] = up + left 
    return dp[a][b]


print(volleyball_score_dp(3,3))
print(volleyball_score_dp(26,24))





