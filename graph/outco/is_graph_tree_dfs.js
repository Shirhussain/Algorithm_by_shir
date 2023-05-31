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

                    0
                1   2    3
                            4


                    3
               0         4
          1        2
 
GraphIsTree1

Output: True
Input:
 {
   0 : [1, 2, 3],
   1 : [0, 2],
   2 : [0, 1],
   3 : [0, 4],
   4 : [3]
 }

  1  -  0   -  3
  |  /         |
  2            4
GraphIsTree2

Output: False // Cycle between 0, 1, 2
Input:
 {
   0 : [1, 2, 3],
   1 : [0],
   2 : [0],
   3 : [0],
   4 : []
 }

            0
        1   2   3               4 - 5


 
GraphIsTree3

Output: False // Island node


Two properties of a Tree
1.) No cycles
2.) Every node connected to each other



Set:
Random lookup: O(1)


TEMPLATE FOR DFS
function graph_transversal_recursive(graph){
  visited = set()

  function helper_dfs(node) {
    visited.add(node)
    for child in node {
      if child not in visited {
        helper_dfs(child)
      }
        
    }
  }

  helper_dfs(graph[0])
}


Input:
 {
   0 : [1, 2, 3],
   1 : [0],
   2 : [0],
   3 : [0, 4],
   4 : [3]
 }

 visited = [0,1,2,3,4]
 hasCycle = false
 visitedCnt = 1
*/

function graphIsATree(graph) {
  if (Object.keys(graph).length == 0) {
    return true;
  }

  let hasCycle = false;

  visited = new Set();

  function helper_dfs(node) {
    visited.add(node);
    let visitCnt = 0;

    for (const neighbor of graph[node]) {
      if (neighbor === node) {
        hasCycle = true;
        return;
      }

      if (visited.has(neighbor)) {
        visitCnt++;
      }

      if (visitCnt >= 2) {
        hasCycle = true;
        return;
      }
    }

    for (const neighbor of graph[node]) {
      if (!visited.has(neighbor)) {
        helper_dfs(neighbor);
      }
    }
  }

  helper_dfs(Number(Object.keys(graph)[5]));

  // After our DFS, check if visited has all nodes in graph
  const allVisited = visited.size == Object.keys(graph).length;
  console.log(visited.size);
  console.log(Object.keys(graph).length);
  return !hasCycle && allVisited;
}

// No cycle, all nodes connected
let adjLst1 = {
  0: [1, 2, 3],
  1: [0],
  2: [0],
  3: [0, 4],
  4: [3],
};

// Cycle (between 0, 1, 2)
let adjLst2 = {
  0: [1, 2, 3],
  1: [0, 2],
  2: [0, 1],
  3: [0, 4],
  4: [3],
};

// Disconnected node (5)
let adjLst3 = {
  0: [1, 2, 3],
  1: [0],
  2: [0],
  3: [0, 4],
  4: [3],
  5: [6],
  6: [5],
};

//console.log(graphIsATree(adjLst1)); // true
//console.log(graphIsATree(adjLst2)); // false
console.log(graphIsATree(adjLst3)); // false

/*
  
  Time: O(v + e)
  Space: O(log(v)) O(v)
  */
