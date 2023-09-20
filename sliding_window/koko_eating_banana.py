from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """

        Speed 11 bananas/hr  Pile 1->hr 1, pile2 -> hr2, pile3 -> hr 3, pile4 -> hr 4
            4 bananas/h4 Pile 1-> 1hr, pile 2-> 2 hrs pile3 -> 2hrs, pile4 -> 3hrs (3 + 2 + 2 +1) = 8
        we need to find the minimum speed and max speed koko can ead 

        the min speed is going to be one banba per hour (1)   1/h
        max speed is going to be max(arr)/h

        Observation 1:
        Upperbound: 
            max_speed = Max(array)/per hour
            #hours = size of pile

        Lowerbound:
            min_speed = 1 banana/per hour
            #hours = sum(size of pile)

        min/speed               max/speed


        Question:
            if i give you a speed?
            can you tell me how many hour koko needs?

            foo(speed, arr):
                total = 0
                for i in arr:
                    total += cil(arr[i]/speed)
                return total

            Exlampels:
            Input: piles = [3,6,7,11], h = 8
            Output: 4

            or piles = [3,6,7,11] -- if seed is 4 
            then cile(3/4) + ciel(6/4) + ciel(7/4) + ceil(11/4)
            then 1         + 2         +   2       + 3
            then hours = 8


            like: [3,6,7,11] --- if speed of 6
            then cil(3/6) + cil(6/6) + cil(7/6) + cil(11/6)
            then  1       +     1    + 2        + 2  
            then total hour = 6


            for speed in range(min_speed, max_speed):
                #  If the pile has less than k(speed) bananas, she eats all of 
                # them instead and will not eat any more bananas
                check foo(speed, arr) <= h:
                    return speed
                return -1

            O(n*(max_speed))
        """

        def hour_need(speed, piles):
            total_hr = 0
            for i in piles:
                total_hr += math.ceil(i/speed)
            return total_hr

        # brute force
        # for speed in range(1, max(piles)+1):
        #     if hour_need(speed, piles) > h:
        #         continue
        #     if hour_need(speed, piles) <= h:
        #         return speed
        # return -1

        # for performance using binary tree

        min_speed = 1
        max_speed = max(piles)

        while min_speed < max_speed:
            mid = (min_speed + max_speed) // 2

            if hour_need(mid, piles) <= h:
                # answer must lie to the left half (inclusive of current value ie mid)
                max_speed = mid
            else:
                # answer must lie to the right half (exclusive of current value ie mid)
                min_speed = mid + 1

        return min_speed


piles = [3, 6, 7, 11]
h = 8
s = Solution()
result = s.minEatingSpeed(piles, h)
print(result)
