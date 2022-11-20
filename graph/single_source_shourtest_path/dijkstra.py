class Edge:
    # each edge is a directed edge and it has a vector start and end points
    def __init__(self, weight, start_vertex, target_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.end_vertex = target_vertex


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
