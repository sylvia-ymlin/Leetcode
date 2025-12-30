import sys
from ast import literal_eval
from collections import deque

def max_pruned_subtree(arr): # 数组表示的完全二叉树

    n = len(arr) # 节点数
    if n == 0:
        return [] # 空树直接返回空列表

    # 标记每个位置是否为真实结点（非 None） 
    valid = [x is not None for x in arr] # true or false

    # dp[i]：以 i 为根，允许裁掉贡献不为正的子树后，能得到的最大子树和
    dp = [0] * n # 初始化 dp 数组，存储每个节点的最大子树和

    best_sum = None  # 全局最大值
    best_root = -1   # 对应的根下标

    # 自底向上 DP
    for i in range(n - 1, -1, -1): # 从最后一个节点到根节点
        if not valid[i]: # 非真实结点，值为 0
            dp[i] = 0
            continue
        # 计算左右子树贡献
        left = 2 * i + 1
        right = 2 * i + 2

        left_dp = dp[left] if left < n and valid[left] else 0
        right_dp = dp[right] if right < n and valid[right] else 0

        # 允许裁掉贡献不为正的子树
        cur = arr[i]
        if left_dp > 0:
            cur += left_dp
        if right_dp > 0:
            cur += right_dp

        dp[i] = cur

        # 更新全局最大值和对应根节点
        if best_sum is None or cur > best_sum:
            best_sum = cur
            best_root = i

    # 表示只有 None 节点
    if best_root == -1: 
        return []

    # BFS 构造被裁剪后的最大子树（完全二叉树形式），best_root 对应的是子树根节点在原数组中的下标
    # 计算子树节点数
    
    res = []
    q = deque()
    # 队列元素：(原数组下标, 新树下标)
    q.append((best_root, 0))

    while q:
        oi, ni = q.popleft() # original index, new index

        # 插入的都是有效节点，有效节点之前全部为 None
        while len(res) <= ni:
            res.append(None)
        
        # 插入当前节点值
        res[ni] = arr[oi]
        # 左子节点
        left = 2 * oi + 1
        # 右子节点
        right = 2 * oi + 2
        # 入队左子节点
        if left < n and valid[left] and dp[left] > 0: # 只有贡献大于 0 的子树才入队
            q.append((left, 2 * ni + 1))
        # 入队右子节点
        if right < n and valid[right] and dp[right] > 0:
            q.append((right, 2 * ni + 2))

    # # 去掉末尾多余的 None -> 不会有 None 节点在最后面的情况吧
    # while res and res[-1] is None:
    #     res.pop()

    return res


def main():
    s = sys.stdin.readline().strip()
    if not s:
        return
    s = s.replace('null', 'None')
    arr = literal_eval(s)  # 得到包含 int 和 None 的列表

    ans = max_pruned_subtree(arr)

    # 输出格式：[1,-1,null,2,...]
    out = '[' + ','.join('null' if x is None else str(x) for x in ans) + ']'
    print(out)


if __name__ == "__main__":
    main()
