# Reverse Linked List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Pointers reverse forward
        pre = None
        cur = head
        while cur:
            next_node = cur.next
            cur.next = pre  # Reverse pointer
            pre = cur
            cur = next_node  # Move to next node
        # When loop ends, cur is None, pre is new head node
        return pre  # Return new head node