/*
Given a binary tree, a node in the binary tree, and an integer value k, find all the nodes at a distance k from the given node. 


			1
        2		3
    4	   5  6    7


				k = 1
        node = 3
        1, 6, 7

				k = 2
        node = 3
        2
        
[1 -> null,
2 -> 1
4 -> 2
5 -> 2
3 -> 1
]
  
1.) left
2.) right
3.) parent
   
find()
Time: O(n)
Space: O(n)

findKDist()
Time: O(kn)
Space: O(lg(n))

Time: O(kn)
Space: O(n)
*/

class Node {
  constructor(v) {
    this.val = v;
    this.left = null;
    this.right = null;
  }
}

function find(root, node, map) {
  if (root.val === node) {
    return root;
  }

  if (root.left !== null) {
    map.set(root.left, root);
    left = find(root.left, node, map);
  }

  if (root.right !== null) {
    map.set(root.right, root);
    right = find(root.right, node, map);
  }

  if (left !== null) {
    return left;
  }

  return right;
}

function findKDist(root, prev, k, map, ret) {
  if (root === null) {
    return;
  }

  if (k === 0) {
    ret.push(root.val);
    return;
  }

  // Left
  if (root.left !== prev) {
    findKDist(root.left, root, k - 1, map, ret);
  }

  // Right
  if (root.right !== prev) {
    findKDist(root.right, root, k - 1, map, ret);
  }

  // Parent
  if (map.get(root) !== prev) {
    findKDist(map.get(root), root, k - 1, map, ret);
  }
}

function kDistAway(root, node, k) {
  let ret = [];

  if (root == null || k < 1) {
    return ret;
  }

  let map = new Map();
  map.set(root, null);

  let target = find(root, node, map);

  if (target !== null) {
    findKDist(target, null, k, map, ret);
  }

  return ret;
}
