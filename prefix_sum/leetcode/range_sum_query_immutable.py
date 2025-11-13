class NumArray:
    # [-2, 0, 3, -5, 2, -1]
    # using prefix sum -> sume previous element with current
    # [-2, -2, 1, -4, -2, -3]
    # this is the pattern of prefix usm: k = num[j]-num[i-1]
    # or k = nums[r]-nums[l-1]
    # nums[r] = k + nums[l-1]
    # this si the pattern.

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix_sum = []

        curr_sum = 0
        for num in nums:
            curr_sum += num
            self.prefix_sum.append(curr_sum)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix_sum[right]
        return self.prefix_sum[right] - self.prefix_sum[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
