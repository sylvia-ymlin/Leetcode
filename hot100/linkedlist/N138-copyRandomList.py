# Deep copy a linked list, requiring creation of new nodes
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

from typing import Optional
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # The difficulty is to judge whether the node already exists
        # use a dict to store the relation between the old list and the new list
        mp = {}
        cur = head
        # Copy nodes, build mapping
        while cur:
            mp[cur] = Node(cur.val)
            cur = cur.next

        # Link nodes
        cur = head
        while cur:
            mp[cur].next = mp.get(cur.next) # return null if don't exist
            mp[cur].random = mp.get(cur.random)
            cur = cur.next
        

        return mp.get(head)

# Time Complexity: Two traversals O(N)
# Space Complexity: Use dictionary to store mapping O(N)

# Optimize Space Complexity, splicing + splitting
# Three traversals of the linked list

class Solution2:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return

        cur = head

        # First copy nodes, and build spliced linked list
        # old -> new -> old -> new -> ... -> old -> new -> null
        # then we can find the corresponding node use old.next
        while cur:
            temp = Node(cur.val);
            temp.next = cur.next
            cur.next = temp
            cur = temp.next
        
        # Build random pointers for new nodes
        cur = head
        while cur:
            if cur.random:
                # cur.next = new
                cur.next.random = cur.random.next
            # next old node
            cur = cur.next.next
        
        # Split linked list
        cur = res = head.next
        pre = head

        while cur.next:
            pre.next = pre.next.next
            cur.next = cur.next.next

            pre = pre.next
            cur = cur.next
        
        pre.next = None # Handle the tail node of the original linked list

        return res
