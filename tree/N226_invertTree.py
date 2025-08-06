# 翻转二叉树返回根节点

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 因为树的结构特性，几乎所有树相关的问题都适用递归解决
        # 翻转左子树，翻转右子树，交换左右子树
        if not root:
            return None
        
        # 翻转左子树和右子树
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        
        # 交换左右子树
        root.left, root.right = right, left
        
        return root