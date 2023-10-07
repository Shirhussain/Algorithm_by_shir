// https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/

class Solution {
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;

        // [1, 2]
        while (left + 1 < right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] == target) {
                return mid;
            }

            // check which side is in order
            if (nums[mid] > nums[left]) {
                // left is in order
                if (target >= nums[left] && target < nums[mid]) {
                    right = mid;
                } else {
                    left = mid;
                }
            } else {
                // right is in order
                if (target > nums[mid] && target <= nums[right]) {
                    // target is on the right side (sorted)
                    left = mid;
                } else {
                    right = mid;
                }
            }
        }

        if (nums[left] == target) {
            return left;
        }
        if (nums[right] == target) {
            return right;
        }

        return -1;
    }
}
