# 动态规划求解最长回文子串
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        
        # dp[i][j] 表示 s[i:j+1] 是否是回文串
        # 状态转移方程：
        # dp[i][j] = dp[i+1, j-1] and s[i] == s[j]

        dp = [[False] * n for _ in range(n)]
        start, end, max_length = 0, 0, 1

        for j in range(n):
            for i in range(j + 1):
                if s[i] == s[j]:
                    if j - i <= 2:  # 长度为1或2的回文串
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

                    if dp[i][j] and (j - i + 1) > max_length:
                        max_length = j - i + 1
                        start, end = i, j
        
        return s[start:end + 1]  # 返回最长回文子串

# 优化空间复杂度为 O(n)
class Solution2:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        # dp[i][j] =  dp[i+1, j-1] and s[i] == s[j]
        # 只需要一维数组来存储当前行的状态, 优化为
        # dp[i] 表示 s[i:j-1] 是否是回文串，代表上一行的状态

        dp = [True] * n
        start, end, max_length = 0, 0, 1
        
        for j in range(n):
            for i in range(j + 1): # j 在这个循环中是固定的
                # 单个字符是回文串
                if i == j:
                    dp[i] = True # dp[i][j] = True
                # 长度 2 的字符串
                elif j - i == 1:
                    dp[i] = (s[i] == s[j])
                else:
                    # dp[i] -> dp[i, j]
                    # dp[i+1] -> dp[i+1, j-1]
                    dp[i] = (s[i] == s[j]) and dp[i + 1]
                
                if dp[i] and (j - i + 1) > max_length:
                    max_length = j - i + 1
                    start, end = i, j

        return s[start:end + 1]  # 返回最长回文子串


s = "babad"
test = Solution()
print(test.longestPalindrome(s))  # 输出 "bab" 或 "aba"，取决于实现细节