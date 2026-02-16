# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def __init__(self):
        self.maxSum = float('-inf')  # Initialize max path sum to negative infinity

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Find max path sum rooted at each node
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            # Recursively calculate max path sum of left and right subtrees
            # Only non-negative can contribute to path sum
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            # Max path sum of current node
            current_sum = node.val + left + right

            # Update global max path sum
            self.maxSum = max(self.maxSum, current_sum)

            # Return max contribution of current node: forming path, can only be unidirectional at this node
            return node.val + max(left, right)
        
        dfs(root)
        return self.maxSum