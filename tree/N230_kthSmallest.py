# 二叉搜索树中第k小元素：中序遍历 -> 升序 -> 第 k 个元素
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # 要在所有递归栈中共享变量，需要用类属性或实例属性
        self.count = 0
        self.result = -1

        def inorder(node: Optional[TreeNode]):
            if not node:
                return
            inorder(node.left)
            self.count += 1
            if self.count == k:
                self.result = node.val
                return
            inorder(node.right)

        inorder(root)
        return self.result
