# 也不是很难嘛！


# 量化：为了减少内存占用，提高计算效率，将浮点数量化为整数
# 例子：int(W_float * 2^8) 将一个小于 1 的浮点数转换为 int8

# 一组 [N,H] 的模型权重，N 表示网络层数，H 表示每层神经元个数
# 现将网络权重进行量化，要求每一层的量化比特 Q_i 一致，不同层之间可以不同
# 量化规则: W_q = int(W_float * 2^Q_i)
# 误差衡量： e = |W_float - W_q / 2^Q_i|
# 要求： sum(Q_i) <= Q_max
# 最小化总误差，给出最优的 Q_i 分配方案
# Q_i = {2, 4, 8}

# 本质上是一个背包问题的变种，使用动态规划求解
# dp[i][j] 表示前 i 层网络，使用了 j 比特时的最小误差

# 读入数据
N, H, Q_max = map(int, input().split())
# 读入网络权重， N 行 H 列
weights = [list(map(float, input().split())) for _ in range(N)]

dp = [[float('inf')] * (Q_max + 1) for _ in range(N + 1)]
# 状态转移方程
# dp[i][j] = min(dp[i-1][j - Q_k] + error_i(Q_k)) for Q_k in {2,4,8} if j >= Q_k
# 初始化
dp[0][0] = 0
quantization_bits = [2, 4, 8]
# 预计算每层在不同量化比特下的误差
errors = [[0] * len(quantization_bits) for _ in range(N)]
for i in range(N):
    for k, Q_k in enumerate(quantization_bits):
        error = 0
        for w in weights[i]:
            W_q = int(w * (1 << Q_k))
            error += abs(w - W_q / (1 << Q_k))
        errors[i][k] = error

# 动态规划填表
for i in range(1, N + 1):
    for j in range(Q_max + 1):
        for k, Q_k in enumerate(quantization_bits):
            if j >= Q_k:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - Q_k] + errors[i - 1][k])

# 输出最小误差（x 100 后取整）
print(int(dp[N][Q_max] * 100))

