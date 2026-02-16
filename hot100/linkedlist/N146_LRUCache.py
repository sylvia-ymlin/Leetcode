# Maintain cached key-value pairs: Hash Map and Doubly Linked List
# Hash Map location: cache = {}
# Find node quickly via key
# Doubly Linked List maintains node, move current operation node to head, delete tail node when cache is full

class LRUCache:

    def __init__(self, capacity: int):
        # Initialize capacity and cache
        self.capacity = capacity
        self.cache = {}
        # Maintain cached key-value pairs: Hash Map and Doubly Linked List
        # Hash Map used for location, Doubly Linked List stores key-value pairs
        # Dummy head and dummy tail, maintain doubly linked list
        self.head = DLinkedNode()  # Dummy head
        self.tail = DLinkedNode()  # Dummy tail
        self.head.next = self.tail # Initialize
        self.tail.prev = self.head # Initialize

        self.size = 0 # Current cache size


    def get(self, key: int) -> int:
        # If key does not exist, return -1
        if key not in self.cache:
            return -1
        # If exists, recently used, move to head
        node = self.cache[key]
        self.move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            # Does not exist, create new node
            new_node = DLinkedNode(key, value)
            # Add to hash map
            self.cache[key] = new_node
            # Add to doubly linked list head
            self.add_to_head(new_node)
            self.size += 1

            # If exceeds capacity, delete tail node -> so-called LRU is cache deletion strategy
            if self.size > self.capacity:
                # Delete tail node
                tail_node = self.remove_tail()
                # Delete from hash map
                del self.cache[tail_node.key]
                self.size -= 1
        else:
            # If exists, update value, and move to head
            node = self.cache[key]
            node.value = value
            self.move_to_head(node)
            
    def move_to_head(self, node: 'DLinkedNode'):
        # Delete node from linked list
        self.remove_node(node)
        # Add to head
        self.add_to_head(node)
        
    def add_to_head(self, node: 'DLinkedNode'):
        # Add to head
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove_tail(self) -> 'DLinkedNode':
        # Delete tail node
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