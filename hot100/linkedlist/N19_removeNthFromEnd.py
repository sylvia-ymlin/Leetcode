# 删除链表倒数第 N 个结点 

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 快慢指针，快指针先行 n 步
        # 快指针指向最后一个结点时，慢指针指向要删除结点的前一个
        dummy = ListNode(0, head)
        slow, fast = dummy, dummy
        for _ in range(n):
            fast = fast.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        
        if slow == dummy: # 删除头结点
            head = head.next
        else:
            slow.next = slow.next.next
        
        return head

# 注意添加头节点和处理逻辑