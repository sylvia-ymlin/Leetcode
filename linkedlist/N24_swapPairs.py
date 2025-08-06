class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        dummy = ListNode(0, head)
        pre = dummy
        cur = head
        while cur and cur.next:
            # pre -> A -> B
            A = cur
            B = cur.next
            # 交换 A 和 B
            # pre -> B -> A
            pre.next = B
            A.next = B.next
            B.next = A
            pre = A
            cur = A.next
        
        return dummy.next
            

