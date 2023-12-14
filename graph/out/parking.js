/*
A city planning department is working with a map of a large urban area. The map
is divided into a grid, where each cell represents a block in the city. The
cells are marked as either 'P' (park) or 'B' (building). The department wants to
determine the number of distinct park areas in the city.

A park area is defined as a contiguous group of park blocks ('P') that are
connected either horizontally or vertically. Blocks marked as 'B' (buildings) do
not count as part of a park area. The city is surrounded by a river, which means
that any park area is also surrounded by buildings or the city boundary.

Example 1:

Input: cityMap = [
["P","P","P","P","B"],
["P","P","B","P","B"],
["P","P","B","B","B"],
["B","B","B","B","B"]
]
Output: 1

Example 2:

Input: cityMap = [
["P","P","B","B","B"],
["P","P","B","B","B"],
["B","B","P","B","B"],
["B","B","B","P","P"]
]
Output: 3
*/
/*
Step 1:
V: Each cell is a vertex.
E: Each node is potentially connected to top/left/right/bottm if they are the same.

Now map this to finding connected components:
1. DFS from one of the unvisited nodes
2. All the nodes that are visited would be in the same connected component
3. Repeate until no node remains unvisited.
4. Return how many times we ran DFS until all nodes were visited.
*/

function countParkAreas(cityMap) {
  let rowCount = cityMap.length;
  let colCount = cityMap[0].length;
  let parkCount = 0;

  function dfs(row, col) {
    // base case:
    if (
      row < 0 ||
      col < 0 ||
      row >= rowCount ||
      col >= colCount ||
      cityMap[row][col] != "P"
    ) {
      return;
    }

    cityMap[row][col] = "visited";

    // Explore neighbors:
    dfs(row + 1, col);
    dfs(row - 1, col);
    dfs(row, col + 1);
    dfs(row, col - 1);
  }

  for (let row = 0; row < rowCount; row++) {
    for (let col = 0; col < colCount; col++) {
      if (cityMap[row][col] === "P") {
        parkCount++;
        dfs(row, col);
      }
    }
  }

  return parkCount;
}

let cityMap1 = [
  ["P", "P", "P", "P", "B"],
  ["P", "P", "B", "P", "B"],
  ["P", "P", "B", "B", "B"],
  ["B", "B", "B", "B", "B"],
];
console.log(countParkAreas(cityMap1)); // Expected output: 1

let cityMap2 = [
  ["P", "P", "B", "B", "B"],
  ["P", "P", "B", "B", "B"],
  ["B", "B", "P", "B", "B"],
  ["B", "B", "B", "P", "P"],
];
console.log(countParkAreas(cityMap2)); // Expected output: 3
