# first it's better to see _graph.py in this directory
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

    def remove_edge(self, vertex1, vertex2):
        # doing something like this
        # {
        #   A: [],
        #   B: [],
        # }
        # with try we try when we remove the edge which doesn't exist so we have to pass
        # otherwise it will give us value error
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            try:
                self.adjacency_list[vertex1].remove(vertex2)
                self.adjacency_list[vertex2].remove(vertex1)
            except ValueError:
                pass
            return True
        return False

    def remove_vertex(self, vertex):
        # {
        #   A: [B,C,D],                                                  A: [B,C,],
        #   B: [A,C],                                                    B: [A,C],
        #   C: [A,B,D],                                                  C: [A,B,]
        #   D: [A,C] --> consider i remove the D
        # }
        if vertex in self.adjacency_list.keys():
            for other_vertex in self.adjacency_list[vertex]:
                # here i need to see the list of edges with this vertex and then i have to remove
                # it from other lists (other_vertex) too
                self.adjacency_list[other_vertex].remove(vertex)
            del self.adjacency_list[vertex]
            return True


new_graph = Graph()
new_graph.add_vertex('A')
new_graph.add_vertex('B')
new_graph.add_edge('A', 'B')
new_graph.print_graph()


print("================================remove edge================================")
new_graph.add_vertex('C')
new_graph.add_vertex('D')

new_graph.add_edge('A', 'C')
new_graph.add_edge('B', 'C')
new_graph.print_graph()
new_graph.remove_edge('A', 'C')
print("This is after remove")
new_graph.remove_edge('A', 'D')
new_graph.print_graph()

print("================================remove vertex================================")

new_graph.add_edge('A', 'C')
new_graph.add_edge('A', 'D')
new_graph.add_edge('C', 'D')
new_graph.print_graph()
print("after remove")
new_graph.remove_vertex('D')
new_graph.print_graph()
