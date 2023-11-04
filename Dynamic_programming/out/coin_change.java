// Tree

// 2-way directed, 1-way directed
// class Node {
//     int label;
//     Node left;
//     Node right;
//     Node parent;
// }

// Node root = x


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

/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    public Node cloneGraph(Node node) {
        // original : copy
        Map<Node, Node> map = new HashMap<>();
        Queue<Node> queue = new LinkedList<>();

        // use a stack so it will be dfs
        queue.offer(node);
        map.put(node, new Node(node.val));

        // clone val
        while (!queue.isEmpty()) {
            Node now = queue.poll();

            for (Node next : map.get(now)) {
                if (!map.containsKey(next)) {
                    map.put(next, new Node(next.val));
                    queue.offer(next);
                }
            }
        }

        // clone the edges
        for (Map.Entry<Node, Node> entry : map.entrySet()) {
            Node original = entry.getKey();
            Node copy = entry.getValue();

            for (Node nei : original.neighbors) { // 2 4
                Node copyNei = map.get(nei); // 2' 4'
                copy.neighbors.add(copyNei); // copy = 1' : [2', 4']
            }
        }

        return map.get(node);
    }
}

    Map<Node, Node> map = new HashMap<>();
    public Node cloneGraph(Node root) {
        return helper(root);
    }

    // to create a copy a node
    Node helper(Node node) {
        // base conditions
        if (node == null) {
            return null;
        }

        if (map.containsKey(node)) {
            return map.get(node);
        }

        Node copy = new Node(node.val); // 1'
        map.put(node, copy); // 1:1'

        for (Node nei : node.neighbors) { // 2 4
            // for each neighbor, copy val and edge
            Node copyNei = helper(nei);
            copy.neighbors.add(copyNei);
        }

        return copy;
    }

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