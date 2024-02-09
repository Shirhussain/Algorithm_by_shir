# 62. Unique Paths
# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The test cases are generated so that the answer will be less than or equal to 2 * 109.


# Example 1:


# Input: m = 3, n = 7
# Output: 28
# Example 2:

# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down


def unique_path(m, n):
    # dp = []
    # for i in range(m):
    #     col = []
    #     for j in range(n):
    #         col.append(0)
    #     dp.append(col)

    dp = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1]


print(unique_path(3, 7))


# def unique_path_tree(m, n):
#     # [
#     # [0, 0, 0, 0, 0, 0, 0],
#     # [0, 0, 0, 0, 0, 0, 0],
#     # [0, 0, 0, 0, 0, 0, 0]
#     # ]

#     #             (0,0)
#     #         /          \
#     #        (1,0)         (0,1)
#     #     /    \        /    \
#     # (2, 0)    (1,1) (1, 1)  (0, 2)

# or vise versa from to to bottom form (m, n) to 0

#     if m < 0 or n < 0:
#         return
#     if m == 0 and n == 0:
#         return 1
#     return unique_path_tree(m-1, n) + unique_path_tree(m, n-1)


# print(unique_path_tree(3, 7))


def unique_path_tree(m, n):
    memo = {}

    def find_path(row, col):
        if (row, col) in memo:
            return memo[(row, col)]

        if row == 0 or col == 0:
            return 0
        if col == 1 and col == 1:
            return 1
        memo[(row, col)] = find_path(row-1, col) + find_path(row, col-1)
        return memo[(row, col)]
    return find_path(m, n)


# Example usage
result = unique_path_tree(3, 7)
print(result)


def unique_path_tree2(m, n):

    def my_path(row, col):
        if row == m - 1 or col == n - 1:
            return 1
        return my_path(row + 1, col) + my_path(row, col + 1)
    return my_path(0, 0)


print(unique_path_tree2(3, 7))


def unique_path_tree2_memo(m, n):
    memo = {}

    def m_path(row, col):
        if (row, col) in memo:
            return memo[(row, col)]

        if row == m-1 or col == n-1:
            memo[(row, col)] = 1
            return 1
        memo[(row, col)] = m_path(row+1, col) + m_path(row, col+1)
        return memo[(row, col)]
    return m_path(0, 0)


print(unique_path_tree2_memo(3, 7))


def unique_path_tree2_memo_2(m, n):

    def m_path(row, col, memo={}):
        if (row, col) in memo:
            return memo[(row, col)]

        if row == m-1 or col == n-1:
            memo[(row, col)] = 1
            return 1
        memo[(row, col)] = m_path(row+1, col, memo) + m_path(row, col+1, memo)
        return memo[(row, col)]
    return m_path(0, 0)


print(unique_path_tree2_memo_2(3, 7))
