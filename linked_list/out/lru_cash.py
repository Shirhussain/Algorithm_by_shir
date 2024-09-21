""" 
146. LRU Cache


Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

    LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    int get(int key) Return the value of the key if the key exists, otherwise return -1.
    void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4


"""


class ListNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Dictionary to store the key and corresponding ListNode
        self.head = None  # Least recently used (LRU)
        self.tail = None   # Most recently used (MRU)

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # Remove the node from its current position
            self._remove_node(node)
            # Move the node to the most recently used position
            self._set_recent_used(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # If the key exists, update the value and move the node to MRU position
            node = self.cache[key]
            node.val = value
            self._remove_node(node)
            self._set_recent_used(node)
        else:
            # If it's a new key
            node = ListNode(key, value)
            if len(self.cache) >= self.capacity:
                # Remove the least recently used (LRU) element
                del self.cache[self.head.key]
                self._remove_node(self.head)
            # Add new node to the cache and set it as most recently used (MRU)
            self.cache[key] = node
            self._set_recent_used(node)

    def _remove_node(self, node: ListNode):
        """Helper method to remove a node from the doubly linked list."""
        prev = node.prev
        next = node.next

        if prev is None:
            # If the node is the head one (LRU), update the head pointer
            self.head = node.next
        else:
            prev.next = next

        if next is None:
            # If the node is the tail one (MRU), update the tail pointer
            self.tail = node.prev
        else:
            next.prev = prev

    def _set_recent_used(self, node: ListNode):
        """Helper method to set the node as the most recently used (MRU)."""
        node.prev = None
        node.next = None

        if self.tail is None:
            # If the cache is empty, the node becomes both head and tail
            self.head = node
            self.tail = node
        else:
            # Move the node to the end (most recently used)
            self.tail.next = node
            node.prev = self.tail
            self.tail = node


# Example usage:
cache = LRUCache(2)

# Put key-value pairs in the cache
cache.put(1, 1)
cache.put(2, 2)

# Get value for key 1 (will return 1)
print(cache.get(1))  # Output: 1

# Add another key-value pair, will evict key 2 since capacity is 2
cache.put(3, 3)

# Get value for key 2 (will return -1 since key 2 has been evicted)
print(cache.get(2))  # Output: -1

# Add another key-value pair, will evict key 1
cache.put(4, 4)

# Get value for key 1 (will return -1 since key 1 has been evicted)
print(cache.get(1))  # Output: -1

# Get value for key 3 (will return 3)
print(cache.get(3))  # Output: 3

# Get value for key 4 (will return 4)
print(cache.get(4))  # Output: 4
