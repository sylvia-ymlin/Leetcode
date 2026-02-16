# add two numbers, and the number is stored in a linked list, in reverse order

# return a new linked list

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Add and then carry
        dummy = ListNode()
        cur = dummy
        carry = 0 # Carry
        while l1 or l2 or carry:
            # Need to create new node
            cur.next = ListNode(carry)
            cur = cur.next
            cur.val += l1.val if l1 else 0
            cur.val += l2.val if l2 else 0

            carry = cur.val // 10  # Update carry
            cur.val %= 10  # Update value of current node

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next

test = Solution()
l1 = ListNode(0, ListNode(8, ListNode(8)))
l2 = ListNode(6, ListNode(7, ListNode(8)))
res = test.addTwoNumbers(l1, l2)
num = 0
while res:
    num = num * 10 + res.val
    res = res.next
print(num)