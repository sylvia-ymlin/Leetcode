# 返回成环的节点；没有则返回 null

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import Optional
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 快慢指针法
        # 快慢指针相遇时
        # 设成环节点 a, 环长度 b
        # 快慢指针相遇在 c
        # 慢指针： x
        # 快指针： 2x
        # 关系：2(a + c) = a + c + n * b
        # 即：a + c = n * b
        # 即此时慢指针走过环长的整数倍
        # 相遇后，一个指针从头开始走，另一个指针从相遇点开始走
        # 两个指针会在成环节点相遇，因为 c + a 走过环长，在环入口处
        # 另一个指针 a 也走到环入口处

        slow = fast = head
        while fast and fast.next:
            slow = slow.next  # 慢指针每次走一步
            fast = fast.next.next  # 快指针每次走两步
            if slow == fast:  # 相遇，说明有环
                break
        
        if not fast or not fast.next:
            return None  # 没有环，返回 None
        
        # 有环，找到环的入口
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow  # 返回环的入口节点                           

# 方法论很简单，快慢指针，重置慢指针到链表头
# 重点是论证方法的正确性