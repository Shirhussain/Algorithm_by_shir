"""
Pair Sum - Sorted

Given an array of integers sorted in ascending order and a target value, return the indexes of any pair of numbers in the array that sum to the target. The order of the indexes in the result doesn't matter. If no pair is found, return an empty array.

Example 1:
Input: nums = [-5, -2, 3, 4, 6], target = 7
Output: [2, 3]
"""
nums = [-5, -2, 3, 4, 6]
target = 7

def pair_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
print(pair_sum(nums, target))


""" 
nums = [-5, -2, 3, 4, 6]
target = 7
diff = 7-3 = 4
i = 3
pair_dict = {12: 0,
            9: 1,
            4: 2,
            }
            
return {diff[i], i}
"""
def par_sum_2(nums, target):
    pair_dict = {}
    
    for i in range(len(nums)):
        diff  = target - nums[i]
        
        if diff in pair_dict:
            return [pair_dict[diff], i]
        pair_dict[nums[i]] = i
    return []
        
print(par_sum_2(nums, target))



def par_sum_two_pointer(nums, target):
    l = 0
    r = len(nums) -1
    
    while l < r:
        if nums[l] + nums[r] == target:
            return [l, r]
        if nums[l] < target:
            l += 1
        if nums[r] > target:
            r -= 1
    return []

print(par_sum_two_pointer(nums, target))