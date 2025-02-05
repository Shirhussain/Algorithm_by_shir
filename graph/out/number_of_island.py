'''
     Sounds like finding connected components, but we want connected components whose nodes are all 1's.
     Solution:
        1. V: all cells
           E: there is an edge only between 1's in four direction
            Find all connected components that consist of non-isolated 0's and count them.

            For finding connected components, we can use DFS:
                - Start from an unvisited node with value of 1. run DFS until we visit all connected nodes.
                - Repate until all ones are visited
                - Return how many times we ran DFS

            We can keep track of visited by maintaining a list of visited nodes. Alternatively, 
            we could flip each node that we visit from 1 to X.


'''

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def get_neighbors(i, j):
            result = []
            # How i changes in 4 directions:
            # Up, down, left, left
            di = [-1, 1, 0, 0]
            dj = [0, 0, -1, 1]

            for k in range(0, len(di)):
                new_i = i+di[k]
                new_j = j+dj[k]

                # Check 2 things:
                # 1. the new cell should not be out of bound
                if new_i < 0 or new_i >= len(grid):
                    continue

                if new_j < 0 or new_j >= len(grid[0]):
                    continue

                # 2. the new cell should be 1.
                if grid[new_i][new_j] != "1":
                    continue

                result.append((new_i, new_j))
            return result

        def dfs(i, j):
            if grid[i][j] == 'x':
                return

            grid[i][j] = 'x'

            neighbors = get_neighbors(i, j)
            for neighbor in neighbors:  # Explore neighbors
                dfs(neighbor[0], neighbor[1])

        counter = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == '1':
                    counter += 1
                    dfs(i, j)

        return counter


s = Solution()
print(s.numIslands([["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], [
      "1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]))

print(s.numIslands([["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], [
      "0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]))
