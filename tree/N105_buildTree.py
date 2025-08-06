# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List, Optional
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 从先序和中序中确定根节点
        if not preorder or not inorder:
            return None
        
        # 先序遍历的第一个节点是根节点
        root_val = preorder[0]
        root = TreeNode(root_val)

        # 在中序遍历中找到根节点的位置
        root_index = inorder.index(root_val)

        # 递归创建 左子树和右子树
        root.left = self.buildTree(preorder[1:1 + root_index], inorder[:root_index])
        root.right = self.buildTree(preorder[1 + root_index:], inorder[root_index + 1:])

        return root

# 时间复杂度 O(n)，空间复杂度 O(n)