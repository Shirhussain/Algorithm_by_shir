"""
Course Schedule

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.


"""

from collections import defaultdict, deque
from typing import List


class Solution:
    """
    Topological sort: 

    remove those node which has "0" incomming edges first 
    then add that node to a list and that list would be the toplogical sort

    

    """
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for u, v in prerequisites:
            graph[u].append(v)
        

        # all node
        nodes = set()
        for u, v in prerequisites:
            nodes.add(u)
            nodes.add(v)
        
        # compute in_dgree or incomming edges
        incomming_edge = {node: 0 for node in nodes }

        for u in graph:
            for v in graph[u]:
                incomming_edge[v] += 1
        
        top_order = []

        q = deque([node for node in nodes if incomming_edge[node] == 0])

        while q:
            curr_node = q.popleft()
            top_order.append(curr_node)
            for neighbor in graph[curr_node]:
                incomming_edge[neighbor] -= 1
                if incomming_edge[neighbor] == 0:
                    q.append(neighbor)
        if len(top_order) == len(nodes):
            return True 
        return False

        

        