"""
rabbit hops 
a rabbit that jump by one and jump by 2, 
how many way it can reach to the "n"
"""


def rabbit_hops(i, n):
    if i == n :
        return 1
    if i > n :
        return 0 
    
    return rabbit_hops(i+1, n) + rabbit_hops(i+2, n)


print(rabbit_hops(0,5))

def rabbit_hops2(n):
    if n == 0:
        return 1
    if n < 0:
        return 0 
    return rabbit_hops2(n-1) + rabbit_hops2(n-2)

print(rabbit_hops2(5))


global_counter = 0

def rabbit_hops3(n):
    global global_counter
    if n == 0:
        global_counter += 1
        return 
    if n < 0:
        return 

    rabbit_hops3(n-1)
    rabbit_hops3(n-2)


rabbit_hops3(5)
print(global_counter)


global_path = []

def find_path(n, path):
    if n == 0:
        global_path.append(path)
        return 
    if n < 0:
        return 
    find_path(n-1, path + [1])
    find_path(n-2, path + [2])
    

find_path(5, [])
print(global_path)




"""" 
(frequently called "Football Score" or "Ways to Score"), asks to find the total number of unique combinations
to reach a target score \(N\) using only 3-point (Field Goal) and 7-point (Touchdown + Extra Point) scoring events. 

Number of Ways (3 and 7 Only)
Small Score Example (N=10):
Ways: {7, 3}, {3, 7}
Total ways = 2 (if order matters, it is 2, if order is ignored, it is 1).
Small Score Example (N=13):
Ways: {3, 3, 7}, {3, 7, 3}, {7, 3, 3}
Total ways = 3 (if order matters). 

solution: 
                                A,  B
                              /.\.  /   \
                          A-3  A-7. B-3  B-7 

"""

def number_of_ways(teamA, teamB):
    if teamA == 0 and teamB == 0:
        return 1
    if teamA < 0 or teamB < 0:
        return 0
    
    return (
        number_of_ways(teamA-3, teamB) +
        number_of_ways(teamA-7, teamB) +
        number_of_ways(teamA, teamB-3) +
        number_of_ways(teamA, teamB-7)
    )
    

print(number_of_ways(3,7))


""" 
# build a subset of all the "abcd".

# solution: the best way to think right now is pick or not pick template. 

                            [],[a,b,c]
                            pik/       !pik\
                            [a],[b,c].   [][b,c]

"""

def generate_subset(arr):
    result = []
    def helper(subset):
        if len(arr) == 0:
            result.append(subset)
            return 
        val = arr.pop(0)
        helper(subset + [val])
        helper(subset)
        arr.insert(0, val)  
    
    helper([])
    return result

print(generate_subset(["a","b","c","d"]))
        