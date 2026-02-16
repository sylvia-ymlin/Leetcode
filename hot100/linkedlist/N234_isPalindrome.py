# Palindrome linked list must be symmetric
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Fast and slow pointers to find midpoint
        # Question does not forbid modifying linked list, so we can reverse linked list
        # Then compare first half and second half

        # Empty node or single node
        if not head or not head.next:
            return True
        # Fast and slow pointers to find middle node, while reversing first half linked list
        slow = fast = head
        pre = None
        while fast and fast.next:
            # Fast pointer moves
            fast = fast.next.next
            # Slow pointer moves and reverses linked list
            next_slow = slow.next
            slow.next = pre
            pre = slow
            slow = next_slow

        # Now pre points to first half nodes
        if fast:  # Odd number of nodes, slow is at middle node
            slow = slow.next  # Skip middle node

        while slow:
            if pre.val != slow.val:
                return False
            pre = pre.next
            slow = slow.next
        
        return True