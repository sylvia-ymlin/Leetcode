# merge two sorted linked lists
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # return a new sorted list

        res = ListNode()  # dummy node
        cur = res

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        
        if list1:
            cur.next = list1
        elif list2:
            cur.next = list2

        return res.next

# time complexity: O(m+n), where m and n are the lengths of the two lists
# space complexity: O(1), since we are not using any extra space except for the dummy node