import sys
import math
from decimal import Decimal, ROUND_HALF_UP


# 计算给定 thetas 下的 U 序列
# thetas: 角标数组
# r: 半径
# 空间维度 k
# 对 1/4 圆还可以折半

def build_U_from_thetas(thetas, r, k):
    sorted_thetas = sorted(thetas) # 确保角度有序
    # 生成 [0, pi/4] 上的 U 序列
    U = [r * math.sin(t) for t in thetas]
    if k % 2 == 1:  # 奇数维度，还要增加 r / sqrt(2)
        U.append(r / math.sqrt(2.0))
    # 对称部分，就是 u 序列的反转， cos 部分
    U += [r * math.cos(t) for t in reversed(thetas)]
    return [0.0] + U + [r] # 添加边界


def objective(thetas, r, k):
    # 生成条带
    U_full = build_U_from_thetas(thetas, r, k)
    s = 0.0 # 1/4 面积
    # i in [1, K+1] # 矩形上边界
    for i in range(1, k + 2):
        # x 是 angle[i-1] 对应的 x 坐标
        # i - 1 + x = k + 1 -> x = k - i + 2
        dy = U_full[i] - U_full[i - 1]
        x_cap = U_full[k - i + 2]
        s += dy * x_cap
    return 4.0 * s # 乘以 4，得到完整面积

# 梯度下降优化
from scipy.optimize import minimize

def optimize_thetas(M):

    if M == 1:
        return  1 #整个像素区域都覆盖
    r = 0.5
    k = (M - 1) // 2
    p = k // 2

    # 初始化 thetas
    thetas = [ (i + 1) * (math.pi / 4.0) / (p + 1) for i in range(p) ]

    # 梯度下降
    # 在 optimize_thetas 中提高 Scipy 精度
    res = minimize(lambda th: objective(th, r, k), thetas, method='L-BFGS-B',
                bounds=[(0.0, math.pi / 4.0)] * p,
                options={'ftol': 1e-16, 'gtol': 1e-16, 'maxiter': 20000})
    # 参数含义
    # minimize 是最小化函数，本身 objective 就是要最小化面积
    # thetas 是初始点
    # method 是优化方法
    # bounds 是每个参数的取值范围
    # options 是优化选项： ftol 是函数值收敛阈值，gtol 是梯度收敛阈值，maxiter 是最大迭代次数
    # 返回的 res 包含优化结果
    return objective(res.x, r, k)

# 如果手动实现梯度下降，可以参考以下代码
def gradient_descent(thetas, r, k, learning_rate=0.01, max_iter=10000, tol=1e-8):
    p = len(thetas)
    for iteration in range(max_iter):
        grad = [0.0] * p
        # 计算梯度: 中心差分法
        for i in range(p):
            delta = 1e-8 # 微小变化
            thetas_plus = thetas[:] # 复制一份
            thetas_minus = thetas[:] # 复制一份
            thetas_plus[i] += delta # 微小增加 
            thetas_minus[i] -= delta # 微小减少
            f_plus = objective(thetas_plus, r, k) # 计算目标函数值
            f_minus = objective(thetas_minus, r, k) # 计算目标函数值
            grad[i] = (f_plus - f_minus) / (2 * delta) # 中心差分法计算梯度
        # 更新参数
        max_change = 0.0 # 记录所有参数重的最大变化
        for i in range(p):
            change = learning_rate * grad[i]
            thetas[i] -= change # 梯度下降更新
            max_change = max(max_change, abs(change)) # 记录最大变化
        # 检查收敛
        if max_change < tol:
            break
    return objective(thetas, r, k)
    


def main():
    M = int(sys.stdin.readline().strip())
    # ans = optimize_thetas(M)
    # 手动梯度下降
    if M == 1:
        ans = 1.0
    else:
        r = 0.5
        k = (M - 1) // 2
        p = k // 2
        thetas = [ (i + 1) * (math.pi / 4.0) / (p + 1) for i in range(p) ]
        ans = gradient_descent(thetas, r, k, learning_rate=0.01, max_iter=20000, tol=1e-16)
    out = Decimal(str(ans)).quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP)
    print(out)

if __name__ == "__main__":
    main()
