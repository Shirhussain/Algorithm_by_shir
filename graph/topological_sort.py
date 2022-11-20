# if a vertex depends on current vertex
#     go to the vertex and then comeback to current vertex
# else:
#     push current vertex to the stack

from collections import defaultdict


class Graph:
    def __init__(self, number_of_vertices):
        self.graph = defaultdict(list)
        self.number_of_vertices = number_of_vertices

    def add_edge(self, vertex, edge):
        self.graph[vertex].append(edge)

    def topological_sort_utils(self, vertex, visited, stack):
        visited.append(vertex)

        for v in self.graph[vertex]:
            if v not in visited:
                self.topological_sort_utils(v, visited, stack)
        # then here we push
        stack.insert(0, vertex)

    def topological_sort(self):
        visited = []
        stack = []

        for k in list(self.graph):
            if k not in visited:
                self.topological_sort_utils(k, visited, stack)
        print(stack)


new_graph = Graph(8)
new_graph.add_edge("A", "C")
new_graph.add_edge("C", "E")
new_graph.add_edge("E", "H")
new_graph.add_edge("E", "F")
new_graph.add_edge("F", "G")
new_graph.add_edge("B", "D")
new_graph.add_edge("B", "F")
new_graph.add_edge("D", "F")

new_graph.topological_sort()
