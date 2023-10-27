"""
    213. House Robber II


    You are a professional robber planning to rob houses along a street. Each house has a 
    certain amount of money stashed. All houses at this 
    place are arranged in a circle. That means the first house is the neighbor of 
    the last one. Meanwhile, adjacent houses have a security system connected, 
    and it will automatically contact the police if two adjacent houses were broken 
    into on the same night.

    Given an integer array nums representing the amount of money of each house, return the 
    maximum amount of money you can rob tonight without alerting the police.

    

    Example 1:

    Input: nums = [2,3,2]
    Output: 3
    Explanation: You cannot rob house 1 (money = 2) and then 
    rob house 3 (money = 2), because they are adjacent houses.

    Example 2:

    Input: nums = [1,2,3,1]
    Output: 4
    Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
    Total amount you can rob = 1 + 3 = 4.

    Example 3:

    Input: nums = [1,2,3]
    Output: 3
    
    

            [1,2,3,1]

            in = include 
            no = not include 

            F(0) = nums[0]
            F(1) = max(nums[0], nums[1])
            F(2) = not in F(2) => F(1) 
                    in  F(2) => F(0) + nums[2]
            F(3) = not in F(3) => F(2)
                    in  F(3) => F(1) + nums[3] 

                        F(i) 
                    in /   no\
                    F(i-2)  F(i-1)

        [2,3,2, 4,1, 7, 10, 0, 7, 9, 1, 8, 12, 2]

        dp1 = [2, 3, 4, 7, 7, 14, 17, 17, 24, 26, 26, 34, 38, 0]
        dp2 = [0, 3, 3, 7, 7, 14, 17, 17, 24, 26, 26, 34, 38, 38]
"""


def house_of_rubber_II(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    dp1 = [0] * n
    dp2 = [0] * n

    # if house rubber start from 0 to n-2
    dp1[0] = nums[0]
    for i in range(1, n-1):
        dp1[i] = max(dp1[i-1], dp1[i-2] + nums[i])

    # house rubber start from 1 to n-1
    dp2[1] = nums[1]
    for i in range(2, n):
        dp2[i] = max(dp2[i-1], dp2[i-2]+nums[i])

    return max(dp1[n-2], dp2[n-1])


lst = [2, 3, 2, 4, 1, 7, 10, 0, 7, 9, 1, 8, 12, 2]

print(house_of_rubber_II(lst))


def house_of_rubber_2(lst):
    # with function
    n = len(lst)
    if len(lst) == 1:
        return lst[0]

    def rob(start, end):
        dp = [0] * n
        dp[start] = lst[start]
        for i in range(start + 1, end+1):
            dp[i] = max(dp[i-1], dp[i-2] + lst[i])
        return dp[end]

    return max(rob(0, n-2), rob(1, n-1))


print(house_of_rubber_2(lst))


def house_of_rubber_recursive(nums):
    def helper(start, end):
        if start == end:
            return nums[start]
        if start + 1 == end:
            return max(nums[start], nums[end])

        return max(helper(start, end-1), helper(start, end-2)+nums[end])
    n = len(nums)
    return max(helper(0, n-2), helper(1, n-1))


lst = [2, 3, 2, 4, 1, 7, 10, 0, 7, 9, 1, 8, 12, 2]
print(house_of_rubber_recursive(lst))


def house_of_rubber_memo(nums):
    def helper(start, end):
        memo = {}
        if end in memo:
            return memo[end]

        if start == end:
            return nums[start]
        elif start + 1 == end:
            return max(nums[start], nums[end])
        memo[end] = max(helper(start, end-1), helper(start, end-2) + nums[end])
        return memo[end]
    n = len(nums)
    return max(helper(0, n-2), helper(1, n-2))


print(house_of_rubber_memo(lst))
