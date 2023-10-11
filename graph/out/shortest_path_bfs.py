'''
Given an unweighted, undirected graph which represents a metro map as follows

vertices are stations
edges are the path between two stations

Given a start station and ending station, determine the minimum number of stops that must be made to get to the destination.

Input: A Graph (unweighted/undirected), a starting Vertex, and an ending Vertex
Output: Integer

Example

Input: The graph represented below, Vertex A, Vertex F
Shortest Route

Output: 2 Stops (From A stop at C, and then stop at F)


# Template for BFS Traversal in a Graph

def graph_traversal_bfs(graph)
  visited = set()

  def helper_bfs(node):
    queue = []

    queue.push(node)

    while len(queue):
      # visit operation
      visited.add(node)
      queue.pop()

      for neighbor in get_neighbors(node):
        if neighbor not in visited:
          queue.push(neighbor)

  helper_bfs(graph[0])

              0
           /     \
           1  -  2
           |  /  |
           3  -  4

'''
from collections import defaultdict

class Graph:
  def __init__(self):
    self.graph = defaultdict(list)

  def addEdge(self, u, v):
    self.graph[u].append(v)

  def shortestPath(self, s, e):
    queue = []
    #visited = set()
    
    def helperBfs(node):
      tuple = (node, 0)
      queue.append(tuple)
      #visited.add(tuple[0])

      while queue:
        tuple = queue.pop(0)
  
        for i in self.graph[tuple[0]]:
          if i == e:
            return tuple[1] + 1
          #if i not in visited:
          queue.append((i,tuple[1] + 1))
            #visited.add(i)

    return helperBfs(s)

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 4)
g.addEdge(2, 4)
g.addEdge(4, 2)
g.addEdge(4, 3)

print(g.shortestPath(0,4))

'''
Time complexity: O(v + e)
Space complexity: O(v)
'''