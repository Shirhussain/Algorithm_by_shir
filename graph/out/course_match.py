
Graphs
What is a graph?
A graph has two things:
V: Vertices ( or nodes): A set
E: Edges: A set of(u, v) where u, v are in V(note that E can be empty)
Therefore, graph is defined as a pair(tuple) of two sets
G(V, E)

What is a simple graph:
A graph where there are no self loops. We usually only talk about simple graphs because self loops are usually not interesting.

What is the size of a graph?
|V | = n
|E | = m
What is the relation between m, n?
m = O(n ^ 2): in the worst case, m is quadratic compared to n.
In an undirected graph: I can connect n-1 edges to each node. I have n nodes, so the maximum  number of edges would be n(n-1)/2 = O(n ^ 2).
In a directed graph: I can connect n-1 edges to each node. I have n nodes, so the maximum  number of edges would be n(n-1) = O(n ^ 2).
So if they are related, why do we talk about the size of the graph in terms of m, n separately?
Because graphs sometimes miss a lot of potential edges(called sparse graphs). In that case it’s more accurate to talk about the size in terms of m, n rather than just n. The graph on the left has many more edges compared to the graph on the right. But they both have the same number of nodes.

A graph can be directed or undirected

An undirected graph can be converted to directed graph by: replacing each undirected edge with two opposite edges.
Connectivity:
An undirected graph is called connected if I can reach any node from any other node.

A directed graph is called strongly-connected, if I can reach any node from any other node.

Connected component:
Undirected graph: a subgraph that is connected.
Directed graph: a subgraph that is strongly connected.

How to find connected components?
DFS/BFS for undirected graphs
Kosaraju’s for strongly connected components in directed graphs
Tarjan’s algorithm for strongly connected components in directed graphs
Union-find
How do we represent graphs as a data structure?
Direct translation of the definition(e.g. use a set/list for V and a set/list for E)
Adjacency List: a map of a node to a list of adjacent nodes.

Adjacency Matrix: A mapping of each node to all other nodes to 0/1.
Very popular

Which representation should I use?
There is a trade-off between runtime and memory!

How about Grid representation?

This grid is often used to represent a map of a maze.
It is usually represented by a matrix(not to be confused with adjacency matrix)
How to represent this as a graph?
What is V? Each cell
What is E? Each cell has 4 four neighbors(assuming we can only go up/down and left/right)

If some cells are blocked(i.e. have 0). Some potential neighbors don’t exist.


What graph algorithm should I know?
DFS and BFS(Please do not go to any interviews unless you can write these algorithms with your eyes closed!)
Also please remember their runtime/space complexity:
DFS/BFS runtime: O(m+n)
DFS space: O(n), but there is usually a tighter upper bound, which is the depth of the graph(the longest path in the graph)
BFS space: O(n), but there is usually a tighter upper bound, which is the width of the graph.
Topological sort
Cycle detection
Can be done with slight enhancement of DFS
​​
Finding connected components
Travelling Salesman
Chinese mailman
Shortest path algorithms
Bipartite check
What are some indicators I should use a Graph

How do I solve a Graph problem
Relationship between entities(e.g. social networks)
Connectivity problems(e.g. Find the number of isolated people in a social network or routing problems in a network)
Path finding and shortest path
Cycle detection
Matching problems
Obvious Problems which are defined on graphs: e.g minimum spanning tree.
.
Write a template for a recursive DFS graph traversal


def dfs(graph, node, visited):
    if node in visited:  # Base case: already visited
        return

    visited.add(node)  # Mark as visited
    process(node)  # Process the node (custom logic)

    for neighbor in graph.get(node, []):  # Explore neighbors
        dfs(graph, neighbor, visited)


Write a template for an iterative BFS or DFS graph traversal


def bfs(graph, start):
    queue = deque([start])
    visited = set([start])  # Mark start node as visited

    while queue:
        node = queue.popleft()  # Dequeue a node
        process(node)  # Process the node

        for neighbor in graph.get(node, []):  # Explore neighbors
            if neighbor not in visited:
                visited.add(neighbor)  # Mark as visited
                queue.append(neighbor)  # Enqueue neighbor


What is the runtime & space complexity of a Graph Traversal?


Problem 1:
https: // leetcode.com/problems/number-of-islands/submissions/1531817367

Problem 2:
'''
Input: numCourses = 2, prerequisites = [[1,0]]


0  <-----  1




Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
  /------>  \
0  <-----   1




I can take all courses if there are no cycles.
Remember that for topo sort to exist, there should not be aaaaa cycle.


Solution: check if the graph has a cycle (yous can use dfs for this). If so, return false, otherwise true.


   enhanced DFS where we mark nodes as three states instead of two states
   UNVISITED
   VISITED
   VISITING (new state)


'''


class State(Enum):
    UNVISITED = 0
    VISITING = 1
    VISITED = 2


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        state = {i: State.UNVISITED for i in range(numCourses)}

        # Return false when there is a cycle

        def dfs(course):
            if state[course] == State.VISITING:
                return False

            if state[course] == State.VISITED:
                return True

            state[course] = State.VISITING:

            for neighbor in get_neighbors[course]:
                if not dfs(neighbor):
                    return False

            state[course] = State.VISITED:
            return True

        for course in range(numbCourse):
            if not dfs(course):
                return False

        return True
