from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Inorder traversal of binary tree, recursion
        def inorder(node: Optional[TreeNode], res: List[int]):
            if not node:
                return
            inorder(node.left, res)
            res.append(node.val)
            inorder(node.right, res)

        result = []
        inorder(root, result)
        return result

# Iterative implementation
class SolutionIterative:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, result = [], []
        current = root

        while current or stack:
            # Traverse to the leftmost
            while current:
                stack.append(current)
                current = current.left

            # Pop and visit node, parent pushed first, so it is inorder
            current = stack.pop()
            result.append(current.val)
            # Turn to right subtree
            current = current.right

        return result