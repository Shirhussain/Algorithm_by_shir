# Route Between Nodes

# Given a directed graph and two nodes (S and E), design an algorithm to find out whether there is a route from S to E.

# Examples
# breadth_first_search technique
class Graph:
    def __init__(self, graph_dict=None):
        if graph_dict is None:
            graph_dict = {}
        self.graph_dict = graph_dict

    def addEdge(self, vertex, edge):
        self.graph_dict[vertex].append(edge)

    def checkRoute(self, start_node, end_node):
        visited = [start_node]
        queue = [start_node]
        path = False
        while queue:
            dequeue_vertex = queue.pop(0)
            for adjacent_vertex in self.graph_dict[dequeue_vertex]:
                if adjacent_vertex not in visited:
                    if adjacent_vertex == end_node:
                        path = True
                        break
                    else:
                        visited.append(adjacent_vertex)
                        queue.append(adjacent_vertex)
        return path


custom_dict = {"a": ["c", "d", "b"],
               "b": ["j"],
               "c": ["g"],
               "d": [],
               "e": ["f", "a"],
               "f": ["i"],
               "g": ["d", "h"],
               "h": [],
               "i": [],
               "j": []
               }

g = Graph(custom_dict)
print(g.checkRoute("a", "j"))  # True
print(g.checkRoute("a", "e"))  # False
