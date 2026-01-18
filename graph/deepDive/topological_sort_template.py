""" 
from collections import deque

indegree = {n: 0 for n in nodes}
for u in graph:
    for v in graph[u]:
        indegree[v] += 1

q = deque([n for n in nodes if indegree[n] == 0])

order = []
while q:
    node = q.popleft()
    order.append(node)
    for nei in graph[node]:
        indegree[nei] -= 1
        if indegree[nei] == 0:
            q.append(nei)
"""
