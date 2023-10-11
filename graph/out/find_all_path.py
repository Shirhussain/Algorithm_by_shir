# INPUT: 
#               C
#             /   \
#     A --- B       E  --- F --- D
#             \   /   \   /
#               H       G

# Origin: (A)

# Destination: D

# OUTPUT: 

# ["ABCEFD", "ABCEGFD", "ABHEFD", "ABHEGFD"]

# EXPLANATION: 

# There are four paths from vertex A to vertex D. These four paths are listed above and then sorted within their array. 


#find all path


def find_all_paths(origin, destination):
    visited = set()
    result = []
    
    def traverse(current, path):
        if current is None:
            return 
        
        if current.id == destination:
            result.append(''.join(path))
            return 
        
        visited.add(current)
        
        for edge in current.edges:
            if edge not in visited:
                path.append(edge.id)
                traverse(edge, path)
                path.pop()
        
        visited.remove(current)
    traverse(origin, [origin.id])
    return result


class Vertex:
    def __init__(self, id=None):
        self.id = id
        self.edges = []
