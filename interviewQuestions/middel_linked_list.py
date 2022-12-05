# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        counter = 0
        new_head = head
        if head is None:
            print("Ths singlyLinkList does not exist")
        else:
            node = head
            while node is not None:
                print(node.val)
                counter += 1
                node = node.next
        mid = counter//2 + counter % 2 if counter % 2 > 0 else counter//2 + 1
        # mid = counter //2 +1

        for _ in range(1, mid):
            new_head = new_head.next
        return new_head


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        single_jump = head
        double_jump = head

        while double_jump:
            double_jump = double_jump.next
            if double_jump:
                single_jump = single_jump.next
                double_jump = double_jump.next
        return single_jump
