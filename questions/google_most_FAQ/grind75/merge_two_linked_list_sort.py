# # You are given the heads of two sorted linked lists list1 and list2.

# # Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# # Return the head of the merged linked list.
# from typing import Optional

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
    
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         dummy = ListNode()
#         tail = dummy

#         while list1 and list2:
#             if list1.val < list2.val:
#                 tail.next = list1
#                 list1 = list1.next
#             else:
#                 tail.next = list2
#                 list2 = list2.next
#             tail = tail.next
#         if list1:
#             tail.next = list1
#         if list2:
#             tail.next = list2
#         return dummy.next



# list1,list2 = [1,2,4],[1,3,4]
# s = Solution()

# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

 

# Example 1:

# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

# Example 2:

# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.

 

# Constraints:

#     1 <= s.length <= 2000
#     s consists of lowercase and/or uppercase English letters only.

from collections import Counter 

def longest_palindrome(s):
    # if it's even it' means that we can put in both side but we can only use one odd character in the string
    # because it can be placed in the middle palindrome 
    counter = Counter(s)
    odd_counter = 0
    
    for char in counter.keys():
        # check if it's odd
        if counter[char] % 2:
            odd_counter += 1
    return len(s) - odd_counter + 1 if odd_counter else len(s)

    # or
    # odd_counter = sum(1 for char in counter.keys() if counter[char] % 2)
    # return len(s) - odd_counter + 1 if odd_counter else len(s)


            