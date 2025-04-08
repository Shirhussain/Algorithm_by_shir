"""   v
 > 1   2   3
   4   0   9
   7   6   5

Output: 10

bfs(matrix, (0,2), (1,0))
queue: []
location: (0,2)
distance: 0


shortestPathFromsTot(matrix, start_location, finish_location):
    bfs(matrix, start_location, finish_location):
        create an empty queue
        place start_location with distance 0 in queue
        mark matrix at start_location as visited 
        while queue is not empty
            get location and distance from front of queue
            if location is finish_location
                return distance
            add each unmarked neighbor to the queue and mark them.
            set their distance to 1 greater than the current distance.
        return -1

    path_length = bfs(start_location, finish_location) 
    if path_length is -1, return (false, -1)
    unmark the matrix (negate all negative numbers)
    return (true, path_length)

                                                        i
heightsAndLocs: [[2, (0,1)], [3, (0,2)], [4, (1,0)], [5, (2,2)], [6, (2,1)], [7, (2,0)]]
i: 1
steps: 5

Add min # steps from (0,0) to (0,1) to steps
increment i
Add min # steps from (0,1) to (0,2) to steps
increment i
Add min # steps from (0,2) to (1,0) to steps
increment i
*/

/*

heightsAndLocs = produceASortedListofTreeHeightsAndCoordinates()
set steps to 0
set prevLocation to (0,0)
for i index in heightsAndLocs
  (succeed, pathLength) = shortestPathFromsTot(matrix, prevLocation, heightsAndLocs[i])
  if does not succeed return -1
  add pathLength to steps
return steps


produceASortedListofTreeHeightsAndCoordinates
simple traversal + sort
time: O(n^2 log n)

shortestPathFromsTot



"""
