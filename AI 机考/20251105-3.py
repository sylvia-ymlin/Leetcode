# 多目标推荐排序模型优化
# 采用线性回归方式完成多目标推荐排序模型的优化

# input 
# 特征值集合
features = input().strip().split(';')
# 特征值维度 d x L
x = [list(map(float, feat.split(','))) for feat in features]
n = len(x) # 样本数
d = len(x[0])  # 特征维度

# 目标值集合
targets = input().strip().split(';')
y = [list(map(float, targ.split(','))) for targ in targets] # n x L

iter = int(input().strip())
alpha = float(input().strip())
beta = float(input().strip())

def total_loss(y_true, y_pred, beta):
    n = len(y_true)
    loss = 0.0
    for i in range(n):
        loss += (y_pred[i][0] - y_true[i][0]) ** 2
        loss += beta * (y_pred[i][1] - y_true[i][1]) ** 2
    return loss / n

# gradient = 2 * (y_pred - y_true) / n

# 初始化权重 和 偏置
w = [0.0] * d # 共享权重
b = [0.0, 0.0]  # 特定偏置

for _ in range(iter):
    y_pred = []
    for i in range(n):
        s = sum(w[j] * x[i][j] for j in range(d))
        y_pred.append([s + b[0], s + b[1]])

    loss = total_loss(y, y_pred, beta)

    dw = [0.0] * d
    db = [0.0, 0.0]

    for i in range(d):
        g0 = sum((y_pred[j][0] - y[j][0]) * x[j][i] for j in range(n))
        g1 = sum((y_pred[j][1] - y[j][1]) * x[j][i] for j in range(n))
        dw[i] = 2 * (g0 + beta * g1) / n

    db[0] = 2 * sum(y_pred[j][0] - y[j][0] for j in range(n)) / n
    db[1] = 2 * beta * sum(y_pred[j][1] - y[j][1] for j in range(n)) / n

    for j in range(d):
        w[j] -= alpha * dw[j]
    for k in range(2):
        b[k] -= alpha * db[k]

print(loss * 1e10)