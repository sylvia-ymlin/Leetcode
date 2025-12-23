# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def __init__(self):
        self.maxSum = float('-inf')  # 初始化最大路径和为负无穷

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # 找到以每个节点为根的最大路径和
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            # 递归计算左子树和右子树的最大路径和
            # 非负才能贡献到路径和
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            # 当前节点的最大路径和
            current_sum = node.val + left + right

            # 更新全局最大路径和 
            self.maxSum = max(self.maxSum, current_sum)

            # 返回当前节点的最大贡献值: 构成路径，在该节点只能单向
            return node.val + max(left, right)
        
        dfs(root)
        return self.maxSum