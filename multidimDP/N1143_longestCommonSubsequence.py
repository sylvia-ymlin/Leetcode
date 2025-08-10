class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 公共子序列的定义：
        # 删除若干个字符（也可以不删除）后，剩下的字符在原字符串中的相对位置不变
        # 例如 "ace" 是 "abcde" 的一个子序列
        # "aec" 不是 "abcde" 的一个子序列，因为 'e' 在 'c' 之后‘
        # 所以是找 text1 和 text2 中有多少个相同的字符，且这些字符在两个字符串中的相对位置是一样的

        # 那么对于 
        # dp[i][j] 表示 text1[0:i] 和 text2[0:j] 的最长公共子序列长度
        # if text1[i-1] == text2[j-1]:
        #     dp[i][j] = dp[i-1][j-1] + 1
        # else:
        #     dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        m, n = len(text1), len(text2)
        if m * n == 0:
            return 0
        
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[m][n]


