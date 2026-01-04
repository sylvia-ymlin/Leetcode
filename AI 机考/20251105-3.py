import sys
import math
from decimal import Decimal, ROUND_HALF_UP


# 计算给定 thetas 下的 U 序列
# thetas: 角标数组
# r: 半径
# 空间维度 k
# 对 1/4 圆还可以折半
def build_U_from_thetas(thetas, r, k):

    U = [r * math.sin(t) for t in thetas]
    if k % 2 == 1:  # 奇数维度，中间还要加一个
        U.append(r / math.sqrt(2.0))
    # 计算条带宽度
    U += [r * math.cos(t) for t in reversed(thetas)]
    return [0.0] + U + [r]


def total_area(thetas, r, k):
    U_full = build_U_from_thetas(thetas, r, k)
    K = len(U_full) - 2  # because U_full = [0] + U + [r]
    s = 0.0
    # i in [1, K+1]
    for i in range(1, K + 2):
        dy = U_full[i] - U_full[i - 1]
        x_cap = U_full[K - i + 2]
        s += dy * x_cap
    return 4.0 * s # 折半再折半


def golden_section_minimize(f, lo, hi, max_it=120, tol=1e-13):
    golden = (math.sqrt(5.0) - 1.0) / 2.0
    a, b = lo, hi
    c = b - golden * (b - a)
    d = a + golden * (b - a)
    fc, fd = f(c), f(d)
    it = 0

    while (b - a) > tol and it < max_it:
        if fc > fd:
            a, c, fc = c, d, fd
            d = a + golden * (b - a)
            fd = f(d)
        else:
            b, d, fd = d, c, fc
            c = b - golden * (b - a)
            fc = f(c)
        it += 1

    return (a + b) / 2.0


def optimize_thetas(M):
    r = 0.5
    k = (M - 1) // 2
    p = k // 2

    if p == 0:
        return total_area([], r, k)

    thetas = [ (i + 1) * (math.pi / 4.0) / (p + 1) for i in range(p) ]

    # outer coordinate-descent rounds
    for _ in range(30):
        changed = False
        for i in range(p):
            lo = thetas[i - 1] + 1e-12 if i > 0 else 1e-12
            hi = thetas[i + 1] - 1e-12 if i < p - 1 else (math.pi / 4.0) - 1e-12

            def f(x):
                tmp = list(thetas)
                tmp[i] = x
                return total_area(tmp, r, k)

            new_theta = golden_section_minimize(f, lo, hi, max_it=120, tol=1e-13)
            if abs(new_theta - thetas[i]) > 1e-15:
                thetas[i] = new_theta
                changed = True

        if not changed:
            break

    return total_area(thetas, r, k)


def main():
    M = int(sys.stdin.readline().strip())
    ans = optimize_thetas(M)
    print(f"{ans:.4f}")

if __name__ == "__main__":
    main()
