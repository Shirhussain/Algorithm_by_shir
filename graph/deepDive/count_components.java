"""
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.


Explain
Example 1:

Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

     0          3
     |          |
     1 --- 2    4 

Output: 2

Example 2:

Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

     0           4
     |           |
     1 --- 2 --- 3

Output:  1
"""

class Solution {
    public int countComponents(int n, int[][] edges) {
        // how to get the count

        Map<Integer, Set<Integer>> map = new HashMap<>();
        Set<Integer> visited = new HashSet<>();

        // {0: [1 2 3]}, 1 : [0, 4] ...
        // cosntruct the graph
        for (int[] edge : edges) {
            int x = edge[0];
            int y = edge[1];

            if (!map.containsKey(x)) {
                map.put(x, new HashSet<Integer>());
            }
            map.get(x).add(y);

            if (!map.containsKey(y)) {
                map.put(y, new HashSet<Integer>());
            }
            map.get(y).add(x);
        }

        int count = 0;
        for (int i = 0; i < n; i++) {
            if (!visited.contains(i)) {
                // visited.add(i);
                dfs(i, visited, map);
                count++;
            }
        }

        return count;
    }

    void dfs(int i, Set<Integer> visited, Map<Integer, Set<Integer>> map) {
        visited.add(i);
        Set<Integer> neighbors = map.get(i);

        for (int nei : neighbors) {
            if (!visited.contains(nei)) {
                // visited.add(nei);
                dfs(nei, visited, map);
            }
        }
    }
}