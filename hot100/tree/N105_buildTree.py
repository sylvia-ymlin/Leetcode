# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List, Optional
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Determine root node from preorder and inorder
        if not preorder or not inorder:
            return None
        
        # First node of preorder traversal is the root node
        root_val = preorder[0]
        root = TreeNode(root_val)

        # Find position of root node in inorder traversal
        root_index = inorder.index(root_val)

        # Recursively create left subtree and right subtree
        root.left = self.buildTree(preorder[1:1 + root_index], inorder[:root_index])
        root.right = self.buildTree(preorder[1 + root_index:], inorder[root_index + 1:])

        return root

# Time complexity O(n), Space complexity O(n)