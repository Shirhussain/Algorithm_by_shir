# from this youtube: https://www.youtube.com/watch?v=JWP9EI88Yoo&t=1s

# while the queue is not empyt:
    # we deque a node 
    # print it 
    # we queue the children
    

def bfs(root):
    if root is None:
        return 
    queue = [root]
    while queue:
        popped = queue.pop(0)
        print(popped.data)
        for child in popped.children:
            queue.append(child)
        
        # or queue.extend(iter(popped.children))
        
    
def bfs(graph; Graph, root: int):
    queue = [root]
    enqueue = {root}
    
    i = 0 
    while i <= len(queue):
        popped = queue[i]
        i += 1
        print(popped)
        for neighbor in graph.adjList[popped]:
            if neighbor not in enqueued:
                queue.append(neighbor)
                enqueue.add(neighbor)
        