https://docs.google.com/document/d/1GkdNX7JAN2M3-iGWRvWX27358rhs3dmiVg8M318okU4/edit?usp=sharing

Sliding Window
What are some indicators I should use Sliding Window
Hunter/catcher or two pointers
What is this technique?
Usually want to find a longest or shortest contiguous slide of an array or string that satisfies a monotonic condition.
[1, 2, 3, 4, 5, 6]
Subsequence: [1, 3] or [1, 2, 5], or odd ones: [1, 3, 5]
Subarray: [3, 4, 5]
We could expand this technique for subsequences as well, but usually this is not that common and subsequences problems are usually solved by dynamic programming.
However it can be used for some limited examples where we filter out some values from the window to get a subsequence. Below is an example:
Example:
Find the longest subsequence of odd numbers where the difference between the two values in the subsequence is less than or equal to 2.
R
[1, 2, 3, 4, 5, 6, 9, 12, 22, 23, 24, 25, 29]
L

[1, 3, 5]
[23, 25]
[29]
Difference between two pointer technique and sliding window:
Two-pointer technique is when we have two pointers in the array and they can move independently.
Sliding window:
Pointers move in the same direction.
There is a contraction and then a catch-up phase
The left pointer does not pass the right pointer.
How do I solve a sliding window problem?
Recognize the monotonic condition
If you expand the window once to satisfy a constraint, further expansions can potentially satisfy it too.
If the expansion of the window breaks a constraint, further expansions should break the constraint.
R
[1, 2, 3, 4, 5, 6, 7, 8, 9]
L
Expand the right pointer until the condition breaks
Shrink the left until the condition is satisfied

Write a template for the sliding window technique

def sliding_window(input);
What is the runtime & space complexity of a sliding window algorithm?
Runtime: O(n)
Memory: O(n)
