# Recursion

<!-- https://docs.google.com/document/d/1Uhnldz90UuZU5vDdVRAQgV49aKyR7ieafbmJTrVAH0U/edit?usp=sharing -->

## When are some indicators I should use recursion?

- A quick test for recursion is to take a random smaller instance of the problem and ask:

  - Is the solution to the subproblem useful for a larger problem?
  - If Yes, then we have established some form of nesting that recursion is suited for

- Recursion is especially good for working on things that have many possible branches that are too complex for an iterative approach

- Good when you want to explore all possibilities of a decisions space, such as describing a brute force algorithm
- Good when you are dealing with data structures that are nested or recursive

  - JSON
  - Tree
  - Linked Lists
  - Hierarchies

- How do I solve a recursion problem?
  - Use a recursive tree tree
    - A recursive tree summarizes how a large problem can be recursively broken down into smaller versions of the same problem. The leaf nodes of a decision tree identify base cases. The relationship between intermediate nodes and child nodes define the recursive relationship.
- Identify base case and recursive cases
  - Once these are identified, the problem is essentially solved by an existing template
  - In the case of pure recursion, we should also identify inputs and outputs
  - In the case of a helper recursion, we should identify the external state shared amongst recursive calls and how the recursion interacts with it
- Decide between pure vs helper recursion

  - Pure recursion is generally better for deriving a recursive relationship due to the lack of side effects. The state transition can be elegantly described as a pure function of multiple states. However, state can be tricky for some outcoders to fully grasp which could make pure recursion less useful.
  - Pure recursion, while elegant and succinct, is less useful for generating all possibilities due to copying of data between state transitions. Helper functions are more useful in these situations.
  - Helper recursion is necessary when the recursion input is different from the original problem’s input.

- Pruning branches

  - Some recursive relationships have conditional branching. Pruning branches of a decision tree will improve the branching factor of your decision tree and thus the Big O runtime
  - Backtracking to reuse state between transitions
    - As with helper recursion, we can apply backtracking to avoid copying too much state between recursive calls and reuse & modify the existing state instead. In particular, backtracking is a step after a recursive call to revert the state back to its original value.

- Write a template for Pure Recursion

```python
def pure_dfs(state):
    # IMPLEMENT base case
    if ...is_basecase(state):
        return ...

    # IMPLEMENT recursive formula
    ans = ...combine(dfs(branch_1),dfs(branch_2), ...)

    return ans

Write a template for Helper Method Recursion
# Variation 1 (Prune after recursive branch)

ans = []
def helper_dfs(state, path):

    # IMPLEMENT base case
    if ...is_basecase(state):
        ans.append( ... )
        return
    # IMPLEMENT pruning logic
    if ...should_prune(branch):
        continue

    # IMPLEMENT visit state
    ...visit(state)

    # IMPLEMENT recursive case branching
    for branch in ...get_branches(state):


        # IMPLEMENT state update each branch
        new_state = ...update(state, branch)
        path.add(branch)

  dfs(new_state, path)

        # IMPLEMENT backtrack if necessary
        path.pop()
        old_state =  ...revert(new_state, branch)

return ans

# Variation 2 (Prune before recursive branch)

ans = []
def helper_dfs(state, path):

    # IMPLEMENT base case
    if ...is_basecase(state):
        ans.append( ... )
        return

    # IMPLEMENT recursive case branching
    for branch in ...get_branches(state):

        # IMPLEMENT pruning logic
        if ...should_prune(branch):
            continue

        # IMPLEMENT visit state
        ...visit(state)

        # IMPLEMENT state update each branch
        new_state = ...update(state, branch)
        path.add(branch)

  dfs(new_state, path)

        # IMPLEMENT backtrack if necessary
        path.pop()
        old_state =  ...revert(new_state, branch)

return ans
```

What is the runtime and space complexity of a recursive algorithm?

```
Runtime = (Time Spent Per State) * BranchFactor(MaxRecursionDepth)

Space = MaxRecursionDepth + OutputSize
```
