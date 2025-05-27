'''
Given two trees, output all of the differences between
the trees.

     1
  2     3
4


      1
    3   2
          7

        1,1
     2,3   3,2
 4,-          -,7

queue:   (4,-),(2,3,L), (-,7),(3,2,R)

                 (1,1)
          (2,3)         (3,2)

'''
'''
# TODO: check special cases
def diff_of_two_trees(node1, node2)
     create empty queue
     create output_tree with (node1.val, node2.val) at root
     create left child = (node1.left, node2.left)
     if left child is not (empty, empty) then 
          add (left child, tree root left) to queue
     create right child = (node1.right, node2.right)
     if right child is not (empty, empty) then 
          add (right child, tree root right) to queue

     while queue is not empty
          remove (node1,node2), output_tree_location from queue
          
          create left child = (node1.left, node2.left)
          if left child is not (empty, empty) then 
               add (left child, output_tree_location left) to queue
          create right child = (node1.right, node2.right)
          if right child is not (empty, empty) then 
               add (right child, output_tree_location right) to queue
     
     return output_tree

'''
