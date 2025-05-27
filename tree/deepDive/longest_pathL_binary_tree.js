/*
Longest Path of a Binary Tree
Given a binary tree node, return the number of nodes in the longest path between the root and a leaf node

Input: Node in a Binary Tree
Output: Integer
Example
Input: <BSTNode 1> =>   Output: 3 (from path 1--> 3--> 4)
LongestPathBinaryTree

Copy Pastable tree

            1
      /           \
      2           3
                      \
                      4

Output: 3


Whiteboarding
---
Understand
- Does the count start at 0 or 1?
1
- Do we include root node?
Yes
- What is the potential longest path?
tens
- Edge cases?
Yes
- Time and space complexity constraints?


Diagram

            1 max(1,2) + 1 = 3
      /1          \ 2
      2           3 max(0,1) + 1
   N     N      0/  \1
                N     4
+1  +1              N    N
1 -> 2 -> null
       -> null
  -> 3 -> null  
       -> 4 -> null
            -> null
Pseudocode

function outer(...) {
  [] //optional

  function recurse(...) {
    // Base case(s)

    // Preorder logic/visit

    // Left recursive

    // Inorder logic/visit

    // Right recursive

    // Postorder logic/visit
  }

  return recurse(...)
  OR
  recurse(...)
  return []
}


function longestPathBinaryTree(root) {

  function recurse(node) {
    // Base case(s)
    if (node === null) return 0;
    

    // Left recursive
    let left = recurse(node.left);

    // Right recursive
    let right = recurse(node.right);

    // Postorder logic/visit
    return Math.max(left, right) + 1;
  }

  return recurse(root);
}

Code

*/

// JavaScript

// DO NOT EDIT
// Node class for a binary tree node
class TreeNode {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

// DO NOT EDIT
// generate tree from array
function deserialize(arr) {
  if (arr.length === 0) {
    return null;
  }
  let root = new TreeNode(arr[0]);
  let queue = [root];
  for (let i = 1; i < arr.length; i += 2) {
    let current = queue.shift();
    if (arr[i] !== null) {
      current.left = new TreeNode(arr[i]);
      queue.push(current.left);
    }
    if (arr[i + 1] !== null && arr[i + 1] !== undefined) {
      current.right = new TreeNode(arr[i + 1]);
      queue.push(current.right);
    }
  }
  return root;
}

// DO NOT EDIT
// const arr = [4, 2, 5, 1, 3, null, 7, null, null, null, null, 6, 8];

// from example above
const arr = [1, 2, 3, null, null, null, 4];

const sampleTree = deserialize(arr);

/*
            1
      /           \
      2           3
                      \
                      4
*/

const longestPathBinaryTree = (root) => {
  function recurse(node) {
    // Base case(s)
    if (node === null) return 0;

    // Postorder logic/visit
    return Math.max(recurse(node.left), recurse(node.right)) + 1;
  }

  return recurse(root);
};

console.log(longestPathBinaryTree(sampleTree));

/*
Time: O(n)
Space: O(log(n)), O(n)
Question: Do you count the return value?
*/
