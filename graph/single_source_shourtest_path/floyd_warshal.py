# in floyd Warshall we never visited a vertex twice.

# we take this as infinity number
import itertools
INF = 9999


def print_solution(number_of_vertices, distance):
    for i in range(number_of_vertices):
        for j in range(number_of_vertices):
            if distance[i][j] == INF:
                print("INF", end=" ")
            else:
                print(distance[i][j], end=" ")
        print(" ")


def floyd_warshall(number_of_vertices, graph):
    distance = graph

    # for k in range(number_of_vertices):
    #     for i in range(number_of_vertices):
    #         for j in range(number_of_vertices):
    #             # here we will find if it gos from one node to another via other nodes(vertices)
    #             distance[i][j] = min(
    #                 distance[i][j], distance[i][k] + distance[k][j])

    for k, i in itertools.product(range(number_of_vertices), range(number_of_vertices)):
        for j in range(number_of_vertices):
            # here we will find if it gos from one node to another via other nodes(vertices)
            distance[i][j] = min(
                distance[i][j], distance[i][k] + distance[k][j])

    print_solution(number_of_vertices, distance)


# crate a matrix
graph = [
    [0, 8, INF, 1],
    [INF, 0, 1, INF],
    [4, INF, 0, INF],
    [INF, 2, 9, 1]
]

floyd_warshall(4, graph)
