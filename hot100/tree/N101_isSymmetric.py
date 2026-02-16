class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Recursively check if left and right subtrees are mirrors: check if two trees are equal
        if not root: # Leaf node exit
            return True
        
        def isMirror(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            if not left and not right: # Recursion exit
                return True
            if not left or not right: # Only one subtree exists
                return False
            if left.val != right.val: # Node values are not equal
                return False
            # Recursive check: note the mirror relationship
            return isMirror(left.left, right.right) and isMirror(left.right, right.left)

        return isMirror(root.left, root.right)