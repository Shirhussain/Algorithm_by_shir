/*

Migrate a Complete Binary Search tree to Min Heap

[1, 2, 3, 4, 5, 6]

BST

							4
          2        6
       1     3    5   7

recurse(..left)
add to array(node)
recurse(..right)

[1,2,3,4,5,6,7]

Min Heap

							1
          2          5
      3     4     6     7
      
current node = node
recurse(..left)
recurse(..right)

         1
      2          5
   3     4     6     7


 */

class Node {
    constructor(data) {
        this.data = data;
        this.left = null;
        this.right = null;
    }
}

function inorderTraversalArrayPush(root, arr) {
  // base case
  if (root == null) {
    return
  }
  
  //recursive case
  inorderTraversalArrayPush(root.left, arr)
  arr.push(root.data)
  inorderTraversalArrayPush(root.right, arr)
}

function preorderFillTree(root, arr, arrIndex) {
  // base case
  if (root == null) {
    return arrIndex
  }
  
  //recursive case
  root.data = arr[arrIndex]
  arrIndex++
  
  arrIndex = preorderFillTree(root.left, arr, arrIndex)
  arrIndex = preorderFillTree(root.right, arr, arrIndex)
  
  return arrIndex
}

function preorderPrintTree(root) {
  // base case
  if (root == null) {
    return
  }
  
  console.log(root.data)
  preorderPrintTree(root.left)
  preorderPrintTree(root.right)
}


let root = new Node(4)
root.left = new Node(2)
root.right = new Node(6)
root.left.left = new Node(1)
root.left.right = new Node(3)
root.right.left = new Node(5)
root.right.right = new Node(7)

function migrateBSTToMinHeap(root) {
  arr = []
  inorderTraversalArrayPush(root, arr) // arr = [1,2,3,4,5,6,7]
  preorderFillTree(root, arr, 0)
  preorderPrintTree(root) // prints 1, 2, 3, 4, 5, 6, 7
}








