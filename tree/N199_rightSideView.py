# 右侧能看到的元素
# 层级遍历，输出每一层的最右侧元素
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
            n = len(queue)  # 当前层的节点数
            for _ in range(n):
                node = queue.popleft()
                level.append(node.val)
                # 将子节点入队列
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # 取当前层的最后一个元素作为右侧可见元素
            res.append(level[-1])

        return res