/**
    1. how to represent the graph
    2. traverse the graph
        BFS
        DFS


        from node1 -> 2, 3, 4
        from node2 -> 3
        from node3 -> 1
 */

class Solution {
    // n = 2, []
    public boolean validTree(int n, int[][] edges) {
        if (edges.length == 0) {
            return n == 1;
        }
        Map<Integer, Set<Integer>> graph = new HashMap<Integer, Set<Integer>>();
        Set<Integer> visited = new HashSet<Integer>();

        // build the graph
        for (int[] edge : edges) {
            int x = edge[0];
            int y = edge[1];

            if (!graph.containsKey(x)) {
                graph.put(x, new HashSet<Integer>());
            }
            graph.get(x).add(y);

            if (!graph.containsKey(y)) {
                graph.put(y, new HashSet<Integer>());
            }
            graph.get(y).add(x);
        }

        // traverse the graphs
        Queue<Integer> queue = new LinkedList<Integer>();
        int start = graph.keySet().iterator().next();
        queue.add(start);
        visited.add(start);

        while (!queue.isEmpty()) {
            int now = queue.poll();

            for (int next : graph.get(now)) {
                if (visited.contains(next)) {
                    return false;
                }

                // now -> next
                // next -> now
                graph.get(next).remove(now);
                queue.offer(next);
                visited.add(next);
            }

            // we touched all the neighbors of NOW
            graph.remove(now);
        }

        // we dont find any circular dependency
        return n == visited.size();

    }
}
