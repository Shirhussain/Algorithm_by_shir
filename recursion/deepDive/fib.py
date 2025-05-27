"""
Recursion - something defined in terms of itself


Fibonacci

        n
0 1 2 3 4 5 6  7
1 1 2 3 5 8 13 21 ...
        
fib(n) ~ returns the nth fibonacci number

fib(4) -> 5
fib(6) -> 13
...
ITERATIVE:
Time: O(n)
Space: O(1)


NAIVE RECURSION:
Time:  O(2^N)
Space: O(N)


                    (n)                                 1
              /              \
           (n-1)           (n-2)                       2
      /           \      /         \ 
    (n-2)        (n-3) (n-3)     (n-4)                  4
                ....
                                                       2^n

                                                       
#_of_nodes * work_per_node = overall_work

2^N * 1 = O(2^N)
                                                       
(1)  (1) (0) (0)

Recursive Tree



                    (4)5
              /              \
           (3)3               (2)2
      /           \      /         \
    (2)2          (1)1    (1)1     (0)1
  /     \
(1)1     (0)1
         

Helper:
count = 5
path = [4, 3, 2, 0]

                    (4) 
              /              \
           (3)                (2) 
      /           \      /         \
    (2)           (1)*    (1)*     (0)*
  /     \
(1)*     (0)*

------
CALL STACK


Base Case(s):
  * if n is 0 or 1:
    return 1

Recursive Case(s):
  * fib(n) = fib(n-1) + fib(n-2)
  * how can I define this problem in terms smaller version(s) of the same problem



----------------------

Pure Recursion
  * relies soley on return values
  * defines no additional helper functions
  * doesn't include any extra "state" or new parameters
  * input/ouput -> NO side effects
  

Helper Method Recursion
  * involves defining a helper function
  * doesn't have to use return values
  * can share a "global" state across function calls
  * can define additional parameters
  * can have side effects


Indicators you should use recursion:
  * Smaller versions of the problem are helpful for solving larger versions of the same problem
  * There is a "smallest" version of the problem
  * combinations/permutations
  * DFS 

                            [Iteration]     
             [  Dynamic Programming  ]     
Recursion -> Memoization -> Tabulation


"""

def fib(n):
  # base case(s)
  if n == 0 or n == 1:
    return 1
  
  # recursive case(s)
  return fib(n-1) + fib(n-2)

print(fib(7))

def helper_fib(n):
  result = 0

  def traverse(n):
    nonlocal result
    if n == 0 or n == 1:
      result += 1
      return
      
    traverse(n-1)
    traverse(n-2)

  traverse(n)
  return result

print(helper_fib(7))