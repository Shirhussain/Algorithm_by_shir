/*
Graph is a Tree ..?
Given an undirected graph in an adjacency list format (a map of every vertex to a list of all its neighboring vertices), determine whether or not said graph is a tree.

Input: Undirected Graph as an Adjacency List (Map<int, int[]>)
Output: Boolean
Example
Input:
 {
   0 : [1, 2, 3],
   1 : [0],
   2 : [0],
   3 : [0, 4],
   4 : [3]
 }
GraphIsTree1

Output: True

              0
          1    2   3
                   4


Input:
 {
   0 : [1, 2, 3],
   1 : [0, 2],
   2 : [0, 1],
   3 : [0, 4],
   4 : [3]
 }
GraphIsTree2

Output: False // Cycle between 0, 1, 2

               1 - 0 - 3
               | /     |
               2        4


Input:
 {
   0 : [1, 2, 3],
   1 : [0],
   2 : [0],
   3 : [0],
   4 : []
 }
GraphIsTree3

Output: False

              0
          1    2   3                  4


Whiteboarding
---
Understand
A tree
- Must not have any cycles
- And all vertices (nodes) are connected

Diagram

              0
          1   2   3
                  4

[0,1,2,3,4]
              

              2
              |
              0
            /   \
          1      3
                 4



               1 - 0 - 3
               | /     |
               2       4

[1,2,0,3,4]

DFS



Pseudocode
Template for DFS traversal of a graph
function graph_traversal_dfs(graph):
  visited = set()

  function dfs(node) {
    // visit node
    visited.add(node)

    for neighbor in neighbors(node) {
      if neighbor not in visited {
        dfs(node)
      }  
    }
  }

  for node in graph {
    if node not in visited {
      dfs(node)
    }
  }
}



function graphIsTree(graph) {
  if (Object.keys(graph).length == 0) {
    return true;
  }

  let visited = new Set();

  let hasCycle = false;

  function dfs(node) {
    visited.add(node);

    let visitCount = 0;

    for (neighbor of graph[node]) {
      if (neighbor === node) {
        hasCycle = true;
        return;
      }

      if (visited.has(neighbor)) {
        visitCount++;
      }

      if (visitCount >= 2) {
        hasCycle = true;
        return;
      }
    
    }

    for (neighbor of graph[node]) {
      if(!visited.has(neighbor)) {
        dfs(neighbor);
      }
    }
  
  }

  dfs(Object.keys(graph)[0]);

  return !hasCycle && visited.size == Object.keys(graph).length;
}

Code

*/

function graphIsATree(graph) {
  if (Object.keys(graph).length == 0) {
    return true;
  }

  let visited = new Set();

  let hasCycle = false;

  function dfs(node) {
    visited.add(node);

    let visitCount = 0;

    for (neighbor of graph[node]) {
      if (neighbor === node) {
        hasCycle = true;
        return;
      }

      if (visited.has(neighbor)) {
        visitCount++;
      }

      if (visitCount >= 2) {
        hasCycle = true;
        return;
      }
    }
    for (neighbor of graph[node]) {
      if (!visited.has(neighbor)) {
        dfs(neighbor);
      }
    }
  }

  dfs(Number(Object.keys(graph)[0]));
  return !hasCycle && visited.size == Object.keys(graph).length;
}

/*
  visited = [0, 1, 2, 3, 4]
  */

// No cycle, all nodes connected
let adjLst1 = {
  0: [1, 2, 3],
  1: [0],
  2: [0],
  3: [0, 4],
  4: [3],
};

/*
  [0,1]
  */
// Cycle (between 0, 1, 2)
let adjLst2 = {
  0: [1, 2, 3],
  1: [0, 5],
  2: [0, 5],
  3: [0, 4],
  4: [3],
  5: [1, 2],
};

/*
                0 - 2 - 5
                | \   /
                3   1
                |
                4
              
  */

// Disconnected node (5)
let adjLst3 = {
  0: [1, 2, 3],
  1: [0],
  2: [0],
  3: [0, 4],
  4: [3],
  5: [],
};

// Self cycle (0 <--> 0)
let adjLst4 = {
  0: [0],
};

let adjLst5 = {};

//console.log(graphIsATree(adjLst1)); // true
console.log(graphIsATree(adjLst2)); // false
/*console.log(graphIsATree(adjLst3)); // false
  console.log(graphIsATree(adjLst4)); // false
  console.log(graphIsATree(adjLst5)); // true*/
