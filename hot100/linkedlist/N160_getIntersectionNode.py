# Find the intersection node of two singly linked lists
# Hash Map Method: Store nodes of one list into hash map, add nodes of another list until node already exists in hash map, return that node as intersection point
# Time Complexity: O(m+n), Space Complexity: O(m)


# Optimization, no extra storage space: Two Pointers Method
# List A: a + c
# List B: b + c
# a = b, then two pointers point to equal node, find intersection point
# a < b, need to walk a + b + c
# We use two pointers to find intersection point, need one pointer point to a of A, one point to b of B
# i.e. let pointer A traverse list A, then point to B, let pointer B traverse list B, then point to A; after pointers walk a + b + c together, pointer A and B will meet at intersection point c
# Time Complexity: O(m+n), Space Complexity: O(1)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # input, linked list not empty
        pA = headA
        pB = headB

        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA

        # Loop exit condition: pA == pB
        # Has intersection node
        # Or no intersection node, return None
        return pA