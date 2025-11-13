# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """ 
    head = [1,2,3,4,5]
    prev
            current
            fallowing   

    we have to move following node to the next node but start from head if head is just empty node so we have have to track of it. 
    then curr.next should be prev node 
    and move the previous node one jump a head to the currnode. 
    and move curr node to the following node. 

    https://medium.com/outco/reversing-a-linked-list-easy-as-1-2-3-560fbffe2088
    """

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # all the time we need just three node
        prev = None
        current = head
        fallowing = head

        while current:
            fallowing = fallowing.next
            current.next = prev
            prev = current
            current = fallowing
        return prev
