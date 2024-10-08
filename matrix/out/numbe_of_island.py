""" 
Number of island
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

"""

from collections import deque
from typing import List
grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]


class Solution:
    def numberIsland(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
                return

            # mark as visited
            grid[i][j] = "0"

            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        counter = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    counter += 1
                    dfs(i, j)
        return counter


s = Solution()
print(s.numberIsland(grid))


grid2 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]


class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])

        def bfs(i, j):
            queue = deque([(i, j)])
            grid[i][j] = "0"  # Mark as visited by turning it to '0'

            # Possible 4 directions (down, up, right, left)
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            while queue:
                x, y = queue.popleft()
                # Explore all 4 directions
                for dx, dy in directions:
                    new_x, new_y = x + dx, y + dy
                    # If the new coordinates are within bounds and are land ('1')
                    if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == "1":
                        queue.append((new_x, new_y))
                        grid[new_x][new_y] = "0"  # Mark as visited

        counter = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":  # Found an unvisited land
                    counter += 1       # This is a new island
                    bfs(i, j)          # Perform BFS to mark the entire island
        return counter


s = Solution2()
print(s.numIslands(grid2))  # Output should be 1
