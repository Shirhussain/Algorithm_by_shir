/*
Imagine there is an unknown latin-based language that has reordered the alphabet.
Given an array of words in order and k which is the total unique characters,
determine the order of character for this language. If no valid ordering is possible, return empty.

Input:  arr = [“caa”, “aaa”, “aab”], k = 3
Output: "cab"


"abcdefgh..."

"ant", "bat"


1.) Create a graph. Directed graph. Each node represents one character, and the edges represent the orderings of characters

    c  ->  a  ->  b
    
    Adjacency list
    
2.) Check if there are cycles

	DFS

3.) We perform topological sorting to the graph

Input:
     a -> e -> f ----v
           \-> g   -> s

    1.) Has to be directed
    2.) Can't have cycles
    
Output:
	Nodes of the graph in order based off of the edges

  a,e,f,g,s

[
'c' -> ['a']
'a' -> ['b']

]

*/

function orderedAlpha(arr, k) {
  // Initialize adjacency list as object
  const adj = {};

  // Initialize adj list for all possible characters
  for (let i = 0; i < k; i++) {
    const char = String.fromCharCode(97 + i); // a,b,c...
    adj[char] = [];
  }

  // Loop through all words up to arr.length - 1
  for (let i = 0; i < arr.length - 1; i++) {
    const word1 = arr[i];
    const word2 = arr[i + 1];

    let j = 0;
    // Loop through each char and check if they are different
    while (j < word1.length && j < word2.length) {
      if (word1[j] !== word2[j]) {
        if (!adj[word1[j]].includes(word2[j])) {
          adj[word1[j]].push(word2[j]);
        }
        break;
      }
      j++;
    }
  }

  // Initialize visited as object
  const visited = {};
  const inProcess = {};

  // Check for cycles
  for (const char of Object.keys(adj)) {
    if (checkCycle(adj, visited, inProcess, char)) {
      return "";
    }
  }

  // Reset visited for topological sort
  for (const char of Object.keys(adj)) {
    visited[char] = false;
  }

  const stack = [];
  // Perform topological sort
  for (const char of Object.keys(adj)) {
    if (!visited[char]) {
      topologicalSort(adj, visited, char, stack);
    }
  }

  return stack.reverse().join("");
}

function checkCycle(adj, visited, inProcess, char) {
  visited[char] = true;
  inProcess[char] = true;

  for (const neighbor of adj[char]) {
    if (!visited[neighbor]) {
      if (checkCycle(adj, visited, inProcess, neighbor)) {
        return true;
      }
    } else if (inProcess[neighbor]) {
      return true;
    }
  }

  inProcess[char] = false;
  return false;
}

function topologicalSort(adj, visited, char, stack) {
  visited[char] = true;

  for (const neighbor of adj[char]) {
    if (!visited[neighbor]) {
      topologicalSort(adj, visited, neighbor, stack);
    }
  }

  stack.push(char);
}

console.log(orderedAlpha(["caa", "aaa", "aab"], 3));
