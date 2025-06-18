""" 
Given a set of distinct integers, print the size of a maximal subset of  where the sum of any  numbers in  is not evenly divisible by .

Example
 

One of the arrays that can be created is . Another is . After testing all permutations, the maximum length solution array has  elements.

Function Description

Complete the nonDivisibleSubset function in the editor below.

nonDivisibleSubset has the following parameter(s):

int S[n]: an array of integers
int k: the divisor
Returns

int: the length of the longest subset of  meeting the criteria
Input Format

The first line contains  space-separated integers,  and , the number of values in  and the non factor.
The second line contains  space-separated integers, each an , the unique values of the set.

Constraints

All of the given numbers are distinct.
Sample Input

STDIN    Function
-----    --------
4 3      S[] size n = 4, k = 3
1 7 2 4  S = [1, 7, 2, 4]
Sample Output

3
Explanation

The sums of all permutations of two elements from  are:

1 + 7 = 8
1 + 2 = 3
1 + 4 = 5
7 + 2 = 9
7 + 4 = 11
2 + 4 = 6
Only  will not ever sum to a multiple of .
"""


#  although you could do this by recursion, it's not the best solution
# if we have a big K or n it's is not possible to do back tracking 
# so in this case if you have some think like the word "mode" or "division" or some thing like that
# and you are working with numbers so think about "Math" how you can solve this problem with math

def nonDivisibleSubset(k, s):
    # Write your code here
    result = 0
    mode_counter = [0]*k
    
    for item in s:
        mode_counter[item%k] += 1
    
    print(mode_counter)
    
    # with l = 0 ther is edge case
    l = 1
    r = k-1
    while l<r:
        max_pick = max(mode_counter[l],mode_counter[r])
        result += max_pick
        l += 1
        r -= 1
    
    # Include at most one element with remainder 0
    if mode_counter[0]> 0:
        result += 1
    
    # Remainder k/2: only if k is even, include at most one
    if k % 2 == 0 and mode_counter[k // 2] > 0:
        result += 1
    
    return result


s = [1, 7, 2, 4]
k = 3
print(nonDivisibleSubset(k, s))