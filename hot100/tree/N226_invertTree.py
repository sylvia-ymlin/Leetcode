# Invert binary tree and return root node

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Because of the structural characteristics of trees, almost all tree-related problems are suitable for recursive solutions
        # Invert left subtree, invert right subtree, swap left and right subtrees
        if not root:
            return None
        
        # Invert left and right subtrees
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        
        # Swap left and right subtrees
        root.left, root.right = right, left
        
        return root