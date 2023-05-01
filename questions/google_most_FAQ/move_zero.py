# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:

# Input: nums = [0]
# Output: [0]

number = [0,1,0,3,12]

def move_zero(nums):
    k = 0 
    n = len(nums)
    for num in nums:
        if num != 0:
            nums[k] = num
            k += 1
    for m in range(k,n):
        nums[m] = 0 

    return nums 

print(move_zero(number))