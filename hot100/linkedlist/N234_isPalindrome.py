# 回文链表一定对称
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 快慢指针找到中点
        # 题目没有要求不能修改链表，所以可以反转链表
        # 然后比较前半部分和后半部分是否相等

        # 空节点或单个节点
        if not head or not head.next:
            return True
        # 快慢指针找到中间节点，同时翻转前半部分链表
        slow = fast = head
        pre = None
        while fast and fast.next:
            # 快指针移动
            fast = fast.next.next
            # 慢指针移动和翻转链表
            next_slow = slow.next
            slow.next = pre
            pre = slow
            slow = next_slow

        # 此时 pre 指向前半段节点
        if fast:  # 奇数个节点，slow 在中间节点
            slow = slow.next  # 跳过中间节点

        while slow:
            if pre.val != slow.val:
                return False
            pre = pre.next
            slow = slow.next
        
        return True