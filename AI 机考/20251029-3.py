import math

# sigmoid 函数
def sigmoid(z): # 数值稳定的实现
    if z >= 0:
        ez = math.exp(-z)
        return 1 / (1.0 + ez)
    else:
        ez = math.exp(z)
        return ez / (1.0 + ez)


# 计算损失和梯度
def compute_loss_and_gradient(X, y, w, b, lam):
    n = len(y) # 样本数量
    d = len(w) # 特征数量

    eps = 1e-15 # 防止 log(0)

    loss = 0.0
    grad_w = [0.0] * d
    grad_b = 0.0

    # 计算交叉熵和梯度
    for i in range(n):
        z = b 
        for j in range(d):
            z += w[j] * X[i][j]
        p = sigmoid(z) # 预测概率
        yi = y[i]
        # 交叉熵
        loss += - (yi * math.log(p + eps) + (1 - yi) * math.log(1 - p + eps))
        # 梯度
        # dy_dz = hat_y - y
        diff = p - yi
        for j in range(d):
            grad_w[j] += diff * X[i][j] # 对 w 的梯度
        grad_b += diff # 对 b 的梯度
    
    # 平均
    loss /= n
    for j in range(d):
        grad_w[j] /= n
    grad_b /= n

    # 添加正则约束，在计算完损失和梯度后
    l2 = 0.0
    for j in range(d):
        l2 += w[j] * w[j]
        grad_w[j] += lam / n * w[j] # L2 正则化梯度
    loss += (lam / (2 * n)) * l2 # L2 正则化损失
    return loss, grad_w, grad_b

def train(X, y, max_iters, alpha, lam, tol):
    n = len(y)
    d = len(X[0])

    # 初始化参数
    w = [0.0] * d
    b = 0.0

    # 先计算一次loss
    loss, _, _ = compute_loss_and_gradient(X, y, w, b, lam)
    iter = 0
    while iter < max_iters and loss >tol:
        loss, grad_w, grad_b = compute_loss_and_gradient(X, y, w, b, lam)
        # 更新参数
        for j in range(d):
            w[j] -= alpha * grad_w[j]
        b -= alpha * grad_b

        iter += 1
    return w, b

def predict(X, w, b):
    d = len(w)
    z = b
    for j in range(d):
        z += w[j] * X[j]
    p = sigmoid(z)
    return 1 if p >= 0.5 else 0, p

# 输入处理
n, max_iters, alpha, lam, tol = input().strip().split()
n = int(n)
max_iters = int(max_iters)
alpha = float(alpha)
lam = float(lam)
tol = float(tol)
X = []
y = []
for _ in range(n):
    line = list(map(float, input().strip().split()))
    X.append(line[:-1])
    y.append(int(line[-1]))

test_num = int(input().strip())
tests = []
for _ in range(test_num):
    line = list(map(float, input().strip().split()))
    tests.append(line)

# 训练模型
w, b = train(X, y, max_iters, alpha, lam, tol)
# 预测
for test in tests:
    pred, prob = predict(test, w, b)
    prob = round(prob, 4)
    print(pred, prob)
    # 不追求和答案完全一致，初始化不同，可能会有微小差异

