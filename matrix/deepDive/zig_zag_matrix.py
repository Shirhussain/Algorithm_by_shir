'''
https://www.geeksforgeeks.org/print-matrix-in-zig-zag-fashion/

Given a matrix of 2D array of n rows and m columns. Print this matrix in 
ZIG-ZAG fashion as shown in figure. 


  [[1,  2,  3], 
   [5,  6,  7],
   [9,  10,11],
   [13, 14,15]]

queue: [(9, (2,0), 2), (6, (1,1), 2), (3, (0,2), 2)]
output_list: [1, 2, 5]
level_list: [9]
prev_level: 2
value: 9
level: 2
i,j: 2,0
visited_set: {1, 5, 2, 9, 6, 3}

'''

'''
Pseudocode

  bfs_with_revesal(matrix):
    create an empty queue
    create empty output_list
    enqueue (matrix[0,0], (0,0), 0)
    add matrix[0,0] to visited_set
    set prev_level to 0
    create empty level_list
    create empty visited_set
    while queue is not empty
      dequeue value, (i,j), level
      if level is not equal to prev_level
        if prev_level is odd
           reverse level_list
        append level_list to output_list
        clear level_list
        set prev_level to level
      add value to level_list
      add each child of (i,j) that has not been visited to queue and visited_set
    if prev_level is odd
       reverse level_list
    append level_list to output_list

    return output_list
    
'''




from collections import deque
def bfs_with_reversal(matrix):
    if not matrix or not matrix[0]:
        return []

    rows = len(matrix)
    cols = len(matrix[0])

    # Initialize queue, output list, and visited set
    queue = deque([(matrix[0][0], (0, 0), 0)])
    output_list = []
    visited_set = {(0, 0)}
    prev_level = 0
    level_list = []

    # Define possible movements (right and down)
    directions = [(0, 1), (1, 0)]  # right and down movements

    while queue:
        value, (i, j), level = queue.popleft()

        # If we're at a new level
        if level != prev_level:
            if prev_level % 2 == 1:  # if previous level was odd
                level_list.reverse()
            output_list.extend(level_list)
            level_list = []
            prev_level = level

        level_list.append(value)

        # Add children
        for di, dj in directions:
            new_i, new_j = i + di, j + dj

            # Check if the new position is valid and not visited
            if (0 <= new_i < rows and
                0 <= new_j < cols and
                    (new_i, new_j) not in visited_set):

                queue.append((matrix[new_i][new_j], (new_i, new_j), level + 1))
                visited_set.add((new_i, new_j))

    # Handle the last level
    if prev_level % 2 == 1:
        level_list.reverse()
    output_list.extend(level_list)

    return output_list

# Test the function


def main():
    matrix = [
        [1,  2,  3],
        [5,  6,  7],
        [9,  10, 11],
        [13, 14, 15]
    ]

    result = bfs_with_reversal(matrix)
    print("Zig-zag traversal:", result)


if __name__ == "__main__":
    main()
