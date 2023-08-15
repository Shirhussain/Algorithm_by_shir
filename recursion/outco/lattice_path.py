# In each of the examples below, lattice diagrams are provided, along with row/column coordinates.


# Input 1: (2, 3)

#     (2 x 3 lattice of squares)

#    0 __1__2__3
#    1|__|__|__|
#    2|__|__|__|

# Output 1: 10 (number of unique paths from top left corner to bottom right corner)


# Input 2: (2, 2)

#     (2 x 2 lattice of squares)

#    0 __1__2
#    1|__|__|
#    2|__|__|

# (2,2) ==> Output 2: 6 (number of unique paths from top left corner to bottom right corner)


import itertools


def latticePaths(row, col):
    """
        I'm comming form the destination to the start like (2,2) to (0,0)
        because it's very easy to find outband paths or find edge and base cases
    """
    if row < 0 or col < 0:
        return 0
    if row == 0 and col == 0:
        return 1
    up = latticePaths(row - 1, col)
    left = latticePaths(row, col-1)
    return left + up


print(latticePaths(2, 2))

# time complexity is (2^m+n)


# Leet code problem  my solution
# https://leetcode.com/problems/unique-paths/solutions/2999834/python-3-solutions-video-solution/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0
        if m == 1 or n == 1:
            return 1
        return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)


s = Solution()
print(s.uniquePaths(3, 7))


class MemoSolution(object):
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        if (m, n) in memo:
            return memo[(m, n)]

        if m == 0 or n == 0:
            memo[(m, n)] = 0
            return 0

        if m == 1 or n == 1:
            memo[(m, n)] = 1
            return 1

        memo[(m, n)] = self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)
        return memo[(m, n)]


memo_sol = MemoSolution()
print(memo_sol.uniquePaths(3, 7))


def uniq_path_tabulation(m, n):
    """
        how it works Let's consider an example with m = 3 and n = 3.

        dp after initialization:
        [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

        After filling the cell (0, 0):
        [[1, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

        After filling the first row and first column:
        [[1, 1, 1],
        [1, 0, 0],
        [1, 0, 0]]

        After filling the remaining cells:
        [[1, 1, 1],
        [1, 2, 3],
        [1, 3, 6]]
    """
    dp = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

    # i use (m-1) and (n-1) because index start from zero
    return dp[m-1][n-1]


print(uniq_path_tabulation(3, 7))


# or with itertools

def unique_path_with_itertools(m, n):
    dp = [[0 for _ in range(n)] for _ in range(m)]

    for i, j in itertools.product(range(m), range(n)):
        dp[i][j] = 1 if i == 0 or j == 0 else dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1]


print(unique_path_with_itertools(3, 7))


def latus_path_with_start_from_one(m, n):
    dp = [[1 for _ in range(n)] for _ in range(m)]
    # this time i put 1 for the first row and colum by default then start from 1
    # for i in range(1, m):
    #     for j in range(1, n):
    #         dp[i][j] = dp[i-1][j] + dp[i][j-1]

    # return dp[m-1][n-1]
    for i, j in itertools.product(range(1, m), range(1, n)):
        dp[i][j] = dp[i][j-1] + dp[i-1][j]
    return dp[m-1][n-1]


print(latus_path_with_start_from_one(3, 7))
