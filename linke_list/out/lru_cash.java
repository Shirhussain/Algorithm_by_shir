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

class LRUCache {

    // Map<3, Node> map: not ordered 
    // a data structure to track the visit history: must be ordered

    // doubly linked list

    // 3 <-> 1 <-> 2 <->  <-> 4 <-> 5

    // first.                  least recently used

    // node.next = first
    // first = node;

    // first = node
    // last = node

    ListNode first = null;
    ListNode last = null;
    Map<Integer, ListNode> map = new HashMap<>();
    int capacity = 0;

    public LRUCache(int capacity) {
        this.capacity = capacity;
    }
    
    public int get(int key) {
        if (map.containsKey(key)) {
            ListNode node = map.get(key);
            removeNode(node);
            setRecentUsed(node);
            return node.value;
        }

        return -1;
    }
    
    public void put(int key, int value) {
        if (map.containsKey(key)) {
            ListNode node = map.get(key);
            node.value = value;
            removeNode(node);
            setRecentUsed(node);
        } else {
            // a new element
            ListNode node = new ListNode(key, value);
            if (map.size() >= capacity) {
                // need to remove the least recent used element first
                map.remove(last.key);
                removeNode(last);
                map.put(key, node);
                setRecentUsed(node);
            } else {
                map.put(key, node);
                setRecentUsed(node);
            }
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */