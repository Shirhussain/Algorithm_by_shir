""" 
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

 

Example 1:

Input: s = "aab"
Output: "aba"

Example 2:

Input: s = "aaab"
Output: ""

"""
import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        # Step 1: Count the frequency of each character in the input string
        freq_map = {}
        for c in s:
            freq_map[c] = freq_map.get(c, 0) + 1

        # Step 2: Create a max heap based on character frequencies
        max_heap = [(-freq, char) for char, freq in freq_map.items()]
        heapq.heapify(max_heap)

        # Step 3: Rearrange characters to avoid adjacent duplicates
        result = []
        while len(max_heap) > 1:
            freq1, char1 = heapq.heappop(max_heap)
            freq2, char2 = heapq.heappop(max_heap)

            # Append characters to the result list
            result.extend([char1, char2])

            # Update frequency in the map
            freq_map[char1] -= 1
            freq_map[char2] -= 1

            # Push characters back onto the heap if their frequency is still greater than 0
            if freq_map[char1] > 0:
                heapq.heappush(max_heap, (-freq_map[char1], char1))
            if freq_map[char2] > 0:
                heapq.heappush(max_heap, (-freq_map[char2], char2))

        # Check if there is a single character left in the heap
        if max_heap:
            freq, last_char = heapq.heappop(max_heap)
            if freq < -1:
                return ""
            result.append(last_char)

        # Step 4: Return the rearranged string
        return ''.join(result)
