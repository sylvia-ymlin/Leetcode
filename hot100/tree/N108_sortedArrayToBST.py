# Convert sorted array to balanced binary search tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Simplest: Binary recursion, guarantees balance
        # Empty array, return
        if not nums:
            return None

        # Middle node as root node
        mid = len(nums) // 2
        root = TreeNode(nums[mid])

        # Left and right subtree recursion
        root.left = self.sortedArrayToBST(nums[:mid])  # Left part
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root