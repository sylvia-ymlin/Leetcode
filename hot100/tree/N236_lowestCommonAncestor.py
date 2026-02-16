# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Core idea:
        1. If current node is p or q, return current node
        2. Search for p and q in left and right subtrees respectively
        3. If p and q are in left and right subtrees respectively, current node is LCA
        4. Otherwise LCA is in the subtree containing p and q
        """
        
        # Recursion termination condition
        if not root:
            return None
        if root == p or root == q:
            return root
        
        # Search for p and q in left subtree
        left_result = self.lowestCommonAncestor(root.left, p, q)
        # Search for p and q in right subtree
        right_result = self.lowestCommonAncestor(root.right, p, q)
        
        # Case analysis:
        if left_result and right_result:
            # p and q are in left and right subtrees respectively, current node is LCA
            return root
        elif left_result:
            # p and q are both in left subtree, LCA is in left subtree
            return left_result
        elif right_result:
            # p and q are both in right subtree, LCA is in right subtree
            return right_result
        else:
            # p and q are not in current subtree
            return None 

# Time complexity: O(N), where N is the number of nodes in the tree, need to traverse all nodes in worst case
# Space complexity: O(H), where H is the height of the tree, depth of recursion stack 



