class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, node1, node2):
        if node1 in self.graph and node2 in self.graph:
            self.graph[node1].append(node2)
            self.graph[node2].append(node1)  # For an undirected graph

    def get_neighbors(self, node):
        return self.graph.get(node, [])

    def has_node(self, node):
        return node in self.graph

    def has_edge(self, node1, node2):
        return node1 in self.graph and node2 in self.graph[node1]

    def __str__(self):
        result = ""
        for node in self.graph:
            result += f"{node}: {self.graph[node]}\n"
        return result


# Test the Graph class
if __name__ == "__main__":
    g = Graph()
    g.add_node(1)
    g.add_node(2)
    g.add_node(3)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 1)

    print("Graph:")
    print(g)
    print("Neighbors of node 2:", g.get_neighbors(2))
    print("Does node 3 have an edge with node 1?", g.has_edge(3, 1))
    print("Does node 4 exist in the graph?", g.has_node(4))
