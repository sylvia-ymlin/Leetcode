# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        核心思想：
        1. 如果当前节点是p或q，返回当前节点
        2. 分别在左右子树中寻找p和q
        3. 如果p和q分别在左右子树中，当前节点就是LCA
        4. 否则LCA在包含p和q的那个子树中
        """
        
        # 递归终止条件
        if not root:
            return None
        if root == p or root == q:
            return root
        
        # 在左子树中寻找p和q
        left_result = self.lowestCommonAncestor(root.left, p, q)
        # 在右子树中寻找p和q  
        right_result = self.lowestCommonAncestor(root.right, p, q)
        
        # 情况分析：
        if left_result and right_result:
            # p和q分别在左右子树中，当前节点是LCA
            return root
        elif left_result:
            # p和q都在左子树中，LCA在左子树
            return left_result
        elif right_result:
            # p和q都在右子树中，LCA在右子树
            return right_result
        else:
            # 当前子树中没有p和q
            return None 

# 时间复杂度：O(N)，N为树的节点数，最坏情况下需要遍历所有节点
# 空间复杂度：O(H)，H为树的高度，递归调用栈的深度 



