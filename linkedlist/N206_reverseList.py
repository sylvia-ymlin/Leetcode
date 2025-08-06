# 翻转链表
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 指针向前翻转
        pre = None
        cur = head
        while cur:
            next_node = cur.next
            cur.next = pre  # 翻转指针
            pre = cur
            cur = next_node  # 移动到下一个节点
        # 循环结束时，cur 为 None，pre 为新的头节点
        return pre  # 返回新的头节点