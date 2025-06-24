'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
'''

'''
Example:

                    1
                    
            2                 2
            
        3      4          4       3
        
           5      6     6            5
        
Output: false

Example 2:
                    1

            2                 2

        3      4          4       3

             5   6      6   5         

Output: true

Example 3:          []

Output: true

Example 4:
                    1
Output: true

'''
'''
Constraints: Between 0 and 1000 nodes.

The input tree can be empty.
'''
'''
Diagram:

                    1

            2                 2

        3      4          4       5

           5      6     6            5



[1]
[2, 2]
[3, 4, 4, 5] false

                    1

            2                 2

        3      4          4       3

           5      6     6            5

queue: 3L, 4L, 4R, 3R

[1]
[2, 2]
[3, 4, 4, 3]
[null, 5, null, 6, 6, null, null, 5] false


                    1

            2                 2

        3      N            N       3

     5    N                       N   5
'''
'''
Pseudocode

while there are levels
   Create an array for each level, including nulls
   Return false if not palindrome
return True


create queue
enqueue root
while queue is not empty
   # Create an array for each level, including nulls
   if queue (treated as an array) is not a palindrome, return false
   for each element currently in queue
      dequeue the element
      if element is not null, add children (with nulls) to queue
return True

def helper(left, right):
   if left and right are null
      return true
   if left or right is null
      return false
   if left.val != right.val
      return false
   return helper(left.left, right.right) and helper(left.right, right.left)
      

def driver(node):
   if node is null
      return true
   return helper(node.left, node.right)
   
   
                   1

           2L                 2R

       3L      4L         4R       3R

          5L      6     6             5R

node:1

helper(2L, 2R) --> False
left: 2L
right: 2R

helper(3L, 3R) [& helper(4L, 4R)] --> False

helper(3L, 3R) --> False
left: 3L
Right: 3R

helper(null, 5R) [& helper(5L, null)] --> False

helper(null, 5R) --> False




      
'''

'''

'''
'''
symmetric3(root):
  [null, 3L, null, 2L, 5, 4L, 6, 1, 6, 4R, ...]


'''