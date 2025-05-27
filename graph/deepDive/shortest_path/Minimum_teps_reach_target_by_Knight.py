# Minimum steps to reach target by a Knight
# https://www.geeksforgeeks.org/minimum-steps-reach-target-knight-set-2

# Given a square chessboard of N x N size, the position of Knight and position of a target is given, the task
# is to find out the minimum steps a Knight will take to reach the target position.

# Examples :


# Input : (2, 4) - knight's position, (6, 4) - target cell
# Output : 2

# Input : (4, 5) (1, 1)
# Output : 3

# the first step is to we have to put our problem us a graph then we can put the graph in
# shortest path formula

from collections import deque


def shortest_path(graph, start, end):
    visited = set()
    q = deque(start)
    parent_dict = {}
    parent_dict[start] = "Null"

    while q:
        cur_node = q.popleft()
        if cur_node not in visited:
            for child in graph[cur_node]:
                if not child in visited:
                    q.append(child)
                    if child not in parent_dict:
                        parent_dict[child] = cur_node
            visited.add(cur_node)

    path = []
    path.append(end)

    while parent_dict[end] != "Null":
        path.append(parent_dict[end])
        end = parent_dict[end]
    return path


def generate_adjacency_list(n):
    adjacency_list = {}
    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1),
             (-1, -2), (1, -2), (2, -1)]  # Knight moves

    # Create nodes and initialize adjacency list
    for i in range(n):
        for j in range(n):
            node = (i, j)
            adjacency_list[node] = []

    # Populate adjacency list with valid moves
    for i in range(n):
        for j in range(n):
            current_node = (i, j)
            for move in moves:
                x, y = move
                new_x = i + x
                new_y = j + y
                if 0 <= new_x < n and 0 <= new_y < n:
                    # Add valid move to adjacency list
                    adjacency_list[current_node].append((new_x, new_y))

    return adjacency_list


# Example usage:
n = 8  # Board size
adj_list = generate_adjacency_list(n)
print(adj_list)
