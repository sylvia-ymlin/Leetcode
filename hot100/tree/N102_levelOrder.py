# 层级遍历
# 需要用到队列
# 根节点入队列
# 队列头出队列，访问节点，所有孩子节点入队列
# until 队列空
# 注意输出要按层

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
        queue = collections.deque([root])  # 使用双端队列作为队列，最优选择
        while queue:
            level = [] # 当前层的节点值列表
            # 当前层的节点数就是队列长度
            n = len(queue) # 在循环中会动态变化，不能直接放到 for 循环中
            for _ in range(n):
                node = queue.popleft() # 队列头出队列
                level.append(node.val) # 访问节点
                # 将子节点入队列
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
        return res