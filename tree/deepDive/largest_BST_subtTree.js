/*
Given a Binary Tree, find the size of the largest subtree which is also a Binary Search Tree (BST)


								6
          3						4
    1         5    
    
Output: 3

          3			
    1         5
    
*/

class Node {
  constructor(value, left = null, right = null) {
    this.value = value;
    this.left = left;
    this.right = right;
  }
}

class IsBST {
  constructor(min, max, size) {
    this.min = min;
    this.max = max;
    this.size = size;
  }
}

function findLargestBSTSubtree(root) {
  if (!root) {
    return new IsBST(-Infinity, Infinity, 0);
  }

  // doing post order
  const left = findLargestBSTSubtree(root.left);
  const right = findLargestBSTSubtree(root.right);

  if (left.max < root.value && right.min > root.value) {
    return new IsBST(
      Math.min(left.min, root.value),
      Math.max(right.max, root.value),
      left.size + right.size + 1
    );
  }

  // When a subtree is invalid, we want it to fail BST checks for its parent nodes
  // Setting min = Infinity and max = -Infinity ensures that
  return new IsBST(Infinity, -Infinity, Math.max(left.size, right.size));
}

function largestBSTSubtree(root) {
  return findLargestBSTSubtree(root).size;
}

const root = new Node(6, new Node(3, new Node(1), new Node(5)), new Node(4));

console.log(findLargestBSTSubtree(root));
console.log(largestBSTSubtree(root));
