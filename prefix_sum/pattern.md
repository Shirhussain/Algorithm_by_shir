https://youtu.be/N_AgTyMHgtw?si=3XSYdSwAblPFisWW

Input: nums = [1, 2, 3, 4, 5, 6], i = 1, j = 3

Output: 9
Explanation:
Preprocess the array A to create a prefix sum array: P = [1, 3, 6, 10, 15, 21].

To find the sum between indices i and j, use the formula: P[j] - P[i-1].

# this is the pattern of prefix usm: k = num[j]-num[i-1]

    # or k = nums[r]-nums[l-1]
    # nums[r] = k + nums[l-1]
    # this si the pattern.
