# if distance of destination vertex > (distance of source vertex + weight between source and destination vertex):
#      update distance of destination vertex to (distance of source vertex + weight between source and destination vertex)

# bellman ford algorithm is just run about `v-1` time or vertex - one
# because inf i.e in six vertex only the biggest distance can be five vertex  e.g A-B => A-B-C-D-E

class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = []
        self.nodes = []

    # start or source
    def add_edge(self, start, destination, weight):
        self.graph.append([start, destination, weight])

    def add_node(self, value):
        self.nodes.append(value)

    def print_solution(self, distance):
        print("vertex distance from source ")
        for key, value in distance.items():
            print(f" {key}:   {value}")

    def bellman_ford(self, src):
        distance = {i: float("inf") for i in self.nodes}
        distance[src] = 0

        for _ in range(self.v - 1):
            for start, destination, weight in self.graph:
                if distance[start] != float("inf") and distance[start] + weight < distance[destination]:
                    distance[destination] = distance[start] + weight

        for start, destination, weight in self.graph:
            if distance[start] != float("inf") and distance[start] + weight < distance[destination]:
                # in negative we should stop at this condation because we are in the loop of infinity
                print("Graph contain negative cycle")
                return

        self.print_solution(distance)


# how many nodes exist
new_graph = Graph(5)
new_graph.add_node("A")
new_graph.add_node("B")
new_graph.add_node("C")
new_graph.add_node("D")
new_graph.add_node("E")
new_graph.add_edge("A", "C", 6)
new_graph.add_edge("A", "D", 6)
new_graph.add_edge("B", "A", 3)
new_graph.add_edge("C", "D", 1)
new_graph.add_edge("D", "C", 2)
new_graph.add_edge("D", "B", 1)
new_graph.add_edge("E", "B", 4)
new_graph.add_edge("E", "D", 2)

# we start from E to the rest of node
# in print you see the weight from E to the rest i.e. E-A == 6
new_graph.bellman_ford("E")
