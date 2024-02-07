from collections import deque
graph = {
    "A": ["C", "D", "B", "G"],
    "B": ["A", "D"],
    "C": ["A", "F"],
    "D": ["A", "F", "B"],
    "E": ["G", "H"],
    "F": ["D", "C", "H"],
    "G": ["A", "E"],
    "H": ["E", "F"]
}


def shortest_path(graph, src, dist):
    visited = set(src)
    q = deque(src)
    parent_dic = {}
    parent_dic[src] = "null"
    result = [src]

    while q:
        node = q.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                parent_dic[neighbor] = node
                q.append(neighbor)
                visited.add(neighbor)
                result.append(neighbor)
    path = []
    path_end = dist
    while path_end != "null":
        path.append(path_end)
        path_end = parent_dic[path_end]
    return path[::-1]


nat = shortest_path(graph, "A", "H")

print(nat)
