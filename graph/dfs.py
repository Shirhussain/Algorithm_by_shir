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


def dfs(graph, node):
    visited = []
    stack = []
    
    visited.append(node)
    stack.append(node)
    
    while stack:
        current = stack.pop()
        print( current , end = " ")
        for n in reversed(graph[node]):
            if n not in visited:
                visited.append(n)
                stack.append(n)
                
dfs(graph, "A")
        