# Diameter of binary tree: length of longest path between any two nodes
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Recursion: sum of max depths of left and right subtrees
        diameter = 0 # Need to use as global variable to record max diameter

        def depth(node: Optional[TreeNode]) -> int:
            nonlocal diameter
            if not node:
                return 0
            
            left_depth = depth(node.left)
            right_depth = depth(node.right)

            # Update diameter
            diameter = max(diameter, left_depth + right_depth)

            # Return depth of current node
            return max(left_depth, right_depth) + 1
        
        # Update diameter during process of finding root node depth
        depth(root)
        return diameter
