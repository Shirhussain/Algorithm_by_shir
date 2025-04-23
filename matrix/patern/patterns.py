def pattern1(n):
    j = 1
    for i in range(n):
        print("* " * j)
        j += 1
    print()

    # or

    # just image all of them as a matrix row and col

    for row in range(n):
        for col in range(row + 1):
            print("* ", end="")
        print()
    return


def pattern2(n):
    for i in range(n):
        for j in range(n):
            print("* ", end="")
        print()
    return


def pattern3(n):
    for i in range(n):
        for j in range(n - i):
            print("* ", end="")
        print()
    return


def pattern4(n):
    for i in range(1, n+2):
        for j in range(1, i):
            print(j, end=" ")
        print()
    return


def pattern5(n):
    for i in range(2*n):
        if i <= n:
            for j in range(i):
                print("* ", end="")
        else:
            for j in range(2*n-i):
                print("* ", end="")
        print()
    return


def pattern6(n):
    for i in range(n):
        print(" "*(n-i)+"*"*i, end="")
        print()

    # or

    for i in range(n):
        for j in range(n-i):
            print(" ", end="")
        for j in range(i):
            print("*", end="")
        print()
    return


def pattern7(n):
    for i in range(n):
        for j in range(i):
            print(" ", end="")
        for j in range(n-i):
            print("*", end="")
        print()
    return


def pattern8(n):
    for i in range(n):
        for j in range(n-i):
            print(" ", end="")
        for j in range(i):
            print("*", end="")
        for j in range(i-1):
            # to know how does it work just change (* to # ) then you will see the pattern
            print("*", end="")
        print()
    return


def pattern9(n):
    for i in range(n):
        for j in range(i):
            print(" ", end="")
        for j in range(n-i):
            print("*", end="")
        for j in range(n-i-1):
            print("*", end="")
        print()
    return


def pattern10(n):
    for i in range(n):
        # for j in range(n-i):
        #     print(" ", end="")
        # for j in range(i):
        #     print("*", end=" ")
        # print()
        # or
        for j in range(n-i):
            print(" ", end="")
        for j in range(i):
            print("*", end=" ")
        for j in range(i):
            print(" ", end="")
        print()
    return


def pattern11(n):
    for i in range(n):
        for j in range(i):
            print(" ", end="")
        for j in range(n-i):
            print("*", end=" ")
        for j in range(i):
            print(" ", end="")
        print()
    return


def pattern12(n):
    pattern11(n)
    pattern10(n)
    return


# def pattern13(n):


def validPath(self, n: int, edges:, source: int, destination: int) -> bool:
    graph = collections.defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()

    def dfs(node):
        if node == destination:
            return True
        visited.add(node)

        for edg in graph[node]:
            if edg not in visited:
                if dfs(edg):
                    return True
        return False

    return dfs(source)
