# 维护缓存的键值对：哈希表和双向链表
# 哈希表定位： cache = {}
# 通过 key 快速查找到 node
# 双向链表维护 node，将当前操作节点移动到头部，缓存满后，删除末尾节点

class LRUCache:

    def __init__(self, capacity: int):
        # 初始化容量 和 缓存
        self.capacity = capacity
        self.cache = {}
        # 维护缓存的键值对：哈希表和双向链表
        # 哈希表用于定位，双向链表存储键值对
        # 伪头部和伪尾部，维护双向链表
        self.head = DLinkedNode()  # 伪头部
        self.tail = DLinkedNode()  # 伪尾部
        self.head.next = self.tail # 初始化
        self.tail.prev = self.head # 初始化

        self.size = 0 # 当前缓存大小


    def get(self, key: int) -> int:
        # 如果 key 不存在，返回 -1
        if key not in self.cache:
            return -1
        # 如果存在，最近使用，移动到头部
        node = self.cache[key]
        self.move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            # 不存在，创建新的节点
            new_node = DLinkedNode(key, value)
            # 添加到哈希表
            self.cache[key] = new_node
            # 添加到双向链表头部
            self.add_to_head(new_node)
            self.size += 1

            # 如果超过容量，删除尾部节点 -> 所谓的 LRU 是缓存删除策略
            if self.size > self.capacity:
                # 删除尾部节点
                tail_node = self.remove_tail()
                # 从哈希表中删除
                del self.cache[tail_node.key]
                self.size -= 1
        else:
            # 如果存在，更新值，并移动到头部
            node = self.cache[key]
            node.value = value
            self.move_to_head(node)
            
    def move_to_head(self, node: 'DLinkedNode'):
        # 从链表中删除节点
        self.remove_node(node)
        # 添加到头部
        self.add_to_head(node)
        
    def add_to_head(self, node: 'DLinkedNode'):
        # 添加到头部
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove_tail(self) -> 'DLinkedNode':
        # 删除尾部节点
        tail_node = self.tail.prev
        tail_node.prev.next = self.tail
        self.tail.prev = tail_node.prev
        return tail_node

    def remove_node(self, node: 'DLinkedNode'):
        node.prev.next = node.next
        node.next.prev = node.prev


class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None