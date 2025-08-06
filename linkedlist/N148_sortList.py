# 链表排序
# 递归、归并排序
# 时间复杂度 O(nlogn)
# 空间复杂度 O(logn) -> 递归栈调用

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 拆分 + 排序
        # don't include tail
        def sortFunc(head: ListNode, tail: ListNode) -> ListNode:
            if not head: # 空
                 return head
             
            if head.next == tail: # 单个节点
                 head.next = None
                 return head

            # find the mid
            slow = fast = head
            while fast != tail:
                slow = slow.next
                fast = fast.next
                if fast != tail:
                    fast = fast.next
            
            mid = slow

            return merge(sortFunc(head, mid), sortFunc(mid, tail))

        def merge(head1: ListNode, head2: ListNode) -> ListNode:
            # 合并两个有序链表
            dummy = ListNode(0)
            temp, temp1, temp2 = dummy, head1, head2
            while temp1 and temp2:
                if temp1.val <= temp2.val:
                    temp.next = temp1
                    temp1 = temp1.next
                else:
                    temp.next = temp2
                    temp2 = temp2.next
                temp = temp.next

            if temp1:
                temp.next = temp1
            else:
                temp.next = temp2

            return dummy.next

        return sorted(head, None)