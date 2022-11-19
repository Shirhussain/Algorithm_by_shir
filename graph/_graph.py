# in graph we have node(vertices or vertex) and edge

#     A
# B       C

# D .     E

#    F


# just connect this alphabet to each node

class Graph:
    def __init__(self, graph_dict):
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
