class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # 递归判断左右子树是否镜像：判断两棵树是否相等
        if not root: #叶子结点出口
            return True
        
        def isMirror(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            if not left and not right: # 递归出口
                return True
            if not left or not right: # 只有一侧子树
                return False
            if left.val != right.val: # 节点值不相等
                return False
            # 递归检查：注意镜像关系
            return isMirror(left.left, right.right) and isMirror(left.right, right.left)

        return isMirror(root.left, root.right)