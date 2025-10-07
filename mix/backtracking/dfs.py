def dfs(root, visited, graph):
    visited[root] = True
    print(root)

    for node in graph[root]:
        if not visited[node]:
            dfs(node, visited, graph)


neighbors = {
    1: [2, 3],
    2: [4, 5],
    3: [],
    4: [6],
    5: [],
    6: []
}

visited = {node: False for node in neighbors}

dfs(1, visited, neighbors)


# or
neighbors = {
    1: [2, 3],
    2: [4, 5],
    3: [],
    4: [6],
    5: [],
    6: []
}


def new_dfs(root, graph):
    visited = {root}
    print(root)

    for node in graph[root]:
        if node not in visited:
            visited.add(node)
            new_dfs(node, graph)


new_dfs(1, neighbors)
