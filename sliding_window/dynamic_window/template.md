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
