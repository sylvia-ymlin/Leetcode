'''
m 个员工买了 n 个月饼， m <= n
每个员工至少分的一个月饼
对员工分到的月饼数降序，相邻两个数不超过 3
'''

m, n = map(int, input().split())

remain = n - m  # 先给每个人分一个月饼，剩下的月饼

# dp[i][j][last] = 前i个人，分配j个剩余月饼，第i个人额外分last个的方案数
# 降序排列：第1个人分的最多，第m个人分的最少
# 相邻差不超过3：a[i] - a[i+1] <= 3

# 每个值只会计算一次，不存在重复计算，不需要记忆化搜索
dp = [[[0] * (remain + 1) for _ in range(remain + 1)] for _ in range(m + 1)]

# 初始化：第1个人额外分last个
for last in range(remain + 1):
    dp[1][last][last] = 1

# 状态转移
for i in range(1, m):  # 前i个人已分配
    for j in range(remain + 1):  # 已分配j个剩余月饼
        for last in range(j, -1, -1):  # 优化：last最多为j
            if dp[i][j][last] == 0:
                continue
            # 第i+1个人额外分curr个：curr <= last 且 last - curr <= 3
            for curr in range(max(0, last - 3), min(last, remain - j) + 1):  # 优化边界
                dp[i + 1][j + curr][curr] += dp[i][j][last]

# 答案：前m个人分配完remain个剩余月饼
result = sum(dp[m][remain])
print(result)

