""" 
1091. Shortest Path in Binary Matrix

Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

    All the visited cells of the path are 0.
    All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).

The length of a clear path is the number of visited cells of this path.

 Input: grid = [[0,1],[1,0]]
Output: 2

"""
from collections import deque


class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])

        # If the start or end is blocked, return -1
        if grid[0][0] == 1 or grid[m-1][n-1] == 1:
            return -1

        # 8 possible directions: right, down, left, up, and diagonals
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0),
                      (1, 1), (1, -1), (-1, 1), (-1, -1)]

        # Queue for BFS initialized with the starting point (row, col, distance)
        q = deque([(0, 0, 1)])  # (row, col, distance)
        visited = [[False] * n for _ in range(m)]
        visited[0][0] = True

        # Perform BFS
        while q:
            row, col, dist = q.popleft()

            # If we reach the bottom-right corner, return the distance
            if row == m-1 and col == n-1:
                return dist

            # Explore all possible directions
            for dr, dc in DIRECTIONS:
                new_row, new_col = row + dr, col + dc

                # Ensure the new cell is within bounds and not visited, and it's not an obstacle
                if 0 <= new_row < m and 0 <= new_col < n and not visited[new_row][new_col] and grid[new_row][new_col] == 0:
                    visited[new_row][new_col] = True
                    q.append((new_row, new_col, dist + 1))

        return -1  # If no path is found
