# 二叉树的直径：任意两个节点之间的最长路径长度
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # 递归：左右子树最大深度之和
        diameter = 0 # 需要作为全局变量来记录最大直径

        def depth(node: Optional[TreeNode]) -> int:
            nonlocal diameter
            if not node:
                return 0
            
            left_depth = depth(node.left)
            right_depth = depth(node.right)

            # 更新直径
            diameter = max(diameter, left_depth + right_depth)

            # 返回当前节点的深度
            return max(left_depth, right_depth) + 1
        
        # 在查找根节点深度的过程中更新 dimaeter
        depth(root)
        return diameter
