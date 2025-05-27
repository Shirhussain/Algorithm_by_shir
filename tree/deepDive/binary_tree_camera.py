# https://leetcode.com/problems/binary-tree-cameras
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    '''
    Although stated as a tree, it's perhaps best to think of as an acyclic, 
        possibly disconnected, graph.
    1. Convert tree to a graph.  Not sure what form...
         Maybe adjacency list for each node.
    2. Repeatedly process remaining nodes:
        If a node is singleton, it takes a camera to cover. Remove the node from the graph.
        If there are exactly two nodes, then it takes a camera to cover both, 
            remove both from the graph.
        If there is a single edge to a node, the other end of the edge should have a camera to
            optimize coverage. Remove that node and all of its neighbors from the graph.

    '''
    '''
    
        1
     2     3
    4       5
            6
          7  8
        9
        
        
        x
     x     3
    4       5
            x
          x  8
        9

    number_of_cameras: 4
    post: return 0 if parent does not need to be a camera, I am not a camera
                1 if parent does not need to be a camera, I am a camera
                2 if parent does need to be a camera
    post(1)
    post(2)
        post(4)
        visit(4): return 2 b/c 4 is a leaf
        visit(2): add 1 to number_of_cameras, return 1
    post(3)
        post(5)
        post(6)
            post(7)
            post(9)
                return 2 b/c 9 is a leaf
            add 1 to number_of_cameras, return 1
            post(8)
            return 2
            add 1 to number_of_cameras, return 1
        return 0
        return 2
    add 1 to number_of_cameras, return 1


    visit:
    if either child says that it needs me to be a camera (returns 2), then add camera and return 1
    (neither child needs me to be a camera) if either child is a camera, return 0
    (neither child needs me to be a camear and neither child is a camera) return 2



        
            1->2
        2->0     3->0
            x->1    x->1
            5->2      6->2
                    
                


        o     : optimal is root
        o   o  

        o
            o   : optimal is "middle"
            o 


            o
                x
            x    o
            o
    '''

    '''
    Base cases:
    Single node in the tree: answer is 1
    If there are two nodes in the tree: answer is 1 (place camere on either node)
    If there are more than two nodes and I am a leaf, place camera on my parent

    '''

    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        number_of_cameras = 0

        def post_order(node):
            nonlocal number_of_cameras
            if node == None:
                return 0
            left_return = post_order(node.left)
            right_return = post_order(node.right)

            if left_return == 2 or right_return == 2:
                number_of_cameras += 1
                return 1
            if left_return == 1 or right_return == 1:
                return 0
            return 2

        if post_order(root) == 2:
            # this is the root and it is not covered, then we need to add a camera
            number_of_cameras += 1

        return number_of_cameras


 # Given Binary Tree
root = TreeNode(0)
root.left = TreeNode(0)
root.left.left = TreeNode(0)
root.left.left.left = TreeNode(0)
root.left.left.left.right = TreeNode(0)

print(Solution().minCameraCover(root))
