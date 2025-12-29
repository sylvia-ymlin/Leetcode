# 给出一个正整数数组，给出有多少连续区间和不小于 x

# 判断的是大等于 x，前缀和 + 二分查找

n, x = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))

prefix_sum = [0] * (n + 1)
for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]

import bisect

count = 0
for i in range(1, n + 1): # 遍历前缀和
    target = prefix_sum[i] - x
    if target < 0:
        continue
    # 找到 prefix_sum 中第一个大于 target 的位置
    pos = bisect.bisect_right(prefix_sum, target, 0, i)
    count += pos # 0 ~ pos-1 均满足条件, 直接计 pos 个

print(count)
