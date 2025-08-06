# K 个一组翻转链表，不满一组，保持原序（末尾）

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 重点在于，最后一组是否需要翻转
        dummy = ListNode(0, head)
        groupPrev = dummy  # 前一组的尾节点
        
        while True:
            # 检查是否有k个结点 - 从当前组开始检查
            kth = groupPrev
            for i in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next  # 不足k个节点
            
            groupNext = kth.next  # 下一组的开头
            
            # 翻转当前组：从groupPrev.next到kth
            prev, curr = groupNext, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            # 连接：
            # 1. 前一组连接到当前组新的头部(kth)
            tmp = groupPrev.next  # 保存当前组翻转前的头部
            groupPrev.next = kth  # 连接到翻转后的头部
            groupPrev = tmp       # 更新前一组尾部为翻转后的尾部

        return dummy.next
