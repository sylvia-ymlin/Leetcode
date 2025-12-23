# 深拷贝链表，要求创建新的结点
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

from typing import Optional
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # 难点是判断节点是否已经存在
        # use a dict to store the relation between the old list and the new list
        mp = {}
        cur = head
        # 复制节点，建立映射
        while cur:
            mp[cur] = Node(cur.val)
            cur = cur.next

        # 链接节点
        cur = head
        while cur:
            mp[cur].next = mp.get(cur.next) # return null if don't exist
            mp[cur].random = mp.get(cur.random)
            cur = cur.next
        

        return mp.get(head)

# 时间复杂度: 两轮遍历 O(N)
# 空间复杂度：使用字典存储映射关系 O(N)

# 优化空间复杂度，拼接 + 拆分
# 三轮遍历链表

class Solution2:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return

        cur = head

        # 先复制结点, 并构建拼接链表
        # old -> new -> old -> new -> ... -> old -> new -> null
        # then we can find the corresponding node use old.next
        while cur:
            temp = Node(cur.val);
            temp.next = cur.next
            cur.next = temp
            cur = temp.next
        
        # 构建新节点的 random 指向
        cur = head
        while cur:
            if cur.random:
                # cur.next = new
                cur.next.random = cur.random.next
            # next old node
            cur = cur.next.next
        
        # 拆分链表
        cur = res = head.next
        pre = head

        while cur.next:
            pre.next = pre.next.next
            cur.next = cur.next.next

            pre = pre.next
            cur = cur.next
        
        pre.next = None # 处理原链表尾节点

        return res
