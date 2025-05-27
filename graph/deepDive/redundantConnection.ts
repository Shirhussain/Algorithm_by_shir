/*
Redundant Connection


In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

 

Example 1:

Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]

Example 2:

Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]



*/

const edges = [
  [1, 2],
  [1, 3],
  [2, 3],
];

class UnionFind {
  parent: number[];

  constructor(size) {
    this.parent = [];
    for (let i = 0; i <= size; i++) {
      this.parent.push(i);
    }
  }

  find(x) {
    if (this.parent[x] !== x) {
      this.parent[x] = this.find(this.parent[x]);
    }
    return this.parent[x];
  }

  union(u, v) {
    const root_u = this.find(u);
    const root_v = this.find(v);
    if (root_u === root_v) {
      return false;
    }
    this.parent[root_u] = root_v;
    return true;
  }
}

const redundantConnection = (graph: number[][]): number[] => {
  const uf = new UnionFind(graph.length);
  for (const [u, v] of graph) {
    if (!uf.union(u, v)) {
      return [u, v];
    }
  }
  return [];
};

console.log(redundantConnection(edges));
