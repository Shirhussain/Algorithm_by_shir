'''
There are 2xN nodes in an undirected graph, and a number of edges connecting some nodes. In each edge, the first value will be between 1 and N, inclusive. The second node will be between N+1 and 2N, inclusive. Given a list of edges, determine the size of the smallest and largest connected components that have 2 or more nodes. A node can have any number of connections. The highest node value will always be connected to at least 1 other node.

Note: Single nodes should not be considered in the answer.

Example
bg = [[1,5],[1,6],[2,4]]


3 (singleton)

2 --- 4

   __ 5
  /
1 
  \__ 6


1       4
  \ / \
2   \   5
     \
3       6

Output: [2,3]

connectedComponents has the following parameter(s):
- int bg[n][2]: a 2-d array of integers that represent node ends of graph edges

Returns
- int[2]: an array with 2 integers, the smallest and largest component sizes


'''
'''
Constraints:

1 <= N <= 15000

2 <= V <= 30000
     E <= (15000)^2

'''
'''
Diagram

bg = [[1,5],[1,6],[2,4]]

VVVVVVVVVVVVVV

1: 5, 6
2: 4
4: 2
5: 1
6: 1

bg = [[1,5],[1,6],[2,4],[3,5]]


1: 5, 6
2: 4
3: 5
4: 2
5: 1, 3
6: 1

min: 30001
max: 2

Remaining nodes to process: 

1: 3
2: 2

queue: 
visited: 2 4
node: 

'''
'''
Pseudocode

def solution(bg):

    set min to 30001
    set max to 2
    convert bg to an adjacency list and capture N
    add left-hand nodes to "remaining nodes to process" set
    while remaining nodes is nonempty
        remove next node from remaining nodes
        visited = bfs(node)
        update min/max using size of visited
        remove visited from remaining
    return [min, max]

    def bfs(start):
        create empty visited set
        create empty queue
        add start to both visited set and queue
        while queue is not empty
            remove node from queue
            for each neighbor of node that is not in visited set
                add neighbor to queue and visited set
        return visited set
        
'''
'''
visited: 1, 5, 6, 3
queue: 6, 3
node: 5

'''


def componentsInGraph(bg):
    pass
