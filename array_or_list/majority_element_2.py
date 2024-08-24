""" 
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

 

Example 1:

Input: nums = [3,2,3]
Output: [3]

Example 2:

Input: nums = [1]
Output: [1]

Example 3:

Input: nums = [1,2]
Output: [1,2]


"""
from collections import Counter
from typing import List


def majorityElement(self, nums: List[int]) -> List[int]:
    # counter = {}
    # result = []

    # for num in nums:
    #     counter[num] = counter.get(num, 0) + 1

    # for num, count in counter.items():
    #     if count > len(nums)//3:
    #         result.append(num)
    # return result

    # result = []
    # counter = Counter(nums)
    # for num, count in counter.items():
    #     if count > len(nums)/3:
    #         result.append(num)
    # return result

    # on line code:
    # return [ num for num, count in Counter(nums).items() if count > len(nums)/3]

    if not nums:
        return []

    candidate1, candidate2, count1, count2 = 0, 1, 0, 0

    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1, count1 = num, 1
        elif count2 == 0:
            candidate2, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1

    return [num for num in (candidate1, candidate2) if nums.count(num) > len(nums) // 3]
