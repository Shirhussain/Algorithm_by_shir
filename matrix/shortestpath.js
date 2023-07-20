// Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

// A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

// All the visited cells of the path are 0.
// All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
// The length of a clear path is the number of visited cells of this path.

// Input: grid = [[0,1],[1,0]]
// Output: 2

//leetcode.com/problems/shortest-path-in-binary-matrix/

https: var shortestPathBinaryMatrix = function (grid) {
  if (grid[0][0] === 1) return -1;

  const queue = [[0, 0, 1]];
  const directions = [
    [-1, 0],
    [-1, 1],
    [0, 1],
    [1, 1],
    [1, 0],
    [1, -1],
    [0, -1],
    [-1, -1],
  ];

  while (queue.length > 0) {
    const [currX, currY, currCount] = queue.shift();

    if (
      currX < 0 ||
      currY < 0 ||
      currX > grid.length - 1 ||
      currY > grid[0].length - 1 ||
      grid[currX][currY] === 1
    ) {
      continue;
    }

    if (currX === grid.length - 1 && currY === grid[0].length - 1) {
      return currCount;
    }

    grid[currX][currY] = 1; // Mark as visited

    directions.forEach((direction) => {
      const [x, y] = direction;
      queue.push([currX + x, currY + y, currCount + 1]);
    });
  }

  return -1;
};
