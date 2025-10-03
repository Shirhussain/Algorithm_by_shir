# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]


def rotate(nums, k):
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]
    return nums

nums = [1,2,3,4,5,6,7]

print(rotate(nums, 3))


def rotate_array(arr, k):
    temp = []
    i = 0 
    
    x = len(arr) - k 
    while i < x:
        temp.append(arr[i])
        i += 1
    i = 0 
    while k < len(arr):
        arr[i] = arr[k]
        i += 1
        k += 1
    arr = arr[:i] + temp
    return arr
        
print(rotate_array(nums, 3))