/*
Given a binary tree, print boundary nodes of the binary tree Anti-Clockwise starting from the root.

 The boundary includes 

left boundary (nodes on left excluding leaf nodes)
leaves (consist of only the leaf nodes)
right boundary (nodes on right excluding leaf nodes)

                  20
            8              22
        4      12              25
            10     14

20, 8, 4, 10, 14, 25, 22

Understand
 1
 2
 3
 4
 5

 1

 How big is tree?
 fit in memory

Diagram

                  20
            8              22
        4        12              25
          5   10   14
           3  
            11
              13
20,8,4,5,3,2,10,14,25,22

Pseudocode

class Node {
  constructor(val) {
    this.left = null
    this.right = null
    this.val = val
  }

}

function printLeft(node) {
  // Base case
  if (node == null) return

  // Recursive case
  if (node.left != null) {
    console.log(node.val)
    printLeft(node.left)
  }
  else if (node.right != null) {
    console.log(node.val)
    printLeft(node.right)
  }
}

function printRight(node) {
  // Base case
  if (node == null) return

  // Recursive case
  if (node.right != null) {
    printRight(node.right) 
    console.log(node.val)
  }
  else if (node.left != null) {
    printRight(node.left)
    console.log(node.val)
  }
}

function printLeaves(node) {
  // Base case
  if (node == null) return

  // Recursive case

  printLeaves(node.left)

  if (node.left == null && node.right == null) {
    console.log(node.val)
  }

  printLeaves(node.right)
}

let root = new Node(20)
root.left = new Node(8)
root.left.left = new Node(4)
root.left.right = new Node(12)
root.left.right.left = new Node(10)
root.left.right.right = new Node(14)
root.right = new Node(22)
root.right.right = new Node(25)
console.log(root.val)

printLeft(root.left)
printLeaves(root)
printRight(root.right)

Code

                  20
            8              22
        4      12              25
            10     14
*/

class Node {
  constructor(val) {
    this.left = null;
    this.right = null;
    this.val = val;
  }
}

function printLeft(node) {
  // Base case
  if (node == null) return;

  // Recursive case
  if (node.left != null) {
    console.log(node.val);
    printLeft(node.left);
  } else if (node.right != null) {
    console.log(node.val);
    printLeft(node.right);
  }
}

function printRight(node) {
  // Base case
  if (node == null) return;

  // Recursive case
  if (node.right != null) {
    printRight(node.right);
    console.log(node.val);
  } else if (node.left != null) {
    printRight(node.left);
    console.log(node.val);
  }
}

function printLeaves(node) {
  // Base case
  if (node == null) return;

  // Recursive case

  printLeaves(node.left);

  if (node.left == null && node.right == null) {
    console.log(node.val);
  }

  printLeaves(node.right);
}

let root = new Node(20);
root.left = new Node(8);
root.left.left = new Node(4);
root.left.left.right = new Node(5);
root.left.left.right.right = new Node(3);
root.left.right = new Node(12);
root.left.right.left = new Node(10);
root.left.right.right = new Node(14);
root.right = new Node(22);
root.right.right = new Node(25);
console.log(root.val);

printLeft(root.left);
printLeaves(root);
printRight(root.right);

/*
                  20
            8              22
        4        12              25
          5   10   14
           3  
            11
              13

Time: O(n)
Space: O(n) O(d) d = worst depth of tree
*/
