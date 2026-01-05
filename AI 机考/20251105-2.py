# 多目标推荐排序模型优化
# 采用线性回归方式完成多目标推荐排序模型的优化
# 共享特征权重，保留任务特定偏置项
# 使用联合损失函数： loss = MSE_ctr + alpha * MSE_cvr
# 权重和偏置都从 0 开始

# 返回最终的 loss 值，放大 1e10 倍并四舍五入取整输出

# 这道题目的样例有问题！

def parse_matrix(line: str):
    # parse "1,2; 3,4" to [[1,2],[3,4]]
    rows = line.strip().split(';')
    matrix = []
    for row in rows:
        matrix.append([float(x) for x in row.split(',')])
    return matrix

def train_and_loss(X, y, iters, lr, alpha):
    # 对于特征矩阵 X
    # n = 样本数
    # d = 特征维度
    n = len(X)
    d = len(X[0])

    # 初始化： weight 大小和特征维度一致
    weights = [0.0] * d
    # ctr 和 cvr 的偏置项
    b_ctr = 0.0 
    b_cvr = 0.0

    for _ in range(iters): # 迭代
        # 1. 计算当前预测值和误差
        e_ctr = []
        e_cvr = []
        for i in range(n): # 对于每个样本
            # 求和，特征权重 x 特征值
            shared_sum = sum(weights[j] * X[i][j] for j in range(d))
            e_ctr.append(shared_sum + b_ctr - y[i][0]) # 预测值 - 真实值
            e_cvr.append(shared_sum + b_cvr - y[i][1])

        # 2. 计算梯度
        # 梯度形状和变量一致
        # e = sum((y_pred - y_true)^2)/n
        # de/dw = 2/n * sum((y_pred - y_true) * x_i)
        # de/dw = 2/n * sum(e_i * x_i)
        grad_w = [0.0] * d
        for j in range(d):
            sum_w = 0.0
            for i in range(n):
                sum_w += (e_ctr[i] * X[i][j] + alpha * e_cvr[i] * X[i][j])
            # 求和之后再乘以 2/n
            grad_w[j] = (2.0 / n) * sum_w
        
        # 偏置项的梯度，2/n * sum(e_i) * 1
        grad_b_ctr = (2.0 / n) * sum(e_ctr)
        # --- 加上 alpha ---
        grad_b_cvr = alpha * (2.0 / n) * sum(e_cvr) 

        # 3. 更新参数
        for j in range(d): # 更新权重
            weights[j] -= lr * grad_w[j]
        b_ctr -= lr * grad_b_ctr
        b_cvr -= lr * grad_b_cvr
    
    # 最终 Loss 计算
    final_mse_ctr = 0.0
    final_mse_cvr = 0.0
    for i in range(n):
        shared_sum = sum(weights[j] * X[i][j] for j in range(d))
        final_mse_ctr += (shared_sum + b_ctr - y[i][0]) ** 2
        final_mse_cvr += (shared_sum + b_cvr - y[i][1]) ** 2
    
    total_loss = (final_mse_ctr / n) + alpha * (final_mse_cvr / n)
    return total_loss


def main():
    # 读入 X
    X_line = input()
    X = parse_matrix(X_line)
    # 读入 y
    y_line = input()
    y = parse_matrix(y_line)
    # 读入迭代次数，学习率，alpha
    iters = int(input())
    lr = float(input())
    alpha = float(input())

    loss = train_and_loss(X, y, iters, lr, alpha)
    print(round(loss * 1e10))

if __name__ == "__main__":
    main()