""" 
 Maximum Average Subarray I

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
"""
from typing import List

# this look fix size 
def findMaxAverage(nums: List[int], k: int) -> float:
    # global_max_avg = 0
    # for i in range(i, len(nums)-k):
    #     curr_sum = 0
    #     for j in range(i, i+k-1):
    #         curr_sume += nums[j]
    #     avg = curr_sum/k

    window_sum = 0
    for i in range(0, k):
        window_sum += nums[i]
    
    avg = window_sum/k

    for i in range(k, len(nums)):
        window_sum += nums[i]
        window_sum -= nums[i-k]
        curr_avg = window_sum/k
        avg = max(avg, curr_avg)
    return avg 


print(findMaxAverage([1,12,-5,-6,50,3], 4))
print(findMaxAverage([5], 1))