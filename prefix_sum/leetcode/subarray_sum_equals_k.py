""" 
Subarray Sum Equals K
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2

https://youtu.be/YxRmeRyVQm4?si=Z1RySxdKXVH14vek

"""
from typing import List


def subarraySum(nums: List[int], k: int) -> int:
    count = 0
    prefix_sum = 0
    prefix_sums = {0: 1}  # base case, only one way to get to step 0

    for num in nums:
        prefix_sum += num

        if prefix_sum - k in prefix_sums:
            count += prefix_sums[prefix_sum - k]

        prefix_sums[prefix_sum] = prefix_sums.get(prefix_sum, 0) + 1
    return count


print(subarraySum([1, 1, 1], 2))
print(subarraySum([1, 2, 3], 3))
