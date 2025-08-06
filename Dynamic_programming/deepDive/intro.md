https://docs.google.com/document/d/1UV4aUeP-gNhUN-cKaECYQrqhkzCkddgHjGTHyy8T1I8/edit?usp=sharing

https://docs.google.com/document/d/15ZKNn2axdWYQkSxA6AOHtm9CAGVsHwpQs3_1QzqKkR4/edit?usp=sharing

Dynamic Programming
What are some indicators I should use dynamic Programming
Recursive problem
No recursion, no DP.
DP is an optimization applied to a recursive problem.
The recursion tree should have duplicate nodes.
This is often expressed as:
Optimal substructure (i.e. recursion).
Overlapping subproblems (i.e. duplicate nodes in the recursion tree)
Remember that the recursion tree is your best friend when it comes to any
DP problem. That’s where you should start from in the absence of any other clues.
How to find the subproblems (i.e. recursion)
Always start from a tree and try to draw it.
Solve the problem in simpler inputs.
F(N)
F(1)=?
F(2)=?
F(3)=?
F(4)=?

How do I solve a dynamic programming problem?
Memoization:
Write the recursion and add a memo to it. Let’s say I have
F(i1, i2, …, ik) -> output_type. E.g. F(1, 1.2, ‘c’) = 1.23
A dictionary (map): < (i1, i2, …, ik) , output_type>
E.g. a map of (int, float, character) to float
Often, it’s a map of a tuple to the output_type.
If the tuple type is all the same: e.g. (int, int, int) what can we do?
Map of array of int to output_type.
Array
When all (i1, i2, …, ik) are integer, I can use represent the map as an k-dimensional array:
Key is the index of the array, which is [i1, i2, …, ik] and the value is the content of array[i1, i2, …, ik].
Note that if the indices are negative, we might have to do some shifting transformations.
If you can do both Array and map, which one is preferred?
The access time for both can be O(1), but in practice looking up in an array is much faster than a map.
A map can be potentially smaller in memory compared to an array, because it’s possible that we dont’ have all possible keys as we generate the nodes in the recursion tree. But if you know that all possible keys would exist, an array is better in terms of memory.

Tabulation
We start from the bottom (base case or leaves of the tree) and move to the top (the root of the tree).
Create a table that stores the values.
Array (similar to memoization)

    There is no recursive call in Tabulation!

Write a template for memoizing a function

What is the runtime & space complexity of a memoized recursive function?
Runtime: O(n), where n is the max number of the keys in the map or equivalently n is the size of the array.
n: Number of the unique nodes in the tree
Space:
The size of memo (same as runtime).
