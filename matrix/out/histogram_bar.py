'''
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Constraints: length <= 10^5
each height is between 0 and 10^4 
'''

'''
      x
    x x
    x x
    x x   x
x   x x x x
x x x x x x

heights = [2,1,5,6,2,3]
'''
'''
            x
          x x
          x x
          x x   x
      x   x x x x
      x x x x x x
      0 1 2 3 4 5



(height 2, beginning 2)
(height 1, beginning 0) 

max_area: 10
'''
