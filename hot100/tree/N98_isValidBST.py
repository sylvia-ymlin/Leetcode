# Validate Binary Search Tree, left subtree nodes strictly less than root node, right subtree nodes strictly greater than root node
# Inorder traversal, whether element values are increasing

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
            
            # Recursively left subtree first
            if not inorder(node.left):
                return False
                
            # Check if current node value is greater than previous value
            if node.val <= self.prev:
                return False
            self.prev = node.val  # Update previous value
            
            # Finally recursively right subtree
            return inorder(node.right)
        
        self.prev = float('-inf')  # Use instance variable to save previous value
        return inorder(root)
