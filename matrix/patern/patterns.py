def pattern1(n):
    print("1: \n")
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


def pattern2(n):
    print("\n 2:")
    for i in range(n):
        for j in range(n):
            print("* ", end="")
        print()
    print()


def pattern3(n):
    print("\n 3:")
    for i in range(n):
        for j in range(n - i):
            print("* ", end="")
        print()
    print()


def pattern4(n):
    print("\n 4:")
    for i in range(1, n+2):
        for j in range(1, i):
            print(j, end=" ")
        print()
    print()


def pattern5(n):
    print("\n 5:")
    for i in range(2*n):
        if i <= n:
            for j in range(i):
                print("*", end=" ")
        else:
            for j in range(2*n-i):
                print("*", end=" ")
        print()
    print()


def pattern6(n):
    print("\n 6:")
    for i in range(n):
        print(" "*(n-i)+"*"*i, end="")
        print()

    # or

    for i in range(n):
        for j in range(n-i):
            print(" ", end=" ")
        for j in range(i):
            print("*", end=" ")
        print()
    print()


def pattern7(n):
    print("\n 7:")
    for i in range(n):
        for j in range(i):
            print(" ", end=" ")
        for j in range(n-i):
            print("*", end=" ")
        print()
    print()


def pattern8(n):
    print("\n 8:")
    for i in range(n):
        for j in range(n-i):
            print(" ", end=" ")
        for j in range(i):
            print("*", end=" ")
        for j in range(i-1):
            # to know how does it work just change (* to # ) then you will see the pattern
            print("*", end=" ")
        print()
    print()


def pattern9(n):
    print("\n 9:")
    for i in range(n):
        for j in range(i):
            print(" ", end=" ")
        for j in range(n-i):
            print("*", end=" ")
        for j in range(n-i-1):
            print("*", end=" ")
        print()
    print()


def pattern10(n):
    print("\n 10:")
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
    print()


def pattern11(n):
    print("\n 11:")
    for i in range(n):
        for j in range(i):
            print(" ", end="")
        for j in range(n-i):
            print("*", end=" ")
        for j in range(i):
            print(" ", end="")
        print()
    print()

# z


def pattern12(n):
    print("\n 12:")
    # pattern11(n)
    # pattern10(n)
    # print()
    for i in range(2*n):
        for j in range(n-i):
            print(" ", end=" ")
        if i <= n:
            for j in range(i):
                print("*", end=" ")

            for j in range(i-1):
                print("*", end=" ")
        # else:
        #     for j in range(2*n-i):
        #         print("*", end="")
        #     for j in range(2*n-i-1):
        #         print("*", end="")
        print()
    print()


def pattern13(n):
    print("\n 13:")
    # z
    print("* " * n)
    for i in range(n):
        print(" " * (n - i), end="")
        print(" *")
    print("* " * n)
    print()


# def pattern13(n):
pattern1(5)
pattern2(5)
pattern3(5)
pattern4(5)
pattern5(5)
pattern6(5)
pattern7(5)
pattern8(5)
pattern9(5)
pattern10(5)
pattern11(5)
pattern12(5)
pattern13(5)
