"""
Create a new data structure,
"""

from abc import ABC, abstractmethod
from typing import Optional


class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class IRecencyList(ABC):
    """Abstract interface for managing node recency."""

    @abstractmethod
    def move_to_front(self, node: Node) -> None:
        """Moves an existing node to the front (Most Recently Used)."""
        pass

    @abstractmethod
    def remove(self, node: Node) -> None:
        """Removes a specific node from the list."""
        pass

    @abstractmethod
    def remove_last(self) -> Optional[Node]:
        """Removes and returns the last node (Least Recently Used)."""
        pass

    @abstractmethod
    def add_to_front(self, node: Node) -> None:
        """Adds a new node to the front (Most Recently Used)."""
        pass


class DoublyLinkedList(IRecencyList):
    def __init__(self):
        # Initialize sentinels (dummy head and tail)
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _insert_after(self, where, node):
        node.next = where.next
        node.prev = where
        where.next.prev = node
        where.next = node

    def add_to_front(self, node: Node) -> None:
        """Adds a new node to the front (Most Recently Used)."""
        self._insert_after(self.head, node)

    def remove(self, node: Node) -> None:
        """Removes a specific node from the list."""
        prev_node = node.prev
        next_node = node.next

        if prev_node and next_node:
            prev_node.next = next_node
            next_node.prev = prev_node

            node.prev = node.next = None

    def move_to_front(self, node: Node) -> None:
        """Moves an existing node to the front (Most Recently Used)."""
        self.remove(node)
        self._insert_after(self.head, node)

    def remove_last(self) -> Optional[Node]:
        """Removes and returns the last node (Least Recently Used)."""
        lru = self.tail.prev

        if lru is self.head:
            return None

        self.remove(lru)
        return lru


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # We hardcoded DoublyLinkedList due to Leetcode requirement, otherwise, we should use dependancy injection
        self.recency_list = DoublyLinkedList()
        self.map: dict[int, Node] = {}

    def get(self, key: int) -> int:
        node = self.map.get(key)
        if node is None:
            return -1

        self.recency_list.move_to_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        # If it's in the map, overwrite the value
        if key in self.map:
            node = self.map.get(key)
            node.val = value
            self.recency_list.move_to_front(node)
            return

        # Otherwise add a new entry
        new_node = Node(key, value)
        self.recency_list.add_to_front(new_node)
        self.map[key] = new_node

        # Check for capacity
        if len(self.map) > self.capacity:
            lru = self.recency_list.remove_last()

            if lru:
                del self.map[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)