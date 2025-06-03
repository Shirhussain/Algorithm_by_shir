/*       

https://leetcode.com/problems/house-robber-iii/

Diagram:

                3

        2               3
         ^(3,0)           ^(1,0)
           3                1


Example 3:
              (1+4+5, 6+5)
                    1
        (6+0+0,1+3)     (1+0+0,0+5)
            6               1
      (1,0)   (3,0)           (5,0)
        1       3               5

Output: 11 (6+5)

Example 4:
                (4+2, 4)
                    4
          (1+3,max(2,3))
             1
      (2,3)
        2
(3,0)   
3
*/

class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;

  constructor(
    val: number = 0,
    left: TreeNode | null = null,
    right: TreeNode | null = null
  ) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }

  static buildTree(arr: (number | null)[]) {
    if (!arr || arr[0] == null) {
      return null;
    }

    const root: TreeNode = new TreeNode(arr[0], null, null);
    let i: number = 1;
    let q = [root];

    while (q.length > 0 && i < arr.length) {
      const currNode = q.shift();
      if (!currNode) continue;

      if (i < arr.length && arr[i] != null) {
        currNode.left = new TreeNode(arr[i]!);
        q.push(currNode.left);
      }
      i++;

      if (i < arr.length && arr[i] != null) {
        currNode.right = new TreeNode(arr[i]!);
        q.push(currNode.right);
      }
      i++;
    }
    return root;
  }
}

const rober = (root: TreeNode | null): number => {
  const postOrder = (root: TreeNode | null): [number, number] => {
    if (root === null) {
      return [0, 0];
    }
    const [leftChild, leftGrand] = postOrder(root.left);
    const [rightChild, rightGrand] = postOrder(root.right);
    const pickCurrNode = root.val + leftGrand + rightGrand;
    const notPickCurrNode =
      Math.max(leftChild, leftGrand) + Math.max(rightChild, rightGrand);
    return [pickCurrNode, notPickCurrNode];
  };

  if (root === null) return 0;
  const [pick, notPick] = postOrder(root);
  return Math.max(pick, notPick);
};

let tree = new TreeNode();

const arr = [3, 2, 3, null, 3, null, 1];

const result = TreeNode.buildTree(arr);

console.log(result);

if (result) {
  const max_number = rober(result);
  console.log(max_number);
} else {
  console.log("Tree is null");
}
