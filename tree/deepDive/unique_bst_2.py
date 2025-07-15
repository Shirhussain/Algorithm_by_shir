# https://leetcode.com/problems/unique-binary-search-trees-ii/

'''
Diagram
n=2

    1
       2

    2
 1


n = 3
                                         [1,2,3]
                                       
                                         
             [],[1],[2,3]                 [1],2,[3]        [1,2],3,[]
             
[],1,[[],2,[3]]  [],1,[[2],3,[]]

answer: [[null, 1, [null,2,[null, 3, null]]], [null, 1, [[null, 2, null], 3, null]]]
root: 1
left_set: []
right_set: helper([2,3])
   answer: [[null,2,[null, 3, null]], [[null, 2, null], 3, null]]
   root: 2
   left_set: []
   right_set: [3]
   return: [null,2,[null, 3, null]]

   root: 3
   return: [[null, 2, null], 3, null]



n = 5

                                              [1,2,3,4,5]
                                             [1,2],[3],[4,5]
Option 1: explore all possible child pairs
    [[],1,[2]],3,[[],4,[5]]   [[1],2,[]],3,[[],4,[5]] [[],1,[2]],3,[[4],5,[]] ...
    
Option 2: more DP-like
                              Generate all [1,2]'s, 3, explore [4,5]


n = 1: 1
n = 2: 2
n = 3: at most 6 = 3*2
n = 4: at most 4*6 = 4*3*2 = 24

n = 8: at most 8!

   8 roots, each root 
                                              
'''
'''
Pseudocode

def gen_bsts(n):
  generate list of n consecutive positive integers beginning at 1

  # Given list of values, returns list of all of
  # the bsts for that list
  def helper(list):

    if list is empty
      return empty list
    if list contains a single element
      return list containing tree containing the single element
      
    answer is empty list
    for root as an element of the list
      let left_set be helper(list to left of root)
      let right_set be helper(list to right of root)
      # add to answer list all trees having root as root and tree from left/right as children
      if left_set is empty
        add to answer list all tree having null on left, root as root, and a right_set element as right
      if right_set is empty
        see above
      if neither is empty
        for each pair from left_set and right_set, add to answer tree having root as root and left/right
    return answer
    
  return helper(list of elements)




def gen_bsts(n):
  generate list of n consecutive positive integers beginning at 1

  define answer to be an empty list

  def helper(left_subtree, root, right_subtree, index):
    make a node containing the root as its value


  for each i in list
    helper(list of elements up to i, i, list of elements following i, )

  return answer
'''