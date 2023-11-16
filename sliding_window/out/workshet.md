What are some indicators I should use Sliding Window?

- Contiguous slices of a linear data structure (array, string)
- Monotonic condition: If the condition is violated,
  then growing the window further will only worsen
  the condition. The condition can only be restored
  by shrinking the window.
- Longest/shortest subsequence is often an element of
  a sliding window problem

How do I solve a sliding window problem?

- Identify the monotonic condition

Write a template for the sliding window technique:

sliding_window(input)
  initialize state related to window
  initialize left to 0
  
  for r in range 0 to length of input
  
    update window state for expansion
    while monotonic condition is not met
      update window state for contraction
      increment left

NOTE: typically going to need additional code to capture/return the answer


What is the runtime & space complexity of a sliding window algorithm?

Time: O(N) * (time for updating state)
Space: O(1) + size of state + output size 
