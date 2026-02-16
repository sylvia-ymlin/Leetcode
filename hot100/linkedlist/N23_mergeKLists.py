# Merge k sorted linked lists
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import List, Optional

# Most intuitive solution: Brute Force
# Insert into array, sort, build linked list
# Time Complexity O(nlogn), Space Complexity O(n)
class Solution1:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        # Put all nodes of linked lists into array
        nodes = []
        for lst in lists:
            while lst:
                nodes.append(lst)
                lst = lst.next

        # Sort
        nodes.sort()
        
        # Build new linked list
        dummy = ListNode(0)
        cur = dummy
        for node in nodes:
            cur.next = node
            cur = cur.next

        cur.next = None  # Set the next of the last node to None
        return dummy.next

# iteration
# Find min value linked list in each loop
# Time Complexity O(nk), where n is total total number of nodes, k is number of linked lists
# Space Complexity O(1), no extra space used
from typing import List, Optional
class Solution2:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ListNode(0) # Simplify boundary handling, dummy node
        cur = res

        while True:
            minNode = -1 # Record index of min value linked list
            for i in range(len(lists)):
                if not lists[i]: # Skip empty list
                    continue 
                if minNode == -1 or lists[minNode].val > lists[i].val: # No min value list, assign directly; if exist, compare
                    minNode = i

            if minNode == -1:
                break # All lists empty
            # Connect min value node
            cur.next = lists[minNode]
            # Delete min value node
            lists[minNode] = lists[minNode].next
            # Result linked list moves forward
            cur = cur.next

        return res.next

# one by one merge
# Merge two linked lists each time, until all linked lists are merged
# Time Complexity O(nk), where n is total total number of nodes, k is number of linked lists
# Space Complexity O(1), no extra space used
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


# Maintain head nodes of k linked lists, Heap
# Time Complexity O(n log k), where n is total total number of nodes, k is number of linked lists
# Space Complexity O(k), use heap to store head nodes of k linked lists
import heapq
class Solution4:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        res = ListNode(0)
        cur = res
        minHeap = [] # Min Heap

        for lst in lists:
            if lst is not None:
                # Put head node of each linked list into heap
                heapq.heappush(minHeap, NodeWrapper(lst))

        # Heap not empty, linked list merging not finished
        while minHeap:
            # Pop min value
            node_wrapper = heapq.heappop(minHeap)
            # Insert
            cur.next = node_wrapper.node
            # Move forward
            cur = cur.next
            # If this linked list has next node, put into heap
            if node_wrapper.node.next:
                heapq.heappush(minHeap, NodeWrapper(node_wrapper.node.next))

        return res.next

# python's heapq cannot directly compare ListNode, need wrapper
class NodeWrapper:
    def __init__(self, node: ListNode):
        self.node = node

    # Define comparison rule
    def __lt__(self, other):
        return self.node.val < other.node.val

# Divide and Conquer
# Method: Divide k linked lists into two halves, recursively merge
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
# Time Complexity O(n log k), where n is total total number of nodes, k is number of linked lists
# Space Complexity O(log k), recursive stack space
class Solution5:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        return self.divide(lists, 0, len(lists) - 1)
    
    # Divide linked lists
    def divide(self, lists: List[Optional[ListNode]], left: int, right: int) -> Optional[ListNode]:
        if left == right: # Only one linked list
            return lists[left]
        mid = (left + right) // 2
        # Split into two halves
        l1 = self.divide(lists, left, mid) # Recursively process left half
        l2 = self.divide(lists, mid + 1, right) # Recursively process right half
        # Merge two halves
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