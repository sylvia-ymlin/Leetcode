# 合并 k 个 升序链表
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import List, Optional

# 最直观解法：暴力解法
# 插入数组，排序，构建链表
# 时间复杂度 O(nlogn)，空间复杂度 O(n)
class Solution1:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        # 将所有链表的节点放入数组
        nodes = []
        for lst in lists:
            while lst:
                nodes.append(lst)
                lst = lst.next

        # 排序
        nodes.sort()
        
        # 构建新的链表
        dummy = ListNode(0)
        cur = dummy
        for node in nodes:
            cur.next = node
            cur = cur.next

        cur.next = None  # 最后一个节点的 next 设为 None
        return dummy.next

# iteration
# 每次循环找出最小值链表
# 时间复杂度 O(nk)，其中 n 是所有链表节点总数，k 是链表个数
# 空间复杂度 O(1)，不使用额外空间
from typing import List, Optional
class Solution2:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ListNode(0) # 简化边界处理，dummy node
        cur = res

        while True:
            minNode = -1 # 记录最小值链表所在索引
            for i in range(len(lists)):
                if not lists[i]: # 跳过空表
                    continue 
                if minNode == -1 or lists[minNode].val > lists[i].val: # 没有最小值表，直接赋值；有，比较
                    minNode = i

            if minNode == -1:
                break # 所有表空
            # 连接最小值节点
            cur.next = lists[minNode]
            # 删除最小值节点
            lists[minNode] = lists[minNode].next
            # 结果链表前进一步
            cur = cur.next

        return res.next

# one by one merge
# 每次合并两个链表，直到所有链表合并完成
# 时间复杂度 O(nk)，其中 n 是所有链表节点总数，k 是链表个数
# 空间复杂度 O(1)，不使用额外空间
class Solution3:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            res = ListNode(0)
            cur = res
            
            while l1 and l2:
                if l1.val < l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next
            if l1:
                cur.next = l1
            elif l2:
                cur.next = l2

            return res.next
        
        if not lists:
            return None
        
        for i in range(1, len(lists)):
            lists[0] = mergeTwoLists(lists[0], lists[i])

        return lists[0]


# 维护 k 个链表的头结点，堆
# 时间复杂度 O(n log k)，其中 n 是所有链表节点总数，k 是链表个数
# 空间复杂度 O(k)，使用堆存储 k 个链表的头结点
import heapq
class Solution4:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        res = ListNode(0)
        cur = res
        minHeap = [] # 最小堆

        for lst in lists:
            if lst is not None:
                # 将每个链表的头结点放入堆中
                heapq.heappush(minHeap, NodeWrapper(lst))

        # 堆不为空，链表没有合成完毕
        while minHeap:
            # 取出最小值
            node_wrapper = heapq.heappop(minHeap)
            # 插入
            cur.next = node_wrapper.node
            # 前进一步
            cur = cur.next
            # 如果该链表还有下一个节点，放入堆中
            if node_wrapper.node.next:
                heapq.heappush(minHeap, NodeWrapper(node_wrapper.node.next))

        return res.next

# python 的 headpq 不能直接比较 ListNode，需要包装一下
class NodeWrapper:
    def __init__(self, node: ListNode):
        self.node = node

    # 定义比较规则
    def __lt__(self, other):
        return self.node.val < other.node.val

# 分二治之
# 分治法：将 k 个链表分成两半，递归合并
            #     mergeKLists([0,1,2,3])
            #              /            \
            #     divide([0,1])        divide([2,3])
            #        /     \              /      \
            # divide([0]) divide([1]) divide([2]) divide([3])
            #    |        |          |           |
            #  list0    list1      list2       list3
            #    |        |          |           |
            #    \       /           \          /
            #     conquer              conquer
            #        |                    |
            #    merged01             merged23
            #        \                  /
            #         \                /
            #           conquer
            #              |
            #        final result
# 时间复杂度 O(n log k)，其中 n 是所有链表节点总数，k 是链表个数
# 空间复杂度 O(log k)，递归栈空间
class Solution5:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        return self.divide(lists, 0, len(lists) - 1)
    
    # 分链表
    def divede(self, lists: List[Optional[ListNode]], left: int, right: int) -> Optional[ListNode]:
        if left == right: # 只有一个链表
            return lists[left]
        mid = (left + right) // 2
        # 分成两半
        l1 = self.divede(lists, left, mid) # 递归处理左半边链表
        l2 = self.divede(lists, mid + 1, right) # 递归处理右半边链表
        # 合并两半
        return self.mergeTwoLists(l1, l2)

    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0)
        cur = res

        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        if l1:
            cur.next = l1
        elif l2:
            cur.next = l2

        return res.next