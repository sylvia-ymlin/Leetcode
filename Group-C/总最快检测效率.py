# 首选需要理清题意
# 输入：采样品人数，志愿者人数
# 第二行输入：各个采样人效率 N/h
# 输出最快总检测效率

# 采样员效率浮动规则100%
# 没有志愿者时，采样员效率 N - N*0.1*2 -> 0.8 N
# 配备两名志愿者，采样员效率 1.1N
# 配备三名志愿者，采样员效率 1.2N
# 配备四名志愿者，采样员效率 1.3N
# 不再增加，增加无效
def eff(N, k):
    if k == 0:
        return N - 2 * (N // 10)   # 0.8N
    if k <= 4:
        return N + (k - 1) * (N // 10)
    return N + 3 * (N // 10)

# 读入数据
n, m = map(int, input().split())
efficiencies = list(map(int, input().split()))

# dp[i][j] 表示前 i 个采样员，分配 j 名志愿者时的最快总检测效率
dp = [[0] * (m + 1) for _ in range(n + 1)]

# 初始化，没有志愿者时的效率
for i in range(1, n + 1):
    dp[i][0] = dp[i-1][0] + eff(efficiencies[i-1], 0)

# 填充 dp 表格
for i in range(1, n + 1): # 遍历采样员
    for j in range(1, m + 1): # 遍历志愿者数量
        for k in range(0, min(4, j) + 1): # 分配给当前采样员的志愿者数
            dp[i][j] = max(
                dp[i][j], 
                dp[i-1][j-k] + eff(efficiencies[i-1], k))

# 输出结果
print(dp[n][m])