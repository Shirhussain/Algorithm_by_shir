# enqueue any starting vertex
# while queue is not empty
#   p = dequeue()
#   if p is unvisited:
#       mark it as visited
#       enqueue all adjacent unvisited vertices of p update parent of adjacent vertices to curVertex


class Graph:
    def __init__(self, graph_dict=None):
        if graph_dict is None:
            graph_dict = {}
        self.graph_dict = graph_dict

    # it only works for related graph
    # it's not working for weighted graph
    # wight is actually the number which is encluded in the graph consider the price of flyight between cities
    # work with unweighted undirected graph
    # work with unweighted directed graph
    # so it means DFC can not find the single shortest path problem
    def breadth_first_search(self, start, end):
        queue = []
        queue.append([start])
        while queue:
            path = queue.pop(0)
            # get the last element of the queue
            node = path[-1]
            if node == end:
                return path
            for adjacent in self.graph_dict.get(node, []):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)


custom_dict = {
    "a": ["b", "c"],
    "b": ["d", "g"],
    "c": ["d", "e"],
    "d": ["f"],
    "e": ["f"],
    "g": ["f"]
}

new_graph = Graph(custom_dict)
# starting form 'a'
print(new_graph.breadth_first_search('a', 'f'))
print(new_graph.breadth_first_search('a', 'e'))
