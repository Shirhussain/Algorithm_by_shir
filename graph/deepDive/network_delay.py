""" 
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel 
times as directed edges times[i] = (ui, vi, wi), where ui is the source node, 
vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for 
all the n nodes to receive the signal. If it is impossible for all the n nodes to 
receive the signal, return -1.



Example 1:


Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
Example 2:

Input: times = [[1,2,1]], n = 2, k = 1
Output: 1

"""
from collections import defaultdict, deque
import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Create adjacency list
        adjacency = {i: [] for i in range(1, n + 1)}

        for src, dst, time in times:
            adjacency[src].append((dst, time))

        # Priority queue for Dijkstra's algorithm (min-heap based on time)
        pq = [(0, k)]  # (time, node)
        visited = set()
        delays = 0

        while pq:
            time, node = heapq.heappop(pq)

            # Skip if the node has been visited
            if node in visited:
                continue

            visited.add(node)
            delays = max(delays, time)

            for neighbor, neighbor_time in adjacency.get(node, []):
                if neighbor not in visited:
                    heapq.heappush(pq, (time + neighbor_time, neighbor))

        # Check if all nodes have been visited
        return delays if len(visited) == n else -1


times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2

s = Solution()
print(s.networkDelayTime(times, n, k))


def network_delay_time(times, n, k):
    graph = defaultdict(list)

    for src, dst, time in times:
        graph[src].append((dst, time))

    print(graph)

    q = [(0, k)]  # time, node
    visited = set()
    delay = 0

    while q:
        time, node = heapq.heappop(q)
        visited.add(node)
        delay = max(delay, time)
        for neighbor, neighbor_time in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                heapq.heappush(q, (neighbor_time + time, neighbor))
    return delay if len(visited) == n else -1


print(network_delay_time(times, n, k))
