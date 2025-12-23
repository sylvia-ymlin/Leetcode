# 有序数组转变为平衡二叉搜索树
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # 最简单：二分递归，保证平衡
        # 空数组，return
        if not nums:
            return None

        # 中间节点作为根节点
        mid = len(nums) // 2
        root = TreeNode(nums[mid])

        # 左右子树递归
        root.left = self.sortedArrayToBST(nums[:mid])  # 左半部分
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root