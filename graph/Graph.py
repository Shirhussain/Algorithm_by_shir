class Graph:
    def __init__(self):
        # for now i just want to create a {}
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        # just adding node or vertex, i.e {A = []}
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False

    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex, ": ", self.adjacency_list[vertex])

    def add_edge(self, vertex1, vertex2):
        # creating something like this
        # {
        #   A: [B],
        #   B: [A],
        # }
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return True
        return False


new_graph = Graph()
new_graph.add_vertex('A')
new_graph.add_vertex('B')
new_graph.add_edge('A', 'B')
new_graph.print_graph()
