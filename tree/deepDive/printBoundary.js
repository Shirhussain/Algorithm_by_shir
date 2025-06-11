/*
Given a binary tree, the task is to find the boundary nodes of the binary tree counter-clockwise starting from the root.

						1
      2						3
         4	    5			6
         						 7

1, 2, 4, 5, 7, 6, 3

*/

function TreeNode(val, left = null, right = null) {
  this.val = val;
  this.left = left;
  this.right = right;
}

// Print left boundary (excluding leaf nodes)
function leftTrav(node) {
  if (!node || (!node.left && !node.right)) {
    return;
  }

  console.log(node.val);

  if (node.left) {
    leftTrav(node.left);
  } else {
    leftTrav(node.right);
  }
}

// Print all leaf nodes
function bottomTraverse(node) {
  if (!node) {
    return;
  }

  if (!node.left && !node.right) {
    console.log(node.val);
    return;
  }

  bottomTraverse(node.left);
  bottomTraverse(node.right);
}

// Print right boundary in reverse (excluding leaf nodes)
function rightTraverse(node) {
  if (!node || (!node.left && !node.right)) {
    return;
  }

  if (node.right) {
    rightTraverse(node.right);
  } else {
    rightTraverse(node.left);
  }

  console.log(node.val); // reverse order
}

// Main function to print boundary in counter-clockwise order
function printBoundary(root) {
  if (!root) return;

  console.log(root.val); // Root always printed first

  leftTrav(root.left);
  bottomTraverse(root.left);
  bottomTraverse(root.right);
  rightTraverse(root.right);
}

const root = new TreeNode(1);
root.left = new TreeNode(2);
root.right = new TreeNode(3);
root.left.right = new TreeNode(4);
root.right.left = new TreeNode(6);
root.right.right = new TreeNode(5);
root.right.left.right = new TreeNode(7);

printBoundary(root);

//     1
//   /   \
//  2     3
//   \   / \
//    4 6   5
//       \
//        7

// with BFS

function TreeNode(val, left = null, right = null) {
  this.val = val;
  this.left = left;
  this.right = right;
}

function isLeaf(node) {
  return !node.left && !node.right;
}

function printBoundaryBFS(root) {
  if (!root) return;

  const leftBoundary = [];
  const rightBoundary = [];
  const leaves = [];

  if (!isLeaf(root)) console.log(root.val); // Print root first

  const queue = [root];

  while (queue.length) {
    const levelSize = queue.length;
    let first = null,
      last = null;

    for (let i = 0; i < levelSize; i++) {
      const node = queue.shift();

      if (i === 0) first = node;
      if (i === levelSize - 1) last = node;

      if (isLeaf(node)) {
        leaves.push(node.val);
      }

      if (node.left) queue.push(node.left);
      if (node.right) queue.push(node.right);
    }

    // Add to left boundary if not leaf and not root
    if (first !== root && !isLeaf(first)) leftBoundary.push(first.val);

    // Add to right boundary if not leaf and not root
    if (last !== root && last !== first && !isLeaf(last)) {
      rightBoundary.push(last.val);
    }
  }

  // Print boundaries
  leftBoundary.forEach((val) => console.log(val));
  leaves.forEach((val) => console.log(val));
  rightBoundary.reverse().forEach((val) => console.log(val));
}

console.log("BFS");
printBoundaryBFS(root);
