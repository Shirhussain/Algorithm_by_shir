class Graph:
    def __init__(self, graph_dict=None):
        if graph_dict is None:
            return {}
        self.graph_dict = graph_dict

    def add_edge(self, vertex, edge):
        self.graph_dict[vertex].append(edge)

    def breadth_first_search(self, vertex):
        # here we work with queue
        # enqueue any starting vertex
        # while queue is not empty
        #   p = dequeue()
        #   if p is unvisited:
        #       mark it as visited
        #       enqueue all adjacent unvisited vertices of p

        visited = [vertex]
        queue = [vertex]
        while queue:
            dequeue_vertex = queue.pop(0)
            print(dequeue_vertex)
            for adjacent_vertex in self.graph_dict[dequeue_vertex]:
                if adjacent_vertex not in visited:
                    visited.append(adjacent_vertex)
                    queue.append(adjacent_vertex)

    def depth_first_search(self, vertex):
        # here we work with Stack
        # push any starting vertex
        # while stack is not empty:
        #   p = pop()
        #   if p is unvisited:
        #       mark it as visited
        #       push all adjacent unvisited vertices of p
        visited = [vertex]
        stack = [vertex]
        while stack:
            # it will pop the last item
            pop_vertex = stack.pop()
            print(pop_vertex)
            for adjacent_vertex in self.graph_dict[pop_vertex]:
                if adjacent_vertex not in visited:
                    visited.append(adjacent_vertex)
                    stack.append(adjacent_vertex)


custom_dict = {
    'a': ['b', 'c'],
    'b': ['a', 'd', 'e'],
    'c': ['a', 'e'],
    'd': ['b', 'e', 'f'],
    'e': ['d', 'f'],
    'f': ['d', 'e']
}

# this is the above dictionary
#   A
# B   C
# D   E
#   F

new_graph = Graph(custom_dict)
print("========================== BFS =============================")
new_graph.breadth_first_search('a')

print("==========================DFS ================================")
new_graph.depth_first_search("a")
# it gos to 'c' after 'a' because in th list of 'a' it's the deepest element in the list
