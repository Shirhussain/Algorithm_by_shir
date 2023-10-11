// Tree

// 2-way directed, 1-way directed
// class Node {
//     int label;
//     Node left;
//     Node right;
//     Node parent;
// }

// Node root = x

"""
Given n nodes labeled from 0 to n-1 and a list of undirected edges 
(each edge is a pair of nodes), write a function to check whether these 
edges make up a valid tree.

Example 1:

Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
Output: true

Example 2:

Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
Output: false


Before solving the problem, we have to know the definitions.
Tree vs Graph

A tree is a special undirected graph. It satisfies two properties

    It is connected
    It has no cycle.
"""


class Solution {
    public boolean validTree(int n, int[][] edges) {
        if (edges.length == 0) {
            return n == 1;
        }
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

        // BFS traversal
        Queue<Integer> queue = new LinkedList<>();
        int id = map.keySet().iterator().next();
        queue.offer(id);
        visited.add(id);

        while (!queue.isEmpty()) {
            int now = queue.poll(); // 1

            // read neighbors
            for (int next : map.get(now)) { // 0 4
                // found a cycle
                if (visited.contains(next)) {
                    return false;
                }

                map.get(next).remove(now); // {0: [2 3]} {4: []}
                visited.add(next); // 0 4
                queue.offer(next); // 4 0
            }

            // map.remove(now); // remove {1 : [0, 4]}
        }

        return visited.size() == n;
    }
}
