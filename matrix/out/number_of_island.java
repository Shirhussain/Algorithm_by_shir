class Solution {
    int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    public int numIslands(char[][] grid) {
        if (grid == null || grid.length == 0) {
            return 0;
        }

        int count = 0;
        int m = grid.length;
        int n = grid[0].length;
        boolean[][] visited = new boolean[m][n];

        // double for loop to find the starting 1
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '1' && !visited[i][j]) {
                    // found a starting non-visited 1!
                    int[] area = {0};
                    count++;
                    dfs(grid, i, j, visited, area);
                    // count++;

                    System.out.println("current area is: " + area[0]);
                }
            }
        }

        return count;
    }

    void dfs(char[][] grid, int i, int j, boolean[][] visited, int[] area) {
        if (i < 0 || i >= grid.length || j < 0 || j >= grid[0].length || grid[i][j] == '0' || visited[i][j]) {
            // out of bound
            return;
        }

        // current element is 1 and it is not visited yet
        visited[i][j] = true;
        area[0] += 1;
        for (int[] dir : directions) {
            dfs(grid, i + dir[0], j + dir[1], visited, area);
        }


        // grid[i][j] = '0';
        // visited[i][j] = true;
        // // it is within bound and also it is a connected 1
        // dfs(grid, i - 1, j, visited);
        // dfs(grid, i + 1, j, visited);
        // dfs(grid, i, j - 1, visited);
        // dfs(grid, i, j + 1, visited);
    }
}


        // if (i >= 0 && i < grid.length && j >= 0 && j < grid[0].length) {

// }
    