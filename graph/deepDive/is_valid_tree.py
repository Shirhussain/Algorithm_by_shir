"""
Tree

 2-way directed, 1-way directed
 class Node {
     int label;
     Node left;
     Node right;
     Node parent;
 }

Node root = x


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


from collections import defaultdict, deque


def is_valid_tree(n, edges):
    if not n:
        return True

    from collections import defaultdict, deque
    graph = defaultdict(list)

    for src, dist in edges:
        graph[src].append(dist)
        graph[dist].append(src)

    q = deque()
    start_node = next(iter(graph.keys()))
    q.append(start_node)

    visited = set()
    visited.add(start_node)

    while q:
        current_node = q.popleft()

        for neighbor in graph[current_node]:
            if neighbor in visited:
                return False

            graph[neighbor].remove(current_node)
            visited.add(neighbor)
            q.append(neighbor)
    return len(visited) == n


# n = 5
# edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]

n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
print(is_valid_tree(n, edges))


def is_valid_tree_2(n, edges):
    graph = {}

    for edge in edges:
        x, y = edge
        if x not in graph:
            graph[x] = []
        if y not in graph:
            graph[y] = []

        graph[x].append(y)
        graph[y].append(x)

    from collections import deque
    # start_node = next(iter(graph.keys()))
    # or
    start_node = 0

    q = deque([start_node])
    visited = {start_node}

    while q:
        current_node = q.popleft()

        for neighbor in graph[current_node]:
            if neighbor in visited:
                return False
            graph[neighbor].remove(current_node)
            visited.add(neighbor)
            q.append(neighbor)
    return len(visited) == n


print(is_valid_tree_2(n, edges))


def is_valid_tree_DFS(n, edges):
    graph = defaultdict(list)

    for src, dest in edges:
        graph[src].append(dest)
        graph[dest].append(src)

    visited = set()

    def has_cycle(node, parent, visited):
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                if has_cycle(neighbor, node, visited):
                    return True
            elif neighbor != parent:
                # If the neighbor is visited and not the parent, it's a cycle
                return True

        return False

    if has_cycle(0, -1, visited):
        return False

    return len(visited) == n


print(is_valid_tree_DFS(n, edges))
