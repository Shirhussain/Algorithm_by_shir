def sliding_window(data):
    # 1. Initialize the state (e.g., sum, count, or hash map)
    window_state = 0
    ans = float('inf')  # or 0 for maximums
    
    left = 0

    for right in range(len(data)):
        # 2. Expand: Add the new element to the state
        # (e.g., window_state += data[right])
        window_state += data[right]

        # 3. Monotonic Condition Check: 
        # Is the window currently meeting or violating our goal?
        while condition_met_or_violate(window_state):
                        # --- UPDATE MINIMUM HERE ---
            # If we want the SHORTEST valid window, update before shrinking.
            ans = min(ans, right - left + 1)

            # 4. Shrink: Remove the left element and move the boundary
            window_state -= data[left]
            left += 1

        # --- UPDATE MAXIMUM HERE ---
        # If we want the LONGEST valid window, update after shrinking 
        # (once the window is guaranteed to be valid again).
        # ans = max(ans, right - left + 1)

    return ans