# in graph we have node(vertices or vertex) and edge

#     A
# B       C

# D .     E

#    F


# just connect this alphabet to each node

class Graph:
    def __init__(self, graph_dict=None):
        if graph_dict is None:
            return {}
        self.graph_dict = graph_dict

    def add_edge(self, vertex, edge):
        self.graph_dict[vertex].append(edge)


custom_dict = {
    'a': ['b', 'c'],
    'b': ['a', 'd', 'e'],
    'c': ['a', 'e'],
    'd': ['b', 'e', 'f'],
    # 'e': ['b', 'c', 'd', 'f'],
    'e': ['b', 'c'],
    'f': ['d', 'e']
}


graph = Graph(custom_dict)
# we want to connect 'e' to 'd'
graph.add_edge('e', 'd')
print(graph.graph_dict['e'])



	1.	Question: Find if a graph is a tree or not.
Solution: A graph is a tree if it is acyclic (no cycles) and has exactly N-1 edges, where N is the number of nodes.


def is_tree(graph):
    visited = set()
    stack = [(0, -1)]

    while stack:
        node, parent = stack.pop()

        if node in visited:
            return False
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor != parent:
                stack.append((neighbor, node))

    return len(visited) == len(graph)

# Example usage:
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 4],
    3: [1],
    4: [2]
}

print(is_tree(graph))  # Output: True


or 



def is_tree(graph):
    num_nodes = len(graph)
    num_edges = sum(len(neighbors) for neighbors in graph.values()) // 2

    return num_edges == num_nodes - 1

# Example usage:
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 4],
    3: [1],
    4: [2]
}

print(is_tree(graph))  # Output: True




shortest path 


from collections import deque

def shortest_path(graph, start, end):
    if start not in graph or end not in graph:
        return None

    queue = deque([(start, [start])])
    visited = set()

    while queue:
        node, path = queue.popleft()

        if node == end:
            return path

        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return None

# Example usage:
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 4],
    3: [1],
    4: [2]
}

start_node = 0
end_node = 4
result = shortest_path(graph, start_node, end_node)

if result:
    print(f"Shortest path from node {start_node} to node {end_node}: {result}")
else:
    print("No path found between the given nodes.")


or for DFS


def shortest_path(graph, start, end):
    if start not in graph or end not in graph:
        return None

    visited = set()
    path = []

    def dfs(node):
        nonlocal path

        if node == end:
            path.append(node)
            return True

        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited and not path:
                if dfs(neighbor):
                    path.append(node)
                    return True

        return False

    dfs(start)
    return list(reversed(path)) if path else None

# Example usage:
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 4],
    3: [1],
    4: [2]
}

start_node = 0
end_node = 4
result = shortest_path(graph, start_node, end_node)

if result:
    print(f"Shortest path from node {start_node} to node {end_node}: {result}")
else:
    print("No path found between the given nodes.")



