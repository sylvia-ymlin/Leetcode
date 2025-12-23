# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


from typing import Optional
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 快慢指针法, 如果有环，快慢指针终会相遇，且无 none
        slow = fast = head
        while fast and fast.next:
            slow = slow.next  # 慢指针每次走一步
            fast = fast.next.next  # 快指针每次走两步
            if slow == fast:  # 相遇，说明有环
                return True
        # 没有环，遇到 None, 退出循环
        return False
        