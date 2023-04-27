# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

def two_sum(nums, target):
    arr = [(num, idx) for idx, num in enumerate(nums)]
    sorted_arr = sorted(arr, key=lambda x: x[0])
    
    left = 0
    right = len(sorted_arr)-1
    while left < right:
        sum = sorted_arr[left][0] + sorted_arr[right][0]
        if sum > target:
            right -= 1
        elif sum < target:
            left += 1
        else:
            return sorted_arr[left][1], sorted_arr[right][1]

nums = [2,7,11,4,15] 
target = 15
print(two_sum(nums, target))
