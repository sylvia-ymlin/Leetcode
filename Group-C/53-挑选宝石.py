# 给出一组数，从这组数中找到 x 个数，乘积不小于 y
# 输出有多少种方案

# 数组长度小于 20
# 暴力枚举

from itertools import combinations
n, x, y = map(int, input().split())
arr = list(map(int, input().split()))
count = 0
for combo in combinations(arr, x): # 为什么不用 permutations ? 因为顺序不重要；顺序重要用 permutations
    prod = 1
    for num in combo:
        prod *= num
    if prod >= y:
        count += 1

print(count)