# 283. Move Zeroes

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.


# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:

# Input: nums = [0]
# Output: [0]


def move_zero(nums):
    idx = 0
    for _ in range(len(nums)):
        if nums[idx] == 0:
            nums.pop(idx)
            nums.append(0)
        else:
            idx += 1
    return nums


def move_zero_2(nums):
    j = 0
    for num in nums:
        if nums[j] != 0:
            j += 1
        else:
            nums[j] = num

    for k in range(j, len(nums)):
        nums[k] = 0
    return nums


nums = [0, 1, 0, 3, 12]
nums = [0, 1, 0]
print(move_zero(nums))
print(move_zero_2(nums))
