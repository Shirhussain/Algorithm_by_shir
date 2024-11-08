class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # global_max = float("-inf")

        # for  i in range(k-1):
        #     sum = 0
        #     sum += nums[i]
        #     avg = sum/k

        current_sum = sum(nums[:k])
        max_sum = current_sum  # This will store the maximum sum of any window of size k

        # Slide the window from the start of the array to the end
        for i in range(k, len(nums)):
            # Slide the window: subtract the element that's going out of the window
            # and add the new element coming into the window
            current_sum += nums[i] - nums[i - k]
            # Update the maximum sum if the current window's sum is greater
            max_sum = max(max_sum, current_sum)

        # Calculate and return the maximum average
        return max_sum / k

        # for i in range(0,k-1):
        #     window  = nums[]
        # for i in range(len(nums)):
        #     sum = []
        #     global_avg = 0
        #     sum = num
