"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.



Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:

Input: lists = []
Output: []

Example 3:

Input: lists = [[]]
Output: []


"""

from merge_two_sorted_list import merge_sorted_list


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def merge_k_sorted_list(lists):
    if lists is None or len(lists) == 0:
        return None
    return helper(lists, 0, len(lists) - 1)


def helper(lists, left, right):
    if left == right:
        return lists[left]

    mid = (left + right) // 2
    left_head = helper(lists, left, mid)
    right_head = helper(lists, mid + 1, right)

    return merge_sorted_list(left_head, right_head)


def create_linked_list(values):
    dummy = ListNode(0)
    curr = dummy
    for val in values:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


def print_linked_list(head):
    curr = head
    while curr:
        print(curr.value, end="-->")
        curr = curr.next
    print("None")


lists = [
    create_linked_list([1, 4, 5]),
    create_linked_list([1, 3, 4]),
    create_linked_list([2, 6]),
]

print_linked_list(merge_k_sorted_list(lists))
