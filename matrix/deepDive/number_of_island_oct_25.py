"""
Solution: 
    1. Go through each unvisited and "1" node
    2. Run DFS from that node and increment a counter for each DFS
    3. Repeat until all "1" nodes are visited
    4. Return the counter

    Instead of having a visited set, we change each cell that we visit from "1" to "2"
    Runtime: 
        1. O(nxm + nxm) = O(nxm) 

"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # All valid and unvisited neighbors
        def get_neighbors(i, j):
            result = []

            # Delta i, j
            # Up, Down, Left, Right
            # .              k
            di = [-1, 1, 0, 0]
            dj = [0, 0, -1, 1]

            for k in range(len(di)):
                new_i = i + di[k]
                new_j = j + dj[k]

                # Check the validity of new_i, new_j

                # 1. Out of bound
                if new_i < 0 or new_i >= m:
                    continue
                if new_j < 0 or new_j >= n:
                    continue

                # 2. Check for "0"
                if grid[new_i][new_j] == "0":
                    continue

                result.append((new_i, new_j))

            return result

        def dfs(r, c):
            if grid[r][c] == "2":  # is visited
                return

            grid[r][c] = "2"
            neighbors = get_neighbors(r, c)

            for neighbor in neighbors:
                dfs(neighbor[0], neighbor[1])

        counter = 0
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == "1":
                    dfs(i, j)
                    counter += 1

        return counter
