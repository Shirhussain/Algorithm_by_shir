import heapq


class Edge:
    # each edge is a directed edge and it has a vector start and end points
    def __init__(self, weight, start_vertex, target_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex


class Node:
    def __init__(self, vertex_name):
        # name is like 'A', 'B', 'C',
        self.vertex_name = vertex_name
        # we assigned as visited to make sure not coming back.
        self.visited = False
        # predecessors is show as which from which node we come to the current node. or parent node.
        self.predecessors = None
        # neighbors is the next nodes which we go from this node to it can be many node
        # which we put our victor to that nodes.
        self.neighbors = []
        # initial distance of all vertex we should assigned to infinite `float('inf')`
        # but only for the first value is going to be '0'
        self.min_distance = float('inf')

    def __lt__(self, other_node) -> bool:
        return self.min_distance < other_node.min_distance

    def add_edge(self, weight, destination_vertex):
        edge = Edge(weight, self, destination_vertex)
        # now adding the neighbors(or those which are going to be the current node)
        self.neighbors.append(edge)


class Dijkstra:
    def __init__(self):
        # we need to create heap data structure
        self.heap = []

    # we need to create the starting node to '0' and the rest is infinity( which already we did)
    def calculate(self, start_vertex):
        start_vertex.min_distance = 0
        heapq.heappush(self.heap, start_vertex)
        while self.heap:
            # pop elements with the lowest distance
            actual_vertex = heapq.heappop(self.heap)
            if actual_vertex.visited:
                continue
            # consider the neighbors
            for edge in actual_vertex.neighbors:
                start = edge.start_vertex
                target = edge.target_vertex
                new_distance = start.min_distance + edge.weight
                if new_distance < target.min_distance:
                    target.min_distance = new_distance
                    target.predecessors = start
                    # update the heap
                    heapq.heappush(self.heap, target)
                    # [F-19, F-17]
            actual_vertex.visited = True

    def get_shortest_path(self, vertex):
        print(f"The shortest path to the vertex is : {vertex.min_distance}")
        actual_vertex = vertex
        while actual_vertex is not None:
            print(actual_vertex.vertex_name, end=" ")
            actual_vertex = actual_vertex.predecessors


# step 1 - create nodes
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")
nodeD = Node("D")
nodeE = Node("E")
nodeF = Node("F")
nodeG = Node("G")
nodeH = Node("H")


# step 2 - create edges
nodeA.add_edge(6, nodeB)
nodeA.add_edge(10, nodeC)
nodeA.add_edge(9, nodeD)

nodeB.add_edge(5, nodeD)
nodeB.add_edge(16, nodeE)
nodeB.add_edge(13, nodeF)


nodeC.add_edge(6, nodeD)
nodeC.add_edge(5, nodeH)
nodeC.add_edge(21, nodeG)


nodeD.add_edge(8, nodeF)
nodeD.add_edge(7, nodeH)

nodeE.add_edge(10, nodeG)

nodeF.add_edge(4, nodeE)
nodeF.add_edge(12, nodeG)


nodeH.add_edge(2, nodeF)
nodeH.add_edge(14, nodeG)


new_dijkstra = Dijkstra()
new_dijkstra.calculate(nodeA)
new_dijkstra.get_shortest_path(nodeG)
