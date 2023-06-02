input = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

    
def robot_paths(matrix):
    result = 0
    
    def traverse(row, col):
        # it works in java but here it's not working
        nonlocal result
        
        # out fo bound for every matrix
        if (row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0])):
            return 
        
        # already visited --> when we are visiting then putting that cell =1 
        if matrix[row][col] == 1:
            return 
        
        # reach to destination
        if (row == len(matrix) -1) and (col == len(matrix[0])-1):
            result += 1
            return 
        
        # when I visit then put cell =1
        matrix[row][col] = 1
        
        # then move to for direction (N,S,W,E) each time to find a path
        traverse(row - 1, col)  # Up
        traverse(row + 1, col)  # Down
        traverse(row, col - 1)  # Left
        traverse(row, col + 1)  # Right

    traverse(0,0)
    return result

print(robot_paths(input))