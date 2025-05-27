from collections import deque


def shortest_path(graph, start, end):
    visited = set()
    q = deque
    parent_dic = {}
    parent_dic["start"] = "Null"

    while q:
        curr_node = q.popleft()
        if curr_node not in visited:
            # if you have many answer in your answer and you want example between 1= A,B,D,H and 2 = A,C,F,H
            # if both of them are the answer and the question is to output in the last one in alphabetical order
            # so only you need is sort the children here: sorted(graph[curr_node])
            for node in graph[curr_node]:
                if node not in visited:
                    q.append(node)
                    if node not in parent_dic:
                        parent_dic[node] = curr_node
            visited.add(curr_node)

    path = []
    path.append(end)
    while parent_dic[end] != "Null":
        path.append(parent_dic[end])
        end = parent_dic[end]
    return reversed(path)
