"""
There are n cities connected by some number of flights.
You are given an array flights where 
flights[i] = [fromi, toi, pricei] indicates that there 
is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return 
the cheapest price from src to dst with at most k stops.
If there is no such route, return -1.


Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.
"""

from typing import List, Union


def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
    """
        DFS (TLE)
    """
    def helper(stop: int, numOfStops: int) -> Union[float, int]:
        if numOfStops > K:
            return float('inf')
        elif stop == dst:
            return 0

        cheapestFlight = float('inf')
        for flight in flights:
            if flight[0] == stop:
                cheapestFlight = min(
                    cheapestFlight, flight[2] + helper(flight[1], numOfStops + 1))

        return cheapestFlight

    cheapestFlight = helper(src, -1)
    return cheapestFlight if cheapestFlight != float('inf') else -1


n = 4
flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
src = 0
dst = 3
k = 1

print(findCheapestPrice(n, flights, src, dst, k))
