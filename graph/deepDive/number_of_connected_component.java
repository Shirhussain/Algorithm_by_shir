/**
    1. how to represent the graph
    2. traverse the graph
        BFS
        DFS
 */
class Solution {
    public int countComponents(int n, int[][] edges) {
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

        // traverse the graph
        int count = 0;

        for (int i = 0; i < n; i++) {
            // all the nodes, in X connected components
            if (visited.contains(i)) {
                continue;
            }

            Queue<Integer> queue = new LinkedList<Integer>();
            queue.add(i);
            visited.add(i);
            count++; // a new island found!

            // mark all the nodes in the island as visited, traverse!
            while (!queue.isEmpty()) {
                int now = queue.poll();

                if (graph.get(now) != null) {
                    for (int next : graph.get(now)) {
                        if (visited.contains(next)) {
                            continue;
                        }
                        queue.offer(next);
                        visited.add(next);
                    }
                } 
            }

        }

        return count;
    }
}

