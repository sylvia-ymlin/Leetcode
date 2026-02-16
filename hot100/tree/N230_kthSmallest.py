# Kth smallest element in BST: Inorder traversal -> Ascending order -> Kth element
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # To share variables across all recursion stacks, need to use class attributes or instance attributes
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
