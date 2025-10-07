""" 
    Permutations
    Given an array nums of distinct integers, return all the possible permutations.
    You can return the answer in any order.
    
    Example 1:

    Input: nums = [1,2,3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

    Example 2:

    Input: nums = [0,1]
    Output: [[0,1],[1,0]]

    Example 3:

    Input: nums = [1]
    Output: [[1]]
    
    
    level one:                                                    []
    level two:                                  [1]                [2]                 [3]
    level three:                      [1,2]      [1,3]        [2,1]    [2,3]       [3,1]    [3,2]
    level four:                       [1,2,3]    [1,3,2]      [2,1,3]   [2,3,1]    [3,1,2]  [3,2,1]

"""


def permutation(nums):
    visited = set()
    result = []

    def helper(subset):
        if len(subset) == len(nums):
            result.append(subset)
            return

        for i in range(len(nums)):
            if i not in visited:
                visited.add(i)
                helper(subset+[nums[i]])
                visited.remove(i)

    helper([])
    return result


print(permutation([1, 2, 3]))
