/**
 * 
 * Merge k Sorted Lists

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
merging them into one sorted linked list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []

 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists == null || lists.length == 0) {
            return null;
        }
        return helper(lists, 0, lists.length - 1);
    }

    ListNode helper(ListNode[] lists, int left, int right) {
        if (left == right) {
            return lists[left];
        }

        // divide
        int mid = (left + right) / 2;
        ListNode leftHead = helper(lists, left, mid);
        ListNode rightHead = helper(lists, mid + 1, right);

        // merge
        ListNode mergeHead = mergeTwoLists(leftHead, rightHead);

        return mergeHead;
    }


    public ListNode mergeTwoLists(ListNode node1, ListNode node2) {
        ListNode dummy = new ListNode(-1);
        ListNode newCur = dummy;

        while (node1 != null && node2 != null) {
            if (node1.val <= node2.val) {
                newCur.next = node1;
                node1 = node1.next;
            } else {
                newCur.next = node2;
                node2 = node2.next;
            }

            newCur = newCur.next;
        }

        if (node1 != null) {
            newCur.next = node1;
        }

        if (node2 != null) {
            newCur.next = node2;
        }

        return dummy.next;
    }
}