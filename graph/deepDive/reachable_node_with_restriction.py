# 2368. Reachable Nodes With Restrictions

# There is an undirected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

# You are given a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree. You are also given an integer array restricted which represents restricted nodes.

# Return the maximum number of nodes you can reach from node 0 without visiting a restricted node.

# Note that node 0 will not be a restricted node.


# Example 1:

# Input: n = 7, edges = [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]], restricted = [4,5]
# Output: 4
# Explanation: The diagram above shows the tree.
# We have that [0,1,2,3] are the only nodes that can be reached from node 0 without visiting a restricted node.

# Example 2:

# Input: n = 7, edges = [[0,1],[0,2],[0,5],[0,4],[3,2],[6,5]], restricted = [4,2,1]
# Output: 3
# Explanation: The diagram above shows the tree.
# We have that [0,5,6] are the only nodes that can be reached from node 0 without visiting a restricted node.

from collections import defaultdict, deque
from typing import List


class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        graph = defaultdict(list)
        visited = [False]*n
        result = 0
        # because it's start from zero
        q = deque([0])

        for u, v in edges:
            print("{u:v}", u, v)
            graph[u].append(v)
            graph[v].append(u)

        for u in restricted:
            visited[u] = True

        while q:
            result += len(q)

            for _ in range(len(q)):
                node = q.popleft()
                visited[node] = True
                q.extend([v for v in graph[node] if not visited[v]])
        return result


s = Solution()

n = 7
edges = [[0, 1], [0, 2], [0, 5], [0, 4], [3, 2], [6, 5]]
restricted = [4, 2, 1]
res = s.reachableNodes(n, edges, restricted)
print(res)
