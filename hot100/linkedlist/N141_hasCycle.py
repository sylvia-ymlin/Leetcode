# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


from typing import Optional
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Fast and slow pointers method. If there is a cycle, fast and slow pointers will eventually meet, and no none
        slow = fast = head
        while fast and fast.next:
            slow = slow.next  # Slow pointer moves one step at a time
            fast = fast.next.next  # Fast pointer moves two steps at a time
            if slow == fast:  # Meet, meaning there is a cycle
                return True
        # No cycle, encountered None, exit loop
        return False
        