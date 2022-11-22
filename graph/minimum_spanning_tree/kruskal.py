# it's a greedy algorithm
# it's find a minimum spanning tree for weighted undirected graph in two ways
#  increase cost edges at each step
# avoid any cycle at each step

# Kruskal(G)
# for each vertex:
#   MakeSet(V)
# sort each set in non decreasing order by weighted
# for each edge (u,v):
#    if findSet(u) != findSet(v):
#       union (u,v)
#       cost = cost + edge(u,v)

import dis_join_set


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.nodes = []
        self.minimum_spanning_tree = []

    def add_edge(self, start, destination, weight):
        self.graph.append([start, destination, weight])

    def add_node(self, value):
        self.nodes.append(value)

    def print_solution(self, start, destination, weight):
        for start, destination, weight in self.minimum_spanning_tree:
            print(f"{start} - {destination}: {weight}")

    def kruskal(self):
        i, e = 0, 0
        # making set for every node
        des_joint = dis_join_set.DisJoinSet(self.nodes)
        self.graph = sorted(self.graph, key=lambda item: item[2])
        while e < self.V - 1:
            start, destination, weight = self.graph[i]
            i += 1
            x = des_joint.find(start)
            y = des_joint.find(destination)
            if x != y:
                e += 1
                self.minimum_spanning_tree.append([start, destination, weight])
                des_joint.union(x, y)
        self.print_solution(start, destination, weight)


new_graph = Graph(5)
new_graph.add_node("A")
new_graph.add_node("B")
new_graph.add_node("C")
new_graph.add_node("D")
new_graph.add_node("E")
new_graph.add_edge("A", "B", 5)
new_graph.add_edge("A", "C", 13)
new_graph.add_edge("A", "E", 15)
new_graph.add_edge("B", "A", 5)
new_graph.add_edge("B", "C", 10)
new_graph.add_edge("B", "D", 8)
new_graph.add_edge("C", "A", 13)
new_graph.add_edge("C", "B", 10)
new_graph.add_edge("C", "E", 20)
new_graph.add_edge("C", "D", 6)
new_graph.add_edge("D", "B", 8)
new_graph.add_edge("D", "C", 6)
new_graph.add_edge("E", "A", 15)
new_graph.add_edge("E", "C", 20)

new_graph.kruskal()
