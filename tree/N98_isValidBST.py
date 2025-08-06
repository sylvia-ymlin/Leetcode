# 验证二叉搜索树，左子树结点严格小于根结点，右子树结点严格大于根结点
# 中序遍历，元素值是否递增

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def inorder(node: Optional[TreeNode]) -> bool:
            if not node:
                return True
            
            # 先递归左子树
            if not inorder(node.left):
                return False
                
            # 检查当前节点值是否大于前一个值
            if node.val <= self.prev:
                return False
            self.prev = node.val  # 更新前一个值
            
            # 最后递归右子树
            return inorder(node.right)
        
        self.prev = float('-inf')  # 用实例变量保存前一个值
        return inorder(root)
