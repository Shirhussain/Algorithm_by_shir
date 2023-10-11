# for BFS we are using queue data structures and for DFS we are using Stack data structures.

# for BFS we need to do this:
# 1. current = queue.dequeue
# 2. loop through current edges 
# 3. if not visited:
#   enqueue the edges
#   add edges to visited 
# add current ID to result.



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
        return ''
    result = ''
    visited = set()
    
    q = deque(origin)
    while q:
        current = q.popleft()
        for child in origin.edges[current]:
            if child not in visited:
                q.append(child)
                visited.add(child)
                result += child
    return result

# DO NOT EDIT
# Vertex class for a graph vertex
class Vertex:
    def __init__(self, id=None):
        self.id = id
        self.edges = []
