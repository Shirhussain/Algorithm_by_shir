"""
Maximum Subarray

Given an integer array nums, find the subarray with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

"""


"""
    Non-efficient Solution:
        Prefix sum: yes. Create the prefix sum array

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]

        [-2, -1, -4, 0, -1, 1, 2, -3, 1]

I can find the max subarray, by checking the sum from each i to j in the prefix sum array.

In this case P[6] - P[2] = 6 is the max value.

Runtime: O(n^2)

There is a better O(n) soloution that detects the max sum by tracking valley and peaksk in the
prefix array.


    - The DP solution:
        - How to know this has a DP solution:
            - Solve the problem in a very small simplified case and see
                if you can see a pattern and use this case as the base case of a recursion.
                E.g. an empty array or an array of size 1, etc.

            - For array problems, it's very commong to formulate the recursion as a function
                of i, where i is the index of the array.


            Let F(i) be the max subarray value where the subarray ends at i

             [-2,1,-3,4,-1,2,1,-5,4]
                                  i
             F(0) = nums[0] = -2
             F(1) =  It's either
                - F(1) because adding previous members would be worse
                - F(0) + nums[1]


            We should pick the maximum value:
            F(1) = max(nums(1), F(0) + nums[1]) = max(1, -1) = 1


            So, the recursion is:
            F(i) = max (nums[i], f(i-1) + nums[i])

            F(2) = max(nums(2), F(1) + nums[2]) = max(-3, -2) = -2
            F(3) = max(nums(3), F(2) + nums[3]) = max(4, -2+4) = 4
            F(4) = max(nums(4), F(3) + nums[4]) = max(-1, 4+ (-1)) = 3
            F(5) = max(nums(5), F(4) + nums[5]) = max(2, 3+2) = 5
            F(6) = max(nums(6), F(5) + nums[6]) = max(1, 5+1) = 6
            F(7) = max(nums(7), F(6) + nums[7]) = max(-5, 6-5) = 1
            F(8) = max(nums(8), F(7) + nums[8]) = max(4, 1+4) = 5

            Return the max F(i) = 6
"""

from typing import List 

class Solution:

    # Kadan's Algorithms
    def maxSubArray(self, nums: List[int]) -> int:
        # You don't need to store the entire table.
        # Just keep the previous value.
        # Momory: O(1)
        cur_value = nums[0]

        result = nums[0]
        for i in range(1, len(nums)):
            cur_value = max(nums[i], cur_value + nums[i])
            result = max(result, cur_value)

        return result

    # Tabulation
    def maxSubArray_tabulation(self, nums: List[int]) -> int:
        # Create a table and initialize the base case
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]

        for i in range(1, n):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])

        return max(dp)

    def maxSubArray_memo(self, nums: List[int]) -> int:
        @cache
        def dfs(i):
            if i == 0:
                return nums[0]

            tmp = dfs(i - 1)

            return max(nums[i], tmp + nums[i])

        result = float("-inf")
        for i in range(0, len(nums)):
            result = max(result, dfs(i))

        return result

