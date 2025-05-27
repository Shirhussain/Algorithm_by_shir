/*
Shortest Route
Given an unweighted, undirected graph which represents a metro map as follows

vertices are stations
edges are the path between two stations
Given a start station and ending station, determine the minimum number of stops that must be made to get to the destination.

Input: A Graph (unweighted/undirected), a starting Vertex, and an ending Vertex
Output: Integer
Example
Input: The graph represented below, Vertex A, Vertex F
Shortest Route


              A - B
            / |   |
          C   D   E
          |   |   /
          F  -  G
Output: 2 Stops (From A stop at C, and then stop F

Whiteboarding
---
Understand
- Will there always be path from v1 to v2?
Yes
- Number of vertices?
Fit in memory
- v1 and v2 can be same?
Yes

Find longest acyclic path from v1 to v2

Diagram

              A - B
            / |   |
          C   D   E
          |   |   /
          F  -  G

          q = [[F,2], [E,2], G[2]]

          
          visited = [A, B, D]

          A -> F


Pseudocode
Template for BFS Graph traversal
function graph_traversal_bfs(graph) {
  visited = set()

  q = [];


  for node in graph {
    if (node not in visited)
      q.push(node)
    while len(queue)  {
      node = q.pop()
  
      for neighbors in get_neighbors(node) {
        if neighbor not in visited
          q.push(neighbor)
      }
    }
  }
}


class Graph {
  constructor(v) {
    this.V = v;
    this.adj = new Array(v);
    for (let i = 0; i < v; i++) {
      this.adj[i] = [];
    }
  }

  addEdge(v, w) {
    this.adj[v].push(w);
  }

  bfs(s, e) {
    let visited = new Array(this.V);

    for(let i = 0; i < this.V; i++) {
      visited[i] = false;
    }

    let q = [];

    visited[s] = true;
    q.push([s, 0])

    while(q.length > 0) {
      [node, count] = queue.shift();
      if (node === e) {
        return count;
      }

      this.adj[node].forEach((adjacent, i) => {
        if(!visited[adjacent]) {
          visited[adjacent] = true;
          q.push([adjacent, count + 1]);
        }
      }); 
    }
    
  }

}



Code

*/

class Graph {
  constructor(v) {
    this.V = v;
    this.adj = new Array(v);
    for (let i = 0; i < v; i++) {
      this.adj[i] = [];
    }
  }

  addEdge(v, w) {
    this.adj[v].push(w);
  }

  bfs(s, e) {
    //let visited = new Array(this.V);

    //for(let i = 0; i < this.V; i++) {
    //visited[i] = false;
    //}

    let q = [];

    //visited[s] = true;
    q.push([s, 0]);

    while (q.length > 0) {
      let [node, count] = q.shift();
      if (node === e) {
        return count;
      }

      this.adj[node].forEach((adjacent, i) => {
        //if(!visited[adjacent]) {
        //visited[adjacent] = true;
        q.push([adjacent, count + 1]);
        //}
      });
    }
  }
}

g = new Graph(4);
g.addEdge(0, 1);
g.addEdge(1, 0);
g.addEdge(0, 2);
g.addEdge(1, 2);
g.addEdge(2, 1);
g.addEdge(2, 0);
g.addEdge(2, 3);
g.addEdge(3, 2);
g.addEdge(3, 3);
g.addEdge(0, 3);
g.addEdge(3, 0);

console.log(g.bfs(0, 3));
/*
  
          0 - 1
          | \ |
          3 - 2
  
          [ [2,2], [3,2]]
          [0,1,2]
  
  Time: O(n)
  Space: O(n)
  */
