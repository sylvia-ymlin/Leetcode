# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 按先序遍历的顺序展开
        preorderList = list()

        # 先序遍历，将所有节点按先序顺序存入列表
        def preorder(node: Optional[TreeNode]) -> None:
            if node:
                preorderList.append(node)
                preorder(node.left)
                preorder(node.right)
        
        preorder(root)
        # 连接所有节点
        for i in range(len(preorderList) - 1):
            preorderList[i].left = None
            preorderList[i].right = preorderList[i + 1]

# 原地交换，空间复杂度 O(1)
class Solution2:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        cur = root
        while cur:
            # 当前树的左孩子
            temp = cur.left
            # 左子树不为空，右子树接到左子树的最右节点
            while temp and temp.right:
                # 找到左子树最右节点
                temp = temp.right

            # 存在最右节点
            if temp:
                # 右子树接到左子树最右节点
                temp.right = cur.right
                # 左子树变成右子树
                cur.right = cur.left
                # 左子树置空
                cur.left = None
            # 继续处理右子树
            cur = cur.right

# 每一个结点，cur，如果存在左子树，就需要处理
# 1. 找到左子树的最右节点
# 2. 将右子树接到左子树的最右节点
# 3. 将左子树变成右子树
# 4. 左子树置空
# 5. 继续处理右子树
# 时间复杂度 O(n)，空间复杂度 O(1)
# 根节点 -> 左子树 -> 右子树： 保证先序遍历顺序