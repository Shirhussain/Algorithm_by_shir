# A city planning department is working with a map of a large urban area. The map
# is divided into a grid, where each cell represents a block in the city. The
# cells are marked as either 'P' (park) or 'B' (building). The department wants to
# determine the number of distinct park areas in the city.

# A park area is defined as a contiguous group of park blocks ('P') that are
# connected either horizontally or vertically. Blocks marked as 'B' (buildings) do
# not count as part of a park area. The city is surrounded by a river, which means
# that any park area is also surrounded by buildings or the city boundary.

# Example 1:

# Input: cityMap = [
# ["P","P","P","P","B"],
# ["P","P","B","P","B"],
# ["P","P","B","B","B"],
# ["B","B","B","B","B"]
# ]
# Output: 1

# Example 2:

# Input: cityMap = [
# ["P","P","B","B","B"],
# ["P","P","B","B","B"],
# ["B","B","P","B","B"],
# ["B","B","B","P","P"]
# ]
# Output: 3

# Step 1:
# V: Each cell is a vertex.
# E: Each node is potentially connected to top/left/right/bottm if they are the same.

# Now map this to finding connected components:
# 1. DFS from one of the unvisited nodes
# 2. All the nodes that are visited would be in the same connected component
# 3. Repeate until no node remains unvisited.
# 4. Return how many times we ran DFS until all nodes were visited.


def count_parking_area(city_map):
    num_row = len(city_map)
    num_col = len(city_map[0])
    num_parking = 0

    def dfs(row, col):
        # base case
        if row < 0 or col < 0 or row >= num_row or col >= num_col or city_map[row][col] != 'P':
            return
        city_map[row][col] = "visited"

        # explore the neighbors
        dfs(row+1, col)
        dfs(row-1, col)
        dfs(row, col+1)
        dfs(row, col-1)

    for row in range(num_row):
        for col in range(num_col):
            if city_map[row][col] == 'P':
                num_parking += 1
                dfs(row, col)
    return num_parking


cityMap1 = [
    ["P", "P", "P", "P", "B"],
    ["P", "P", "B", "P", "B"],
    ["P", "P", "B", "B", "B"],
    ["B", "B", "B", "B", "B"],
]

cityMap2 = [
    ["P", "P", "B", "B", "B"],
    ["P", "P", "B", "B", "B"],
    ["B", "B", "P", "B", "B"],
    ["B", "B", "B", "P", "P"],
]

print(count_parking_area(cityMap1))
print(count_parking_area(cityMap2))
