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










