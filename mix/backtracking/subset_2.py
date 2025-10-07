""" 
Subsets II

Given an integer array nums that may contain duplicates, return all possible

(the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:

Input: nums = [0]
Output: [[],[0]]


use pick or not pick template 
it is inside the dynamic programming folder
                                          1,2,2
                                             []
                                 not pick/     pick\
                                     []          [1]
                                     / \         / \
                                []    [2]      [1]   [1,2]
                              / \     / \      / \     /  \
                            [] [2] [2] [2,2] [1][1,2] [1,2] [1,2,2]

to remove duplicates then become [[], [1], [1,2], [1,2,2], [2], [2,2]]

"""


class Solution:
    def subsets_with_duplicates(self, nums):
        nums.sort()
        result, subset = [], []
        self.backtrack(nums, 0, subset, result)
        # self.backtrack_optimized(nums, 0, subset, result)
        return result

    def backtrack(self, nums, index, subset, result):
        if index == len(nums):
            if subset not in result:
                result.append(subset[:])
                return
            return
        # not pick
        self.backtrack(nums, index + 1, subset, result)

        # pick
        subset.append(nums[index])
        self.backtrack(nums, index + 1, subset, result)
        subset.pop()

    def backtrack_optimized(self, nums, index, subset, result):
        if index == len(nums):
            result.append(subset[:])
            return

        # pick
        subset.append(nums[index])
        self.backtrack_optimized(nums, index + 1, subset, result)
        subset.pop()

        # not pick
        while index + 1 < len(nums) and nums[index] == nums[index + 1]:
            index += 1
        self.backtrack_optimized(nums, index + 1, subset, result)


sol = Solution()
print(sol.subsets_with_duplicates([1, 2, 2]))
