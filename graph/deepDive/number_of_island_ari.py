""" 
Number of Islands

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


""" 
solution: 
    iterate through the grid
    if it's a '1' then run dfs
    if it's a '0' then skip 
    it means that keep the visited node and go to the next
    
"""


"""
    Solution: Find the number of connected components

        We can use DFS: 
            1. Iterate through the entire grid
            2. Run DFS from each unvisited 1 (we change visited ones to 2)
            3. Keep the visited nodes and move to the next unvisited nodes

        return the total number of DFS runs
"""


from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def get_neighbors(i, j):
            result = []

            # Up, Down, Left, Right
            di = [-1, 1, 0, 0]
            dj = [0, 0, -1, 1]

            for k in range(len(di)):
                new_i = i + di[k]
                new_j = j + dj[k]

                # We check two things:
                # 1. out of bound
                if new_i < 0 or new_i >= len(grid):
                    continue

                if new_j < 0 or new_j >= len(grid[0]):
                    continue

                # 2. '0's
                if grid[new_i][new_j] == "0":
                    continue

                result.append([new_i, new_j])
            return result

        def dfs(i, j):
            if grid[i][j] == "2":
                return

            grid[i][j] = "2"
            neighbors = get_neighbors(i, j)

            for neighbor in neighbors:
                dfs(neighbor[0], neighbor[1])

        counter = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    counter += 1

        return counter


grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

solution = Solution()
print(solution.numIslands(grid))
