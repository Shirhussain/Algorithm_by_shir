class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # Helper function to calculate subarrays with at most `goal` sum
        def at_most(goal):
            if goal < 0:
                return 0
            left = 0
            current_sum = 0
            result = 0

            # Sliding window with right pointer expanding the window
            for right in range(len(nums)):
                current_sum += nums[right]

                # Shrink the window if the sum exceeds the goal
                while current_sum > goal:
                    current_sum -= nums[left]
                    left += 1

                # Count the valid subarrays with sum <= goal
                result += right - left + 1

            return result

        # Count subarrays with sum exactly equal to the goal
        # It is the difference between subarrays with sum at most `goal`
        # and subarrays with sum at most `goal-1`
        return at_most(goal) - at_most(goal - 1)
