https://docs.google.com/document/d/1lA0-lfkrG9KVk88mgJtHnlrPpTVlVoOlSkOawfJXzrA/edit?usp=sharing

What are some indicators I should use dynamic Programming?

- Repeated work.
- Overlapping subproblems.
  - Are they useful in solving a larger problem?
- Optimal substructure.
- Brute force gives exponential time solution,
  we want something more like linear!
-

How do I solve a dynamic programming problem?

- Might start with brute-force recursive program.
- Then improve by either
  -- Memoization: add "memory" to the recursive solution. "Top down" strategy.
  -- Tabular: use a similar combination strategy to
  combine answers to subproblems, but build the
  answer from the "bottom up".

Write a template for memoizing a function

define cache
def rec(state):
if problem has been solved for this state
return the solution
ans = rec(new state) (perhaps multiple rec calls)
store answer for later use (memoize)
return ans

What is the runtime & space complexity of a memoized recursive function?

Runtime: linear in size of input
Space: size of cache + output size
