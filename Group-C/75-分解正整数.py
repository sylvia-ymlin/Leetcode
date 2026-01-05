# 给一个正整数，将其分解为 m 个连续正整数的和，输出 m 最小的解

# 假设 m 个正整数：最小数是 x，则有：
# x + (x+1) + (x+2) + ... + (x+m-1) = n
# 即 m*x + (1+2+...+(m-1)) = n
# 即 m*x + m*(m-1)/2 = n
# 即 m*x = n - m*(m-1)/2
# 即 x = (n - m*(m-1)/2) / m
# 因为 x 是正整数，所以 n - m*(m-1)/2 必须大于 0，且能被 m 整除
# 从 m=2 开始递增，直到 n - m*(m-1)/2 <= 0 为止
# 无法分解这输出 ‘N'

# 输出表达式

n = int(input())
m = 2
found = False
while True:
    remainder = n - m * (m - 1) // 2
    if remainder <= 0:
        break
    if remainder % m == 0:
        x = remainder // m
        if x > 0:
            found = True
            result = '+'.join(str(x + i) for i in range(m))
            break
    m += 1

if not found:
    print('N')
else:
    print(f"{n}=" + result)