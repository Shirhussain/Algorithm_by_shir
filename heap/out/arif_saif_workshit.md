the full detail is in https://docs.google.com/document/d/1Pywez4fFN1L7hysgrPwsNKpd5QNKXMgYGCTpg_D7-0E/edit?usp=sharing

https://docs.google.com/document/d/1LIKP68y9G63u6LH_Q_495D7DjEm6qdrPY7hTvceCNxE/edit?usp=sharing

Heap
What is a min heap?
It’s a complete binary tree.
Why is this important?
We can get to log n height.
We can put the entire tree in an array without wasting memory.
We can find the index of each child if we have the index of the parent.
Each child is less than both parents.
What is good about a min heap?
It is a very efficient data structure, it’s almost as if you have an array!
We can find the minimum value in O(1), which is much better than a simple array where this operation takes O(n).
In return push and pop have O(log n). Compare this to O(1) push_back and pop_back for a vector (or a list in python).

What are some indicators I should use a Heap
When you are required to find min/max repeatedly.
Especially when you also push and pop, i.e. add to the heap and remove the minimum. (A great example usage is the Uber application that finds the closest driver to you. Another famous example is the Dijkstra algorithm.)
When you can get away with only partial sorting of your collection rather than total sorting.
When finding the Kth min/max
https://leetcode.com/problems/kth-largest-element-in-an-array/description/

How do I solve a Heap problem
When you see a problem you can use a heap, as much as possible, avoid implementing the heap yourself, chances are you can assume you have a heap class as a blackbox and use it. E.g.
Python: heapq
Javascript: doesn’t have a built in one, but you can always assume you have a Heap class that you can instantiate.
There are also several packages you can install: https://www.npmjs.com/package/heap
CPP:
std::priority_queue
Std::make_heap
What’s the relationship between priority queue and heap?
It’s an abstract data structure. It’s like having an interface (abstract class) without knowing what is inside. For example, a priority queue has this interface:
Push(value)
Pop(): the highest priority will be popped (Unline FIFO order)
Top()
Empty()
Heap can be used to implement a priority queue.

What are the operations on a heap and what are their runtimes?
Push(value): log n
Pop(): log n
Top(): O(1)
Empty(): O(1)
Runtime for creating a heap?
Algorithm 1: O (n log n): insertion in an empty heap, n times.
Algorithm 2: O (n). See here.

https://leetcode.com/problems/relative-ranks/submissions/1475781511
https://leetcode.com/problems/k-closest-points-to-origin/submissions/1475790148
