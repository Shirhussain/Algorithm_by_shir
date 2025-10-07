""" 
78. Subsets


Given an integer array nums of unique elements, return all possible

(the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:

Input: nums = [0]
Output: [[],[0]]
                              use pick or not pick template 
                            it is inside the dynamic programming folder
                            1,2,3
                              []
                        pick/     not pick\
                        [1]        []
                        /  \       /     \
                    [1,2]  [1]    [2]          []
                    /  \   /  \    /    \       /  \
            [1,2,3] [1,2] [1,3][1][2,3] [2]    [3] []

"""


class Subset:
    def __init__(self, nums):
        self.nums = nums

    def subsets(self):
        result, subset = [], []

        def backtrack(i):
            if i == len(self.nums):
                result.append(subset[:])
                return

            # pick
            subset.append(self.nums[i])
            backtrack(i+1)
            subset.pop()

            # not pick
            backtrack(i+1)

        backtrack(0)
        return result

    def sub_set_iterative(self):
        result = [[]]
        for num in self.nums:
            for i in range(len(result)):
                result.append(result[i] + [num])
        return result

    def sub_set_iterative_2(self):
        result = [[]]
        for num in self.nums:
            result += [res + [num] for res in result]
        return result


sol = Subset([1, 2, 3])
print(sol.subsets())
print(sol.sub_set_iterative())
print(sol.sub_set_iterative_2())
