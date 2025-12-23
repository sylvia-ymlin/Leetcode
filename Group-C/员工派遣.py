# 输入
# a b c d
# a: 国家 x 代号
# b: 国家 y 代号
# c: 国家 x 派遣人数
# d: 国家 y 派遣人数

# 编号共用，派遣规则是
# 编号 a 的倍数的不能去 国家 x
# 编号 b 的倍数的不能去 国家 y
# 输出符合要求的编号 [1, k] 中的最小 k

# 读入
a, b, c, d = map(int, input().split())

# 对一个给定的 k，判断能派遣的人数，然后二分 k
# 根据题目要求定义序列区间
left, right = 1, 10**9
while left < right:
    k = (left + right) // 2

    # X 还需要多少人，数量是明确可以分给 X 的编号个数
    need_x = max(0, c - (k // b - k // (a*b)))
    # Y 还需要多少人，数量是明确可以分给 Y 的编号个数
    need_y = max(0, d - (k // a - k // (a*b)))

    # 可分配但是还未分配的编号个数
    total_available = k - k // a - k // b + k // (a*b)

    if total_available >= need_x + need_y:
        right = k
    else:
        left = k + 1

print(left)