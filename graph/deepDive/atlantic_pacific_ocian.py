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
 

Constraints:

m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 105

"""

"""
We want to find all nodes from which we can go to both Pacific and Atlantic
Idea:
    - Use DFS to see what nodes we can get to from Pacific in reverse ---> P
    - Use DFS to see what nodes we can get to from Atlantic in reverse ---> A
    - Return P ∩ A

I'm going to map this to a graph:
    V: Every cell in the grid plus an extra node for Atlantic and one node for pacific
    E: There is an edge from each cell to its four neighbors only if its height is **LESS** than or equal to the neighor.
        - Also, there is an edge from Atlantic to all nodes on the right and bottom edges of the grid
        - Also, there is an edge from Pacific to all nodes on the left and top edges of the grid

    Runtime Complexity:
        O(n+m) , where n = rows*cols and m=4*n + (row2s+cols) = O(rows*cols)
    Memory Complexity:
        O(ros*cols)

"""


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        # Virtual nodes
        pacific_node = (-1, -1)
        atlantic_node = (-1, 0)

        rows = len(heights)
        cols = len(heights[0])

        def GetNeighbor(i, j):
            result = []

            # Handling neighbors of Pacific
            if (i, j) == pacific_node:
                for r in range(rows):
                    result.append((r, 0))
                for c in range(cols):
                    result.append((0, c))
                return result

            # Handling neighbors of Atlantic
            if (i, j) == atlantic_node:
                for r in range(rows):
                    result.append((r, cols - 1))
                for c in range(cols):
                    result.append((rows - 1, c))
                return result

            for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                # Check the boundary
                if ni < 0 or nj < 0 or ni >= rows or nj >= cols:
                    continue

                # Check the height
                if heights[i][j] > heights[ni][nj]:
                    continue

                result.append((ni, nj))
            return result

        pacific_visited = set()
        atlantic_visited = set()

        def dfs(i, j, visited):
            if (i, j) in visited:  # Base case: already visited
                return

            visited.add((i, j))  # Mark as visited

            for ni, nj in GetNeighbor(i, j):  # Explore neighbors
                dfs(ni, nj, visited)

        dfs(pacific_node[0], pacific_node[1], pacific_visited)
        dfs(atlantic_node[0], atlantic_node[1], atlantic_visited)

        return [[i, j] for i, j in pacific_visited & atlantic_visited]
