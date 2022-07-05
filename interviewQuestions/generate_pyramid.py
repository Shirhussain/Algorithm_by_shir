# Q.53. Can you write a function to generate the following pyramid?

#     *

#    ***

#   *****

#  *******

# *********

def pyramid(n):
    for row in range(n):
        for space in range(n-row):
            print(" ", end = "")
        for star in range(row):
            print("*", end = "")
        for start in range(row+1):
            print("*", end = "")
        print()
        

pyramid(50)