/*
Invert a Binary Tree
Given a binary tree root node, invert the binary tree (mirror) and return back the root node.

Input: Node in a Binary Tree
Output: Node in a Binary Tree
Example


Copy Pastable Input

              1
          /       \
        2           3
                /       \
               4         5
Copy Pastable Output

            1
        /         \
       3           2
    /     \
   5       4


Whiteboarding
---
Understand
- Time/Space complexity constraints?
- Edge cases? 1 node tree?

Diagram
BFS
[]



              1
          /       \
        3           2
    /       \
  5         4


Pseudocode
BFS Tree Traversal Template
function func(...) {
  q = []

  q.push(...)

  while len(q) {
    node = q.pop()

    // Preorder Logic

    for child in node.children {
      q.push(child)
    }
  }
  return ...
}


BFS
[]



              1
          /       \
        3           2
    /       \
  4          5



// DFS

// Preorder
function invert(root) {

  function recurse(node) {
    if (node === null) return;

    temp = node.left;
    node.left = node.right;
    node.right = temp;

    recurse(node.left);
    recurse(node.right);
  }
  
}

// Inorder
function invert(root) {

  function recurse(node) {
    if (node === null) return;



    recurse(node.left);

    temp = node.left;
    node.left = node.right;
    node.right = temp;
    
    recurse(node.left);
  }
  
}


// Postorder
function invert(root) {

  function recurse(node) {
    if (node === null) return;

    recurse(node.left);
    recurse(node.right);

    temp = node.left;
    node.left = node.right;
    node.right = temp;
  }
  
}


//BFS
function invert(root) {
  q = [root];

  while (q.length) {
    node = q.shift();

    // Preorder Logic
    temp = node.left;
    node.left = node.right;
    node.right = temp;

    q.push(node.right);
    q.push(node.left);
  }
  return root;
}

Code

*/

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
const arr = [1, 2, 3, 7, 8, 4, 5, null, null, null, null];

const sampleTree = deserialize(arr);

const invert = (root) => {
  q = [root];

  while (q.length) {
    node = q.shift();

    // Swap left, right
    temp = node.left;
    node.left = node.right;
    node.right = temp;

    /*
    node.left, node.right = node.right, node.left

    [node.left, node.right] = [node.right, node.left]
    */

    if (node.right !== null) q.push(node.right);
    if (node.left !== null) q.push(node.left);
  }
  return root;
};

//console.log(invert(sampleTree))

/*
Time: O(n)
Space: O(MaxTreeWidth) => O(n)

Question: Return? 

32 deep binary how many nodes are leaves?
2^31
*/

/*
              1
          /       \
        2           3
    7       8   /       \
               4         5

1,2,3,4,5 (pre)
2,1,4,3,5 (in)
2,4,5,3,1 (post)
*/

function printPre(root) {
  function recurse(node) {
    if (node === null) return;

    recurse(node.left);

    recurse(node.right);

    console.log(node.value);
  }

  recurse(root);
}

printPre(sampleTree);
