# 多目标推荐排序模型优化
# 采用线性回归方式完成多目标推荐排序模型的优化

# 这道题目的样例有问题！

from decimal import Decimal, ROUND_HALF_UP

def parse_matrix(line: str):
    # parse "1,2; 3,4" to [[1,2],[3,4]]
    rows = line.strip().split(';')
    matrix = []
    for row in rows:
        matrix.append([float(x) for x in row.split(',')])
    return matrix

def train_and_loss(X, y, iters, lr, alpha):
    n = len(X)
    d = len(X[0])
    # 初始化
    weights = [0.0] * d
    b_ctr = 0.0
    b_cvr = 0.0

    for _ in range(iters):
        # 1. 计算当前预测值和误差
        e_ctr = []
        e_cvr = []
        for i in range(n):
            shared_sum = sum(weights[j] * X[i][j] for j in range(d))
            e_ctr.append(shared_sum + b_ctr - y[i][0])
            e_cvr.append(shared_sum + b_cvr - y[i][1])

        # 2. 计算梯度 (注意 alpha 的应用)
        grad_w = [0.0] * d
        for j in range(d):
            # w 受到两个任务的共同影响
            sum_w = 0.0
            for i in range(n):
                sum_w += (e_ctr[i] * X[i][j] + alpha * e_cvr[i] * X[i][j])
            grad_w[j] = (2.0 / n) * sum_w
        
        grad_b_ctr = (2.0 / n) * sum(e_ctr)
        # --- 修正点：加上 alpha ---
        grad_b_cvr = alpha * (2.0 / n) * sum(e_cvr) 

        # 3. 更新参数
        for j in range(d):
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