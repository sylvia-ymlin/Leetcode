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
        # Path length is sum of node values
        # Brute force, traverse all paths, count number of paths meeting condition
        
        # Starting from a node, traverse all paths downwards, count number of satisfying paths
        def rootSum(node: Optional[TreeNode], currentSum: int) -> int:
            if node is None:
                return 0
            
            ret = 0
            if node.val == currentSum:
                ret += 1

            # Recursively traverse left and right subtrees, path sum of subtree needs to subtract current node value
            ret += rootSum(node.left, currentSum - node.val)
            ret += rootSum(node.right, currentSum - node.val)
            return ret
        
        if not root:
            return 0
        
        # Start from root node, count all paths
        return (rootSum(root, targetSum) + 
                self.pathSum(root.left, targetSum) + 
                self.pathSum(root.right, targetSum))

# Prefix sum solution, avoid repeated calculation
# Hash table stores calculated path sums
class Solution2:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # Traverse each node only once, current node value + prefix sum occurrence count
        # Prefix sum, stores occurrence count of path sums
        prefix = collections.defaultdict(int)
        prefix[0] = 1

        # curr: sum of all node values from root node to current node
        def dfs(node, curr):
            if not node:
                return 0
            
            ret = 0
            curr += node.val # Path sum from root node to current node
            # Number of paths satisfying condition
            ret += prefix[curr - targetSum]
            # Update occurrence count of current path sum
            prefix[curr] += 1
            # Recursively traverse left and right subtrees
            ret += dfs(node.left, curr)
            ret += dfs(node.right, curr)
            # Backtrack, exit
            prefix[curr] -= 1
            return ret

        return dfs(root, 0)

# After traversing a branch in DFS, remove influence of that branch
# Avoid affecting calculation of other branches
# This is a classic handling method of prefix sum in tree structure
