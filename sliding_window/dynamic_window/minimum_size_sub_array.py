""" 
Given an array of positive integers nums and a positive integer target, return the minimal length of a
subarray
whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0


"""
from typing import List


def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    min_size = float("inf")
    l = 0
    r = 0
    curr_window_sum = 0
    for r in range(len(nums)):
        curr_window_sum += nums[r]

        while l <= r and curr_window_sum >= target:
            min_size = min(min_size, r-l + 1)
            curr_window_sum -= nums[l]
            l += 1
    return min_size if min_size != float("inf") else 0
