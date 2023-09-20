""" 
75. Sort Colors

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.



Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]

 

Constraints:

    n == nums.length
    1 <= n <= 300
    nums[i] is either 0, 1, or 2.




answer =

  Do not return anything, modify nums in-place instead.
        start = s
        midlle = m
        end = e

        nums = [2,0,2,1,1,0]
                s         e
                m

        Input: nums = [2,0,2,1,1,0]
        Output: [0,0,1,1,2,2]
        s should be = 0
        middle should b = 1
        end should be = 2



        if we have 4 color then we need to categorize in three like if we have color like  
        0->s-1 (red)
        s->m-1(white)
        m=e ->len(arr-1) (Blue)
        
        then we have orange as ) (O)
        [R W B B R W O B W]
        [R R W W B B O B]
        O( #colors * N) ->  (Bucket Sort)

        we group orange with blue as shown in above then once agen we sort last two --> blue and ornage 
        R, W, B, O  
        [R , R , B, B, W, B, O, O, R , B, W]
        [R, R, R, W, W, B, B, B, O, O, B] (Apply our algorithm)
"""


def sort_colors(nums):
    s = m = 0
    e = len(nums) - 1

    while m <= e:
        if nums[m] == 0:
            # swap then increment both
            nums[s], nums[m] = nums[m], nums[s]
            m += 1
            s += 1
        elif nums[m] == 1:
            # increment m
            m += 1
        elif nums[m] == 2:
            # swap then decrement
            nums[m], nums[e] = nums[e], nums[m]
            e -= 1
    return nums


nums = [2, 0, 2, 1, 1, 0]
print(sort_colors(nums))
