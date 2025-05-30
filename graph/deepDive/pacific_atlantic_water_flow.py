""" 
Pacific Atlantic Water Flow


There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

 

Example 1:

Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.

Example 2:

Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.


"""


"""
    Solution 1: From each cell we run DFS to see if we can get to both Atlantic and Pacific
        Runtime: O((m x n)^2) becase we have |V| DFS runs which is m*n and each DFS is O(|V|+|E|)
            But |V| = m x n
                |E| = 4*m x n

    Solution 2: Rather than DFS from each cell to all other nodes, we only run DFS from nodes that touch the ocean:
        1. We can find all nodes that I can reach from Pacific
        2. We can find all nodes that I can reach from Atlantic
        3. We find the intersection

        O(m + n) DFS runs
        EAch DFS O(mxn)
        Total = O((m+n)(mxn))
"""


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        # 2d Boolean matrix of size mxn
        pacific_visited = [[False for _ in range(n)] for _ in range(m)]
        atlantic_visited = [[False for _ in range(n)] for _ in range(m)]

        def get_intersection(pacific, atlantic):
            result = []
            for r in range(m):
                for c in range(n):
                    if pacific[r][c] and atlantic[r][c]:
                        result.append([r, c])
            return result

        def dfs(r, c, visited):
            visited[r][c] = True

            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < m
                    and 0 <= nc < n
                    and not visited[nr][nc]
                    and heights[r][c] <= heights[nr][nc]
                ):
                    dfs(nr, nc, visited)

        # Atlantic: top row and left column:
        for col in range(n):
            dfs(0, col, pacific_visited)
        for row in range(m):
            dfs(row, 0, pacific_visited)

        # Atlantic: bottom row and right column:
        for col in range(n):
            dfs(m - 1, col, atlantic_visited)
        for row in range(m):
            dfs(row, n - 1, atlantic_visited)

        return get_intersection(pacific_visited, atlantic_visited)
