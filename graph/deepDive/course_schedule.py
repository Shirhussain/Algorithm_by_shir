""" 
207. Course Schedule

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

"""
    Solution: 
        Nodes: courses
        Edges are prerequisit relationships

        Detect if there is at least one cycle in the graph because 
        A graph has topological sort iff there are no cycles

        We can use DFS to check if a graph has a cycle or not

        DFS with a change:
            Initially Mark the node that you are visiting as visiting, instead of visited
            continue like before,
            If you hit a node that is marked as visited, you have a cycle
            

            Once you are done with all the children of a visiting node, mark it as visited.
"""

from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        has_cycle = [False]
        visited = set()
        visiting = set()

        adjacency_list = {}

        def create_adjacency_list():
            for i in range(0, numCourses):
                adjacency_list[i] = set()

            for p in prerequisites:
                b = p[1]
                a = p[0]
                adjacency_list[b].add(a)

        def dfs(node):
            if node in visited or has_cycle[0]:
                return

            if node in visiting:
                has_cycle[0] = True
                return

            visiting.add(node)

            for neighbor in adjacency_list[node]:
                dfs(neighbor)

            visiting.remove(node)
            visited.add(node)

        create_adjacency_list()
        for i in range(numCourses):
            if has_cycle[0]:
                return False

            if i not in visited:
                dfs(i)

        return not has_cycle[0]


print(Solution().canFinish(2, [[1, 0]]))
print(Solution().canFinish(2, [[1, 0], [0, 1]]))
