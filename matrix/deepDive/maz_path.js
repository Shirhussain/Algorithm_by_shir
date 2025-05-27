/*
Given a maze, represented by a matrix of bits (values 0 and 1), a rat must find a path from index [0][0] to [n-1][m-1]. The rat can only travel to the right or down, and can only travel on 0 values. 1 values represent walls.

Input:   maze (Matrix of elements with values either 0 or 1)
Output:  Array of two-item arrays indicating the path.
Example
Input:   [[0, 0, 0, 1],
          [0, 1, 0, 1],
          [0, 1, 0, 0],
          [0, 0, 1, 0]]

Output:  [[0, 0],
          [0, 1],
          [0, 2],
          [1, 2],
          [2, 2],
          [2, 3],
          [3, 3]]

          */
// Solution:
// We map this to a graph:
// 1. V: each cell (i,j) in he matrix is a node
// 2. E: There is an edge between each 0 node u=(i,j) to its right and down provided that they are not blocked
// The path from (0,0) to (m-1, n-1) can be found by either DFS or BFS.
// Remember that BFS can find the shortest path (when the graph is unweighted, which is the case here.)

function ratPath(maze) {
  const m = maze.length;
  const n = maze[0].length; // assume maze is non-empty
  let path = [[0, 0]];
  let result = [];
  function isSafeAndNotBlocked(i, j) {
    if (i < 0 || i >= m) {
      return false;
    }

    if (j < 0 || j >= n) {
      return false;
    }

    return maze[i][j] === 0;
  }

  function dfs(i, j) {
    // Base
    if (i === m - 1 && j === n - 1) {
      // Deep copy of path to result;
      result = path.map((e) => (Array.isArray(e) ? [...e] : e));
      return;
    }

    // Check the children
    let newI;
    let newJ;

    // Right child:
    newI = i;
    newJ = j + 1;
    if (isSafeAndNotBlocked(newI, newJ)) {
      // Adjusting your auxiliary variables (aka state).
      path.push([newI, newJ]);
      dfs(newI, newJ);
      // Resetting your auxiliary variables (aka state).
      path.pop();
    }

    // Bottom child:
    newI = i + 1;
    newJ = j;
    if (isSafeAndNotBlocked(newI, newJ)) {
      // Adjusting your auxiliary variables (aka state).
      path.push([newI, newJ]);
      dfs(newI, newJ);
      // Resetting your auxiliary variables (aka state).
      path.pop();
    }
  }
  dfs(0, 0);
  return result;
}

console.log(
  "-----------------------------------------------------------------------------"
);
const maze2 = [
  [0, 0, 0],
  [0, 1, 1],
  [0, 0, 0],
];
console.log(ratPath(maze2));

const maze5 = [
  [0, 0, 0, 0],
  [0, 1, 1, 0],
  [0, 0, 0, 0],
  [0, 1, 0, 0],
];
console.log(ratPath(maze5));
