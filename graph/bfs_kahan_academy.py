from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, obj):
        self.items.append(obj)

    def dequeue(self):
        return self.items.popleft()

    def is_empty(self):
        return len(self.items) == 0


def do_bfs(graph, source):
    bfs_info = []

    for i in range(len(graph)):
        bfs_info.append({
            'distance': None,
            'predecessor': None
        })

    bfs_info[source]['distance'] = 0

    queue = Queue()
    queue.enqueue(source)

    while not queue.is_empty():
        current = queue.dequeue()
        neighbors = graph[current]

        for neighbor in neighbors:
            if bfs_info[neighbor]['distance'] is None:
                bfs_info[neighbor]['distance'] = bfs_info[current]['distance'] + 1
                bfs_info[neighbor]['predecessor'] = current
                queue.enqueue(neighbor)

    return bfs_info


adj_list = [
    [1],
    [0, 4, 5],
    [3, 4, 5],
    [2, 6],
    [1, 2],
    [1, 2, 6],
    [3, 5],
    []
]

bfs_info = do_bfs(adj_list, 3)

for i in range(len(adj_list)):
    print(
        f"vertex {i}: distance = {bfs_info[i]['distance']}, predecessor = {bfs_info[i]['predecessor']}")
