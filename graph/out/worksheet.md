read this once: https://www.cs.princeton.edu/~wayne/kleinberg-tardos/

https://docs.google.com/document/d/12VirIjRy5VqQqBwRD2trhHwPfVN84XQ1_ijQo4ryCDU/edit?usp=sharing

https://docs.google.com/document/d/1GD4PJFtNePP5pfOhgI-oVcS5wBoPqwmN0DbGAD5NW3M/edit?usp=sharing

Graphs
What is a Graph?
Node: a data point or a number
A graph is a set of vertices that are connected via edges.
G = (V, E), where V is a set of vertices (aka nodes) and E is a set of edges.
Each edge in E is a subset of V*V, which means each edge is a pair of vertices.
One of the first steps in Graph problems is to accurately recognize
V
E
What are some indicators I should use a Graph
If my input can be mapped to a graph (i.e. V, E), then maybe we are solving a graph problem.
E.g. relationship between data points.
Similarities with famous graph problems
In a weighted graph:
Shortest path
Longest path
If there is a positive cycle reachable from the source, the longest path does not exist!
Otherwise:
Exhaustive search (exponential)
Use Dijkstra but change FindMin to FindMax ?
Transform G(V, E) to G*(V, -E), i.e. multiply all weights by -1, and then find the shortest path.
Bellman-Ford?
Floyd-Warshall?
Traveling salesman
Problems that require finding a shortest route that passes through a set of nodes.
Dependency relationship (course schedule) -> Topological sort
Note that Topo sort is only defined in DAGs!
Connected components
Finding cycles
Undirected: Run DFS: if you visit a node that is not the parent
Directed: Coloring AKA back edges. This extends Visited/unvisited to:
Unvisited or 0 or white
BeingVisited or Visiting or -1 or gray
Visited or 1 or black

How do I solve a Graph problem
Accurately define your V and E
Represent the graph in an efficient data structure
Adjacency list
A map of a node to a list of neighbors
Adjacency matrix
Graph definition, remember that it was V (a set) and E (a set of pairs/set)
So you can use a set/list/vector data structure for V and also for E
Sometimes you can just provide E and deduce V from it
E.g. E= {(1,2), (5, 6)}
Note that this only works if there is no isolated vertex.
Matrix (AKA grid)
Map to a known graph algorithm (some of them are above)
Please never forget DFS and BFS.
.
Write a template for a recursive DFS graph traversal

Write a template for an iterative BFS or DFS graph traversal

What is the runtime & space complexity of a Graph Traversal?
Runtime O(E+V)
Space:
DFS: size of the stack: O( |V| ). But there is a better upper bound which is the depth of your graph.
BFS: size of the queue: O( |V|), but there is a better upper bound which is the width of your graph

Attendance code: GraphOutcoDec12_2
