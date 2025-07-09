""" 
there is two kind of sliding window:
1. fixed window size
2. dynamic window size


https://www.piratekingdom.com/leetcode/templates/sliding-window
"""

# fix window size
def sliding_window_fixed_two_loops(arr, k):
    n = len(arr)
    window = 0
    result = []

    # Build the first window
    for i in range(k):
        window += arr[i]
    result.append(window)

    # Slide the window
    for i in range(k, n):
        window += arr[i]         # add new element
        window -= arr[i - k]     # remove leftmost element
        result.append(window)

    return result


# dynamic window size
def sliding_window(arr):
    left = 0
    answer = … # depends on problem
    window = … # sum, count, freq map, etc.

    for right in range(len(arr)):
        # expand the window
        window += arr[right]  # or update state here

        # shrink the window as long as the condition is met
        while condition(window):
            # update the answer
            answer = min(answer, right - left + 1)  # or max, etc.

            # shrink the window
            window -= arr[left]  # or update state here
            left += 1

    return answer
