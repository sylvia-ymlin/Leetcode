# 给一组数，判断是否是某个 BST（二叉搜索树）的前序遍历结果 -- 如果是，返回 1，否则返回 0
# 前序遍历：根节点 -> 左子树 -> 右子树
# 约束条件：
# - 左子树所有值 < 根节点值
# - 右子树所有值 > 根节点值
# 即，BTS 的前序遍历有一个单调下界：一旦你进入某个节点的右子树，后续节点的值都必须大于该节点值
# 即，你可以一路向左变小，但是一旦向右变大，就不能再变小了 --> 所以需要栈辅助判断
# 
# 第二个任务：找到这棵树最左叶子节点的值和最右叶子节点的值 
# 如果找到的叶子节点是根节点，说明缺少左子树或右子树，对应位置输出 0


# 核心思路
# 一个栈：模拟从根节点走到当前节点的路径
# 一个 lower_bound：表示当前节点的最小允许值，初始值为 -1，因为题目说明全是正整数
# 算法流程：
# 1. 第一个数是根节点，入栈
# 2. 从左到右遍历节点 x
# -- 如果 x < lower_bound，说明 x 不符合 BST 规则，返回 0
# -- 如果 x > stack[-1], 说明 x 在栈顶节点的右子树上
#    - 不断弹出栈顶节点，直到栈顶节点值大于 x
#    - 每弹出一个节点，就更新 lower_bound 为该节点值
# -- 将 x 入栈
# 3. 遍历结束，说明是合法的 BST 前序遍历，返回 1

# 要找到最左叶子节点和最右叶子节点，可以显示的构建这棵树，然后从根节点出发不断向左或向右走即可


# 构建树
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

pre_order = list(map(int, input().split(" ")))

root = TreeNode(pre_order[0])

stack = [root] # 记录当前路径
low_bound = -1 # 最小值约束节点
flag = True
for i in range(1, len(pre_order)):
    currentNode = TreeNode(pre_order[i])
    # 先判断是否合法 BST 前序遍历
    if currentNode.val < low_bound: # 小于最小值约束，直接退出
        flag = False
        break

    # 递减序列，插入左子节点
    if stack and currentNode.val < stack[-1].val:
        # 当前节点是栈顶节点的左子节点，直接插入
        stack[-1].left = currentNode
        stack.append(currentNode)
        continue

    # 栈空，或当前节点值大于栈顶节点值，说明在右子树上
    # 需要弹出栈中所有小于当前节点值的节点，找到当前节点的父节点
    while stack and currentNode.val > stack[-1].val: # 弹出栈中所有小于当前节点值的节点，最后一个弹出的节点就是当前节点的父节点
        parentNode = stack.pop()
        low_bound = parentNode.val # 更新最小值约束为弹出的节点值
    
    # 挂载右子节点；一开始 stack 非空，parentNode 一定有值
    parentNode.right = currentNode 
    # 当前节点入栈
    stack.append(currentNode)

# 是合法的 BST 前序遍历，构建树
if flag:
    leftNode = root
    # 找最左叶子节点，左右子节点都为空
    while leftNode.left is not None or leftNode.right is not None:
        if leftNode.left is not None: # 优先往左走
            leftNode = leftNode.left
        else: # 往右走
            leftNode = leftNode.right
    
    rightNode = root
    while rightNode.right is not None or rightNode.left is not None:
        if rightNode.right is not None:
            rightNode = rightNode.right
        else:
            rightNode = rightNode.left
    
    res = 1
    left_val = leftNode.val if leftNode != root else 0
    right_val = rightNode.val if rightNode != root else 0
    print(' '.join([str(res), str(left_val), str(right_val)]))
    