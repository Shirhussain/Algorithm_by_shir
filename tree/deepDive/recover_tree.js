/*

You are given the root of a binary search tree (BST), where the values of exactly 
two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.


											6
            10										2
      1						3						7				12
      
      
											6
            2*										10*
      1						3						7				12
    	
      
      
      
      								1
              2								3
              
              
      								2*
              1*								3
              
  
[1, 10, 3, 6, 7, 2, 12]
    f   m        l 

[1, 2, 3, 6, 7, 10, 12]


[2,1,3]
 f m


1.) If there are 2 violations, we need to first get the first violation and have some pointers to them
firstOne
firstTwo
Continue
to find if 
is one more violation.
secondOne
secondTwo

prev - previous node's val
first - firstOne
middle - firstTwo
last - secondTwo

If there is one violation, then we swap first <-> middle
If there are two violations, then we swap first <-> last

*/

class Node {
  constructor(val, left, right) {
    this.val = val;
    this.left = left;
    this.right = right;
  }
}

function fixBST(root) {
  let inOrder = [];
  convertToArr(root, inOrder);

  inOrder.sort((a, b) => a - b);
  repopulateBST(root, inOrder, { val: 0 }); // pass an object to track index
}

function convertToArr(root, inOrder) {
  if (root === null) return;

  convertToArr(root.left, inOrder);
  inOrder.push(root.val);
  convertToArr(root.right, inOrder);
}

function repopulateBST(root, inOrder, indexObject) {
  if (root === null) return;

  repopulateBST(root.left, inOrder, indexObject);
  root.val = inOrder[indexObject.val];
  indexObject.val++;
  repopulateBST(root.right, inOrder, indexObject);
}

/*
 * Optimal approach
 *
 * Time: O(n)
 * Space: O(log(n))
 */

let first = (middle = last = prev = null);

function betterFixBST(root) {
  betterFixBSTHelper(root);

  // Two violations
  if (first !== null && last !== null) {
    let temp = first.val;
    first.val = last.val;
    last.val = temp;
  } else {
    let temp = first.val;
    first.val = middle.val;
    middle.val = temp;
  }
}

function betterFixBSTHelper(root) {
  if (root === null) return;

  betterFixBSTHelper(root.left);

  // If root is smaller than prev node, then we've found a violation
  if (prev !== null && root.val < prev.val) {
    // First violation
    if (first === null) {
      first = prev;
      middle = root;
    }
    // 2nd violation
    else {
      last = root;
    }
  }

  prev = root;

  betterFixBSTHelper(root.right);
}

// Time: O(nlog(n))
// Space: O(n)
