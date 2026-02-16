# Reverse linked list in groups of K, if not enough for a group, keep original order (at end)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Key point is whether the last group needs to be reversed
        dummy = ListNode(0, head)
        groupPrev = dummy  # Tail node of previous group
        
        while True:
            # Check if there are k nodes - check from current group
            kth = groupPrev
            for i in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next  # Not enough k nodes
            
            groupNext = kth.next  # Head of next group
            
            # Reverse current group: from groupPrev.next to kth
            prev, curr = groupNext, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            # Connect:
            # 1. Previous group connects to new head of current group (kth)
            tmp = groupPrev.next  # Save head of current group before reverse
            groupPrev.next = kth  # Connect to head after reverse
            groupPrev = tmp       # Update previous group tail to tail after reverse

        return dummy.next
