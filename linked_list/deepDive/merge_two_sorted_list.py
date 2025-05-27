""" 

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

 
"""

__all__ = ["merge_sorted_list"]


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def merge_sorted_list(list1: ListNode, list2: ListNode) -> ListNode:
    dummy = ListNode(0)
    curr = dummy

    while list1 and list2:
        if list1.value <= list2.value:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next

    curr.next = list1 if list1 else list2

    return dummy.next


# Helper function to create a linked list from a Python list
def create_linked_list(values):
    dummy = ListNode(0)
    curr = dummy
    for val in values:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


# Helper function to print a linked list
def print_linked_list(head):
    curr = head
    while curr:
        print(curr.value, end=" -> ")
        curr = curr.next
    print("None")


# Test the function
list1 = create_linked_list([1, 2, 4])
list2 = create_linked_list([1, 3, 4])

merged = merge_sorted_list(list1, list2)
print_linked_list(merged)
