# 两个字符串构成一个 m*n 矩阵，求从左上角到右下角的最短路径长度
# 如果当前位置的字符相同，则可以斜向移动，否则只能向下或向右移动
# 使用动态规划解决该问题

str1, str2 = input().split()
m, n = len(str1), len(str2)

# DP 矩阵 (m+1) x (n+1)
dp = [[0]*(n+1) for _ in range(m+1)]

# 初始化第一行和第一列
for i in range(1, m+1):
    dp[i][0] = i
for j in range(1, n+1):
    dp[0][j] = j

# 填充 DP 矩阵
for i in range(1, m+1):
    for j in range(1, n+1):
        # 计算当前位置的最短路径长度, 考虑三种可能的移动方式,取最小值
        candidates = [dp[i-1][j] + 1, dp[i][j-1] + 1]  # 向下或向右
        if str1[i-1] == str2[j-1]:
            candidates.append(dp[i-1][j-1] + 1)  # 相同可以斜向
        dp[i][j] = min(candidates)

print(dp[m][n])