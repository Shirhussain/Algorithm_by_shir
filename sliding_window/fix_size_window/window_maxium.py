from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []

        # Outer loop slides the window
        for i in range(len(nums) - k + 1):
            max_in_window = nums[i]  # Initialize max for this window

            # Inner loop finds the maximum in the current window
            for j in range(1, k):
                if nums[i + j] > max_in_window:
                    max_in_window = nums[i + j]

            # Store the maximum of the current window
            result.append(max_in_window)

        return result


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
s = Solution()
final = s.maxSlidingWindow(nums, k)
print(final)
