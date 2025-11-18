""" 130. Surrounded Regions

You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.

 

Example 1:

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

Explanation:


In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

Example 2:

Input: board = [["X"]]

Output: [["X"]]

"""

"""
Solution:
    - Iterate through the nodes
    - If it's on the perimeter or visited, or X, leave it out, otherwise do DFS/BFS and we preserve the list of visited.
    - Store the region that it finds
    -   Flip if the region doesn't have a node on the perimeter

Runtime:
    O(m x n)
"""


from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        visited = set()

        def flip_region(region):
            for i, j in region:
                board[i][j] = "X"

        def get_neighbors(i, j):
            di = [-1, 1, 0, 0]
            dj = [0, 0, -1, 1]
            result = []
            for k in range(0, len(di)):
                new_i = i + di[k]
                new_j = j + dj[k]
                if (
                    new_i < 0
                    or new_j < 0
                    or new_i == m
                    or new_j == n
                    or board[new_i][new_j] == "X"
                ):
                    continue

                result.append((new_i, new_j))
            return result

        def dfs(i, j, region, hit_perimeter):
            if (i, j) in visited:
                return
            visited.add((i, j))

            if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                hit_perimeter[0] = True
            else:
                region.add((i, j))

            neighbors = get_neighbors(i, j)
            for neighbor in neighbors:
                dfs(neighbor[0], neighbor[1], region, hit_perimeter)

        for i in range(0, m):
            for j in range(0, n):
                if (i, j) in visited:
                    continue
                if board[i][j] == "X":
                    continue
                if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                    continue
                region = set()
                hit_perimeter = [False]
                dfs(i, j, region, hit_perimeter)
                if not hit_perimeter[0]:
                    flip_region(region)


s = Solution()
board = [["X", "X", "X", "X"], ["X", "O", "O", "X"],
         ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
s.solve(board)
print(board)
