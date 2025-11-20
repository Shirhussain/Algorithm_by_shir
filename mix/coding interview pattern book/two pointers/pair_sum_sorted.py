""" 
Pair Sum - Sorted

Given an array of integers sorted in ascending order and a target value, return the indexes of any pair of numbers in the array that sum to the target. The order of the indexes in the result doesn't matter. If no pair is found, return an empty array.

Example 1:
Input: nums = [-5, -2, 3, 4, 6], target = 7
Output: [2, 3]
Explanation: nums[2] + nums[3] = 3 + 4 = 7

Example 2:
Input: nums = [1, 1, 1], target = 2
Output: [0, 1]

"""
from typing import List

def pair_sum_sorted(nums: List[int], target: int) -> List[int]:
    pair_dict = {}
    
    for i, num in enumerate(nums):
        diff = target - num 
        if diff in pair_dict:
            return [pair_dict[diff], i]
        else:
            pair_dict[num] = i 
    return [] 


nums = [-5, -2, 3, 4, 6]
target = 7
print(pair_sum_sorted(nums, target))


def pair_sum_sorted_tow_pointer(nums, target):
    l = 0 
    r = len(nums) -1 
    
    while l < r:
        if nums[l] + nums[r] == target:
            return [l, r]
        elif nums[l] + nums[r] < target:
            l += 1
        else: 
            r -= 1
    return []

print(pair_sum_sorted_tow_pointer(nums, target))