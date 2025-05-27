# https://www.geeksforgeeks.org/snake-ladder-problem-2

# Snake and Ladder Problem
# Last Updated : 14 Feb, 2023

# Given a snake and ladder board, find the minimum number of dice throws required to reach the destination or
# last cell from the source or 1st cell. Basically, the player has total control over
# the outcome of the dice throw and wants to find out the minimum number of
# throws required to reach the last cell.
# If the player reaches a cell which is the base of a ladder,
# the player has to climb up that ladder and if reaches a cell is the mouth of
# the snake, and has to go down to the tail of the snake without a dice throw.

# the est way is to solve this kind of problem is to first try to create a graph then put this in shortest path template:
# put that graph here:

from collections import deque


def shortest_path(graph, start, end):
    visited = set()
    q = deque
    parent_dic = {}
    parent_dic["start"] = "Null"

    while q:
        curr_node = q.popleft()
        if curr_node not in visited:
            # if you have many answer in your answer and you want example between 1= A,B,D,H and 2 = A,C,F,H
            # if both of them are the answer and the question is to output in the last one in alphabetical order
            # so only you need is sort the children here: sorted(graph[curr_node])
            for node in graph[curr_node]:
                if node not in visited:
                    q.append(node)
                    if node not in parent_dic:
                        parent_dic[node] = curr_node
            visited.add(curr_node)

    path = []
    path.append(end)
    while parent_dic[end] != "Null":
        path.append(parent_dic[end])
        end = parent_dic[end]
    return reversed(path)
