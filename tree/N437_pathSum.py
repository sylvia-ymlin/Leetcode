# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import collections
from typing import Optional
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # 路径长度是节点值的和
        # 暴力解，遍历所有路径，统计符合条件的路径数量
        
        # 以某个节点为起点，向下遍历所有路径，统计满足的路径数量
        def rootSum(node: Optional[TreeNode], currentSum: int) -> int:
            if node is None:
                return 0
            
            ret = 0
            if node.val == currentSum:
                ret += 1

            # 递归左子树和右子树, 子树的路径和需要减去当前节点值
            ret += rootSum(node.left, currentSum - node.val)
            ret += rootSum(node.right, currentSum - node.val)
            return ret
        
        if not root:
            return 0
        
        # 从根节点开始，统计所有路径
        return (rootSum(root, targetSum) + 
                self.pathSum(root.left, targetSum) + 
                self.pathSum(root.right, targetSum))

# 前缀和解法，避免重复计算
# 哈希表存放计算过的路径和
class Solution2:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # 每个节点只遍历一次，当前结点值 + 前缀和出现次数
        # 前缀和，存储路径和出现的次数
        prefix = collections.defaultdict(int)
        prefix[0] = 1

        # curr: 从根节点到当前结点前所有节点值的和
        def dfs(node, curr):
            if not node:
                return 0
            
            ret = 0
            curr += node.val # 根节点到当前节点的路径和
            # 满足条件的路径条数
            ret += prefix[curr - targetSum]
            # 更新当前路径和出现的次数
            prefix[curr] += 1
            # 递归遍历左子树和右子树
            ret += dfs(node.left, curr)
            ret += dfs(node.right, curr)
            # 回溯，退出
            prefix[curr] -= 1
            return ret

        return dfs(root, 0)

# DFS遍历完一个分支后，要移除该分支的影响
# 避免影响其他分支的计算
# 这是树形结构中前缀和的经典处理方式
