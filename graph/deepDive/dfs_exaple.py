class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, vertex, edge):
        if vertex not in self.graph:
            self.graph[vertex] = []
        self.graph[vertex].append(edge)

    def dfs(self, start_vertex, visited=None):
        if visited is None:
            visited = set()
        visited.add(start_vertex)
        print(start_vertex, end=' ')

        for neighbor in self.graph[start_vertex]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)


# Example usage:
g = Graph()

# Add edges to the graph
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(2, 5)
g.add_edge(3, 6)

print("Depth-First Traversal starting from vertex 1:")
g.dfs(1)
