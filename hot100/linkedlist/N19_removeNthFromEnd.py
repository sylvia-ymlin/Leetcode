# Remove the Nth node from the end of the list

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Fast and slow pointers, fast pointer goes n steps first
        # When fast pointer points to the last node, slow pointer points to the previous node of the node to be deleted
        dummy = ListNode(0, head)
        slow, fast = dummy, dummy
        for _ in range(n):
            fast = fast.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        
        if slow == dummy: # Delete head node
            head = head.next
        else:
            slow.next = slow.next.next
        
        return head

# Note adding head node and handling logic