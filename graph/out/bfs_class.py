# INPUT: 
#               C
#             /   \
#     A --- B       E  --- F --- D
#             \   /   \   /
#               H       G

# OUTPUT: 

# "ABCHEFGD"


# This order is one of the possible breadth-first paths. "ABHCEFGD" is also a valid breadth-first traversal, but be aware this will not match with the test expectation. To handle for this, make sure you work with the edges for a node in the order they appear in the node's edge list.


graph = {
    'C': ['A', 'E'],
    'A': ['B'],
    'B': ['H'],
    'E': ['F', 'G'],
    'F': ['D'],
    'D': [],
    'H': [],
    'G': []
}



#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'bfs' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. Vertex origin
#

    
# For your reference:

# Vertex:
#   char id
#   edges[Vertex]
# 


from collections import deque

def bfs(origin):
    if origin is None:
        return ""
    my_result = ""
    visited = set()
    q = deque([origin])
    visited.add(origin)
    
    while q:
        current = q.popleft()
        edges = current.edges
        
        for i in range(len(edges)):
            node = edges[i]
            if node not in visited:
                visited.add(node)
                q.append(node)
        my_result += current.id
    return my_result
                
            
    
    
    
    

# DO NOT EDIT
# Vertex class for a graph vertex
class Vertex:
    def __init__(self, id=None):
        self.id = id
        self.edges = []

# DO NOT EDIT
# generate graph from int and list of lists
def deserialize(vertices, edges):
    container = {}
    for i in range(0, len(vertices)):
        container[vertices[i]] = Vertex(vertices[i])
    for edge in edges:
        v1 = edge[0]
        v2 = edge[1]
        container[v1].edges.append(container[v2])
        container[v2].edges.append(container[v1])
    return container[vertices[0]]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    vertices = input()

    edges_count = int(input().strip())

    edges = []

    for _ in range(edges_count):
        edges_item = input()
        edges.append(edges_item)

    
    origin = deserialize(vertices, edges)
        
    result = bfs(origin)

    fptr.write(result + '\n')

    fptr.close()
