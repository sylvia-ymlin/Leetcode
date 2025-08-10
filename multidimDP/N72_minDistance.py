# 编辑距离
# 其实四个操作
# 0，什么也不做
# 1，删除一个字符
# 2，插入一个字符
# 3，替换一个字符

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 动态规划求解编辑距离
        # dp[i][j] 表示 word1[0:i] 和 word2[0:j] 的编辑距离
        m, n = len(word1), len(word2)
        # 其中一个字符串为空字符串时，编辑距离为另一个字符串的长度
        if n * m == 0:
            return n + m
        
        # 动态规划状态转移方程：i -> j
        # if word1[i-1] == word2[j-1]:
        #     dp[i][j] = dp[i-1][j-1]
        # else:
        #     dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        # 替换操作：dp[i-1][j-1] + 1
        # 删除操作：dp[i-1][j] + 1
        # 插入操作：dp[i][j-1] + 1

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # 第一行和第一列的初始化
        for i in range(m + 1):
            dp[i][0] = i  # word1[0:i] 到空字符串的编辑距离为 i
        for j in range(n + 1):
            dp[0][j] = j  # 空字符串到 word2[0:j] 的编辑距离为 j

        # 填充 dp 数组
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        
        return dp[m][n]