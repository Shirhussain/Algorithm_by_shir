//   Definition for a binary tree node.
class BinaryTreeNode {
  val: number;
  left: BinaryTreeNode | null;
  right: BinaryTreeNode | null;
  constructor(
    val?: number,
    left?: BinaryTreeNode | null,
    right?: BinaryTreeNode | null
  ) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

function levelOrder(root: BinaryTreeNode | null): number[][] {
  let result: number[][] = [];

  function levelOrderDFS(root: BinaryTreeNode | null, level: number): void {
    if (root === null) {
      return;
    }
    if (result.length == level) {
      result.push([]);
    }

    // this is preorder traversal but doesn't matter
    // if you do if pre order or post order it's also working.
    result[level].push(root.val);
    levelOrderDFS(root.left, level + 1);
    levelOrderDFS(root.right, level + 1);
  }

  levelOrderDFS(root, 0);

  return result;
}
