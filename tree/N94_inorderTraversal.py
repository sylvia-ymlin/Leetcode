from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 中序遍历二叉树, 递归
        def inorder(node: Optional[TreeNode], res: List[int]):
            if not node:
                return
            inorder(node.left, res)
            res.append(node.val)
            inorder(node.right, res)

        result = []
        inorder(root, result)
        return result

# 非递归实现
class SolutionIterative:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, result = [], []
        current = root

        while current or stack:
            # 先遍历到最左边
            while current:
                stack.append(current)
                current = current.left

            # 出栈并访问节点，parent 先入栈，所以是中序
            current = stack.pop()
            result.append(current.val)
            # 转向右子树
            current = current.right

        return result