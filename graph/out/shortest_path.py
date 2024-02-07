from collections import deque
garph = {
    "A": ["C", "D", "B", "G"],
    "B": ["A", "D"],
    "D": ["A", "F", "B"],
    "E": ["G", "H"],
    "F": ["D", "C", "H"],
    "G": ["A", "E"],
    "H": ["E", "F"]
}


def shortest_path(graph, src, dist):
    visited = set()
    q = deque(graph[src])
    
    while q:
        node = q.popleft()
        
        for  in graph[node]:
            
