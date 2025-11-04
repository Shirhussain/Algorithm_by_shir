'''
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

V
1 ---- 2
|      |
|      | 
3 ---- 4  
        

V
1' ---- 2'
|       |
|       |
3' ---- 4'

'''


'''
Constraints:

The number of nodes in the graph is in the range [0, 100].

1 <= Node.val <= 100

Node.val is unique for each node.

There are no repeated edges and no self-loops in the graph.

The Graph is connected and all nodes can be visited starting from the given node.

'''
'''
Diagram

V
1 ---- 7
|      |
|      | 
3 ---- 4  

nodes[1]: {value:1, neighbors: [3', 7']}  # 1'
nodes[2]: {value:2, neighbors: [1', 4']}  # 2'
nodes[3]: {value:3, neighbors: null}  # 3'
...
nodes[100]: {value:100, neighbors: null} # 100'


queue: 7, 4
visited: 1, 3, 7, 4
node: 3

1: 2, 3
2: 1, 4
3: 1, 4
4: 2, 3

Node
1': 2', 3'
2' 
3'
4'


'''
'''
Pseudocode

define clone(node1):
    create an array of 100 Nodes with values correspond9ing to indices of the array
      (nodes[1] contains {value:1, neighbors:null}, etc.)
    
'''


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        pass
