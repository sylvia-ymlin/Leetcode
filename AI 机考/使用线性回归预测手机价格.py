# 三个特征，建立线性回归模型，预测手机价格
# 要求使用正规法，即方程求解

# 第一行：样本数量
# 第二行：特征1，特征2，特征3，价格 四个一组
# 第三行：特征1，特征2，特征3，要求预测价格，三个一组代表一例测试数据
# 输出预测价格，四舍五入取整数

# 读入数据
n = int(input())

data = list(map(int, input().split()))

m = int(input()) # 测试数据组数

tests = list(map(int, input().split()))

train_X = []
train_Y = []
for i in range(n):
    x1 = data[4 * i]
    x2 = data[4 * i + 1]
    x3 = data[4 * i + 2]
    y = data[4 * i + 3]
    train_X.append([1, x1, x2, x3])  # 添加偏置项
    train_Y.append(y)

# 构建 normal equation 的矩阵形式
# X^T * X * W = X^T * Y

# 计算 X^T * X
XT_X = [[0] * 4 for _ in range(4)]
for i in range(n):
    for j in range(4):
        for k in range(4):
            XT_X[j][k] += train_X[i][j] * train_X[i][k]

# 计算 X^T * Y
XT_Y = [0] * 4
for i in range(n):
    for j in range(4):
        XT_Y[j] += train_X[i][j] * train_Y[i]

# 求解线性方程组 XT_X * W = XT_Y
# 使用高斯消元法
def gaussian_elimination(A, b):
    n = len(b)
    for i in range(n):
        # 寻找主元
        max_row = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > abs(A[max_row][i]):
                max_row = k
        A[i], A[max_row] = A[max_row], A[i]
        b[i], b[max_row] = b[max_row], b[i]

        # 消元
        for k in range(i + 1, n):
            factor = A[k][i] / A[i][i]
            for j in range(i, n):
                A[k][j] -= factor * A[i][j]
            b[k] -= factor * b[i]

    # 回代
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = b[i]
        for j in range(i + 1, n):
            x[i] -= A[i][j] * x[j]
        x[i] /= A[i][i]
    return x

weights = gaussian_elimination(XT_X, XT_Y)
# 预测测试数据
res = []

for i in range(m):
    x1 = tests[3 * i]
    x2 = tests[3 * i + 1]
    x3 = tests[3 * i + 2]
    y_pred = weights[0] + weights[1] * x1 + weights[2] * x2 + weights[3] * x3
    res.append(str(round(y_pred)))

print(' '.join(res))
