/*
  You are given a list of n tasks labeled from 0 to n - 1. Some tasks may have
dependencies, which are expressed as a pair [a, b], meaning task a must be
completed before task b. Given the total number of tasks and a list of
dependency pairs, return an ordering of tasks such that all tasks can be
completed if possible, or return an empty list if it is not possible to complete
all tasks. This problem can be solved using topological sorting with DFS.

  Example:

  Input: n = 4, dependencies = [[1,0],[2,0],[3,1],[3,2]]
  Output: [0, 1, 2, 3] or [0, 2, 1, 3]

  Explanation: There are a total of 4 tasks to do. To do task 3, you should have
finished both tasks 1 and 2. Both tasks 1 and 2 should be done after you
finished task 0. So one correct task order is [0, 1, 2, 3].

For simplicity, let's assume the first node is always 0.

Solve this using DFS.
*/
#include <iostream>
#include <map>
#include <set>
#include <vector>

// V: is {0, ..., n-1}
// E: is given as dependancies
// Represent the graph as adjacency list (because this would be conveninent for
// DFS)
std::vector<int> topo_sort;

std::vector<int> DFS(int start, std::map<int, std::set<int>> &adj_list)
{
    // base case
    if (Visited(start))
    {
        return;
    }
    MarkAsVisited(start);
    for (auto n : adj_list[start])
    {
        DFS(n, adj_list);
    }
    topo_sort.push_back(n);
}

std::vector<int> TopologicalSort(int n,
                                 std::vector<std::vector<int>> &dependancies)
{
    std::vector<int> result;
    std::map<int, std::set<int>> adj_list = ConvertToAdjacencyList(dependancies);

    if (ThereIsACycle(adj_list))
    {
        return result;
    }

    result = DFS(/*start=*/0, adj_list);
    return Reverse(result);
}
0, 1, 2, 3, 4 0 [1 0] 1 []