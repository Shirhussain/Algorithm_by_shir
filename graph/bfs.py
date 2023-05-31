graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E', 'F'],
    "C": ['G'],
    "D": [],
    "E": [],
    "F": ["H"],
    "G": ["I"],
    'H': [],
    'I': [],
}


def bfs(graph, node):
    visited = []
    queue = []
    
    visited.append(node)
    queue.append(node)
    
    while queue:
        current = queue.pop(0)
        print(current, end=" ")
        for n in graph[current]:
            if n not in visited:
                visited.append(n)
                queue.append(n)


bfs(graph, "A")
bfs(graph, "F")

                