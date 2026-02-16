# Return the node where the cycle begins; return null if no cycle

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import Optional
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Fast and slow pointers method
        # When fast and slow pointers meet
        # Assume cycle node a, cycle length b
        # Fast and slow pointers meet at c
        # Slow pointer: x
        # Fast pointer: 2x
        # Relation: 2(a + c) = a + c + n * b
        # i.e.: a + c = n * b
        # i.e. current slow pointer has walked integer multiple of cycle length
        # After meeting, one pointer starts from head, another starts from meeting point
        # Two pointers will meet at cycle entry, because c + a walks cycle length, at cycle entry
        # The other pointer a also walks to cycle entry

        slow = fast = head
        while fast and fast.next:
            slow = slow.next  # Slow pointer moves one step
            fast = fast.next.next  # Fast pointer moves two steps
            if slow == fast:  # Meet, meaning there is a cycle
                break
        
        if not fast or not fast.next:
            return None  # No cycle, return None
        
        # Has cycle, find cycle entry
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow  # Return cycle entry node                           

# Methodology is simple, fast and slow pointers, reset slow pointer to head
# Key is to prove correctness of the method