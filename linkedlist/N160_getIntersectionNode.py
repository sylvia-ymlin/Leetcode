# 找出两个单链表相交的起始点
# 哈希法：将其中一个链表的节点存入哈希表，添加另一个链表的节点直到节点已经存在在哈希表中，返回该节点就是相交点
# 时间复杂度：O(m+n)，空间复杂度：O(m)


# 优化，没有额外存储空间：双指针法
# 链表 A: a + c
# 链表 B: b + c
# a = b, 则两个指针指向相等节点，找到相交点
# a < b, 需要走过 a + b + c
# 我们通过双指针要找到相交点，需要一个指针指向 A 的 a，一个指向 B 的 b
# 即 让指针 A 遍历链表 A，后指向 B, 让指针 B 遍历链表 B，后指向 A; 指针共同走过 a + b + c 后，指针 A 和 B 会相遇在相交点 c
# 时间复杂度：O(m+n)，空间复杂度：O(1)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # input, 链表不为空
        pA = headA
        pB = headB

        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA

        # 循环⏏️条件： pA == pB
        # 有相交节点
        # 或无相交节点，返回 None
        return pA