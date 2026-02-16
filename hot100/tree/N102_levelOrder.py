# Level order traversal
# Need to use a queue
# Root node enters queue
# Queue head leaves queue, visit node, all children nodes enter queue
# until queue is empty
# Note output should be by level

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List
import collections
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
       
        res = []
        queue = collections.deque([root])  # Use deque as queue, optimal choice
        while queue:
            level = [] # List of node values at current level
            # Number of nodes at current level is queue length
            n = len(queue) # Will change dynamically in loop, cannot be put directly into for loop
            for _ in range(n):
                node = queue.popleft() # Queue head leaves queue
                level.append(node.val) # Visit node
                # Children nodes enter queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
        return res