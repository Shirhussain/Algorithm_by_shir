"""
You are given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.

You can attend an event i at any day d where startTimei <= d <= endTimei. You can only attend one event at any time d.

Return the maximum number of events you can attend.
"""
import heapq
from typing import List


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        result = 0
        if not events:
            return result

        # Sort events based on the starting time
        events.sort(key=lambda x: x[0])

        # mean heap to keep track of event based on their ending time
        min_heap = []

        i, time = 0, 0

        # Iterate through events and update the min heap
        while i < len(events) or min_heap:
            # if the mean heap is empty, update the current time
            if not min_heap:
                time = events[i][0]

            # add event with the same starting point to the heap
            while i < len(events) and time == events[i][0]:
                heapq.heappush(min_heap, events[i][1])
                i += 1

            # remove the event with the earliest ending time from the main heap
            heapq.heappop(min_heap)

            # increament the result counter
            result += 1

            # move the the next time slog
            time += 1

            # Remove events from the min heap that have already ended
            while min_heap and time > min_heap[0]:
                heapq.heappop(min_heap)
        return result
