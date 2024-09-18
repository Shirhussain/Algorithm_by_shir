class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        window_sum = 0
        for i in range(k):
            window_sum += nums[i]

        # Initialize max_sum with the sum of the first window
        max_sum = window_sum

        # Step 2: Slide the window across the rest of the array
        for i in range(k, len(nums)):
            # Add the new element (nums[i]) and subtract the element going out of the window (nums[i - k])
            window_sum += nums[i] - nums[i - k]

            # Track the maximum sum encountered
            max_sum = max(max_sum, window_sum)

        # Step 3: Return the maximum average (max_sum / k)
        return max_sum / float(k)
