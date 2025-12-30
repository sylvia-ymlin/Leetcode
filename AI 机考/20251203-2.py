# 基于剪枝的神经网络模型压缩
# 给定输入矩阵 x， 权重矩阵 w，剪枝比例 ratio
# 对 W 进行结构化剪枝，使用剪枝后的结果计算模型预测的结果

# X: n x d, n 为样本数，d 为特征数
# W: d x c, c 为类别数
# 计算过程：
# h = X * W
# s = softmax(h)
# 输出类别为 argmax(s)

# 剪枝
# 对 W 按行剪枝，剪枝率 ratio， 剪枝指标 L1 范数 (行向量绝对值之和)

# 剪枝定义
# 1. 按行剪枝：移除不重要的行，保留重要的行
# 2. 物理意义：移除对输出影响较小的特征输入，以压缩模型的输入维度
# 3. 剪枝后
# - w： (d-k) x c, k 为剪枝掉的行数
# - x： n x (d-k)
# 剪枝指标：计算 sum(abs(w[i]))，选择 sum 最小的 ratio% 的行进行剪枝，移除 x 中对应的列

# k = ratio * d 向下取整

n, d, c = map(int, input().strip().split())

X = [list(map(float, input().strip().split())) for _ in range(n)]
W = [list(map(float, input().strip().split())) for _ in range(d)]
ratio = float(input().strip())

k = int(d * ratio)
if k == 0 and ratio > 0:
    k = 1 # 至少剪掉一行

# 计算每行的 L1 范数
l1_norms = [(i, sum(abs(W[i][j]) for j in range(c))) for i in range(d)]
# 按照 L1 范数排序，选择前 k 个进行剪枝
l1_norms.sort(key=lambda x: x[1])

# 不用显示剪枝，只需要跳过被剪掉的行计算
h = [[0.0] * c for _ in range(n)] # x * w
pruned_indices = set(idx for idx, _ in l1_norms[:k])
for i in range(n):
    for j in range(d):
        if j in pruned_indices:
            continue
        for col in range(c):
            h[i][col] += X[i][j] * W[j][col]
            
# 计算 softmax
import math
s = [[0.0] * c for _ in range(n)]
for i in range(n):
    max_h = max(h[i])
    exp_sum = sum(math.exp(h[i][j] - max_h) for j in range(c))
    for j in range(c):
        s[i][j] = math.exp(h[i][j] - max_h) / exp_sum

# 输出类别
labels = []
for i in range(n):
    predicted_class = s[i].index(max(s[i]))
    labels.append(predicted_class)

print(' '.join(map(str, labels)))

