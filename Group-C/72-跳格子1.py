# n 个连续格子，每个格子有不同的分数
# 可以选择任何位置起跳，但是不能跳连续的格子，也不能回头
# 计算能得到的最高分

nums = list(map(int, input().split()))
n = len(nums)

# 动态规划：从后往前
# dp[i] = 从位置 i 开始能得到的最高分
# 跳到 j（j >= i+2）后，得分为 nums[i] + dp[j]

dp = [0] * n
# 最后两个位置的分数就是它们本身
dp[n - 1] = nums[n - 1]
if n > 1:
    dp[n - 2] = nums[n - 2]

# 从倒数第三个位置开始计算
for i in range(n - 3, -1, -1):
    # 可以跳到 i+2, i+3, ..., n-1
    dp[i] = nums[i] + max(dp[i + 2:])

print(max(dp))
    