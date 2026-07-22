""" 
Input: Graph shown below, vertex A is the start, vertex F is the end

      A - B
    / |   |
  C   D   E
  |   | /
  F - G
  
Output: 2 Stops (From A stop at C, and then stop at F)


"""

edges = [("A","B"), ("A","C"), ("A","D"),
         ("B","E"), ("C","F"), ("D","G"),
         ("E","G"), ("F","G")]


start, end = "A", "F"


from collections import defaultdict, deque

def min_number_of_stops(edges, start, end):
    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    q = deque(graph[start])

    parent_dict = {}
    parent_dict[start] = None

    while q:
        node = q.popleft()
        if node == end:
            break

        for child in graph[node]:
            if child not in parent_dict:
                parent_dict[child] = node 
            q.append(child)

    last = end 
    path = []

    while last != None:
        path.append(last)
        last = parent_dict[last]
    return len(path) -1
    


def min_step(edges, start, end):
    graph = defaultdict(list)

    visted = set()

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    q = deque([(start, 0)])
    visted.add(start)

    while q:
        node, step = q.popleft()
        if node == end:
            return step

        for child in graph[node]:
            if child not in visted:
                q.append((child, step+1))
                visted.add(child)

print(min_step(edges, start, end))







        
    
    


print(min_step(edges, start, end))
    


