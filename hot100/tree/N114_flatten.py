# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Flatten in preorder traversal order
        preorderList = list()

        # Preorder traversal, store all nodes in list in preorder
        def preorder(node: Optional[TreeNode]) -> None:
            if node:
                preorderList.append(node)
                preorder(node.left)
                preorder(node.right)
        
        preorder(root)
        # Connect all nodes
        for i in range(len(preorderList) - 1):
            preorderList[i].left = None
            preorderList[i].right = preorderList[i + 1]

# In-place exchange, space complexity O(1)
class Solution2:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        cur = root
        while cur:
            # Left child of current tree
            temp = cur.left
            # If left subtree is not empty, connect right subtree to the rightmost node of left subtree
            while temp and temp.right:
                # Find the rightmost node of left subtree
                temp = temp.right

            # Rightmost node exists
            if temp:
                # Connect right subtree to rightmost node of left subtree
                temp.right = cur.right
                # Left subtree becomes right subtree
                cur.right = cur.left
                # Set left subtree to empty
                cur.left = None
            # Continue processing right subtree
            cur = cur.right

# For each node cur, if left subtree exists, need to process
# 1. Find the rightmost node of the left subtree
# 2. Connect the right subtree to the rightmost node of the left subtree
# 3. Left subtree becomes right subtree
# 4. Set left subtree to empty
# 5. Continue processing right subtree
# Time complexity O(n), Space complexity O(1)
# Root -> Left Subtree -> Right Subtree: Ensure preorder traversal order