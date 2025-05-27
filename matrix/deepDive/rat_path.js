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

// Approach: Start DFS from node 0, 0 and stop at (m-1, n-1). If there is no path, return (-1,-1)

// Test cases
// Base case

// 	# 0. If (node is leaf) :
// 	#	 Maybe store some value do some calculation
// 	#    	 return
// # 1. Mark node as visited
// # 2. for (neighbors n of node):
// #	  if ( n is not an answer) :
// #		continue // Backtracking!

// #      if(n is not visited) :
// #        Adjust auxiliary variables
// # 	   DFS(n)
// #        undo Adjust auxiliary variables
function ratPath(maze) {
  let result = [[-1, -1]];
  let curPath = [[0, 0]];
  let di = [1, 0];
  let dj = [0, 1];
  function dfs(row, col) {
    // This was actually correct, not sure what happened during the lectrue!
    // As soon as we find the result, we should return and discontinue DFS.
    if (result[0][0] !== -1) {
      return;
    }

    // Check for leaf AKA base case
    if (row === maze.length - 1 && col === maze[0].length - 1) {
      // Deep copy curPath to result
      result = curPath.map((item) => (Array.isArray(item) ? [...item] : item));
      return;
    }

    for (let k = 0; k < di.length; k++) {
      let newRow = row + di[k];
      let newCol = col + dj[k];

      if (newRow >= maze.length || newCol >= maze[0].length) {
        continue;
      }

      if (maze[newRow][newCol] === 1) {
        continue;
      }

      curPath.push([newRow, newCol]);
      dfs(newRow, newCol);
      curPath.pop();
    }
  }
  dfs(0, 0);
  return result;
}

const maze2 = [
  [0, 0, 0],
  [0, 1, 1],
  [0, 0, 0],
];
console.log(ratPath(maze2));

const maze5 = [
  [0, 1, 0, 0],
  [0, 1, 1, 0],
  [0, 0, 0, 1],
  [0, 1, 0, 0],
];
console.log(ratPath(maze5));
