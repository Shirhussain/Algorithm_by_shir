""" 
Given an integer array nums, find the

with the largest sum, and return its sum.

 

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
from typing import List


class Solution:
    def __init__(self):
        self.memo = {}

    def maxSubArray(self, nums: List[int]) -> int:
        # nums = [-2,1,-3,4,-1,2,1,-5,4]
        # if there is any nigative number it means getrid of that if we sum it with the previous counts
        # and the result begcome negative otherwise just get the max of current sum or that previous subarray
        # max_sub_arr = nums[0]
        # current_sum = 0
        # for num in nums:
        #     # if it's nigative number let's get rid of that
        #     if current_sum < 0:
        #         current_sum = 0
        #     current_sum += num
        #     max_sub_arr = max(current_sum, max_sub_arr)
        # return max_sub_arr

        # or we can solve with recurtion pick or not pick template
        """
        [-2,1,-3,4,-1,2,1,-5,4]
        f(0) = arr[0]
        f(1) = either of start from zero or start from 1:
                1 if start from 1
                -2 + 1 if start before one 
                = max(arr[1], f(0) + arr[1])

        f(2) = max(arr[2], f(1) + arr[2])
        f(3) = max(arr[3], f(2) + arr[3])

        f(i) = max(arr[i], f(i-1) + arr[i])

        f(i) = max subarray ending exactly at index i 
        """

        def dfs(i):
            if i == 0:
                return nums[0]
            if i in self.memo:
                return self.memo[i]
            self.memo[i] = max(nums[i], dfs(i-1)+nums[i])

            return self.memo[i]

        return max(dfs(i) for i in range(len(nums)))


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
