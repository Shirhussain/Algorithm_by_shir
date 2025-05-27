'''




Problem Description:


You are given:


A list of cities, each identified by a unique string.


A list of flights, where each flight is represented as a tuple:
(source_city, destination_city, departure_time, duration)


departure_time: integer between 0 and 1439 (minutes since midnight)


duration: duration in minutes


A start_city, a destination_city, and a start_time (in minutes since midnight).


Each flight can only be taken if you arrive at the source city before or exactly at its departure_time.


Write a function to determine whether there exists a sequence of flights that allows you to travel from start_city to destination_city, obeying time constraints.




Example:


cities = ["A", "B", "C", "D"]
flights = [
   ("A", "B", 60, 30),   # departs at 1:00 AM, arrives at 1:30 AM
   ("B", "C", 90, 60),   # departs at 1:30 AM, arrives at 2:30 AM
   ("C", "D", 200, 50),  # departs at 3:20 AM, arrives at 4:10 AM
   ("A", "D", 100, 80)   # departs at 1:40 AM, arrives at 3:00 AM
]
start_city = "A"
destination_city = "D"
start_time = 50  # 12:50 AM


print(is_path_possible(cities, flights, start_city, destination_city, start_time))  # True






Solution 1:
   - A simple DFS can find if there is a path between two nodes int the graph
   - In this problem the edges change depending on what time we arrive to each node. So if we carry over the current  time to each node, we can decide what cities we can go from that node.




Solution 2: Frame this as a backtracking problem.
'''

from collections import defaultdict
from typing import List, Tuple, Dict


def is_path_possible(cities: List[str], flights: List[Tuple[str, str, int, int]],
                     start_city: str, destination_city: str, start_time: int) -> bool:
    visited = set()

    # Each node is mapped into a tuple (dst, dep, dur)
    neighbors = create_adjacency_list(flights)

    def dfs(city, cur_time):
        if city == destination_city:
            return True

        if city in visited:
            return

        visited.add(city)

        for dst, dep, dur in neighbors[city]:
            if cur_time <= dep:
                if dfs(dst, dep+dur) == True:
                    return True

        return False

    return dfs(start_city, start_time)


def create_adjacency_list(flights: List[Tuple[str, str, int, int]]) -> Dict[str, List[Tuple[str, int, int]]]:
    neighbors = defaultdict(list)

    for src, dst, dep, dur in flights:
        neighbors[src].append((dst, dep, dur))

    return neighbors


cities = ["A", "B", "C", "D"]
flights = [
    ("A", "B", 60, 30),   # departs at 1:00 AM, arrives at 1:30 AM
    ("B", "C", 90, 60),   # departs at 1:30 AM, arrives at 2:30 AM
    ("C", "D", 200, 50),  # departs at 3:20 AM, arrives at 4:10 AM
    ("A", "D", 100, 80)   # departs at 1:40 AM, arrives at 3:00 AM
]
start_city = "A"
destination_city = "D"
start_time = 50  # 12:50 AM


print(is_path_possible(cities, flights, start_city,
      destination_city, start_time))  # True
