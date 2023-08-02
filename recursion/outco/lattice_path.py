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
