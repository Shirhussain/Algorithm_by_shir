""" 

Summary Ranges


You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

    "a->b" if a != b
    "a" if a == b

 

Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"

"""


def summary_range(nums):
    result = []
    l = 0

    for r in range(1, len(nums)+1):
        if r == len(nums) or nums[r] != nums[r-1]+1:
            if l == r - 1:
                result.append(f"{nums[l]}")
            else:
                result.append(f"{nums[l]}->{nums[r-1]}")
            l = r
    return result


print(summary_range([0, 1, 2, 4, 5, 7]))


def summary_range_2(nums):
    start = nums[0]
    end = nums[0]
    result = []

    for i in range(1, len(nums)):
        if nums[i] == end + 1:
            end = nums[i]
        else:
            result.append(f"{start}->{end}" if start != end else f"{start}")
            start = nums[i]
            end = nums[i]
    return result


print(summary_range_2([0, 1, 2, 4, 5, 7]))
