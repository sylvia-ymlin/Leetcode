# Elements visible from the right side
# Level order traversal, output the rightmost element of each level
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional
import collections
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        
        queue = collections.deque([root])
        while queue:
            level = []
            n = len(queue)  # Number of nodes at current level
            for _ in range(n):
                node = queue.popleft()
                level.append(node.val)
                # Add children nodes to queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # Take the last element of current level as right side visible element
            res.append(level[-1])

        return res