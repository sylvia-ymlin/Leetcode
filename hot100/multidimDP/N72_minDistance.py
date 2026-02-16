# Edit Distance
# Actually four operations
# 0, do nothing
# 1, delete a character
# 2, insert a character
# 3, replace a character

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Dynamic programming to solve edit distance
        # dp[i][j] represents edit distance between word1[0:i] and word2[0:j]
        m, n = len(word1), len(word2)
        # When one string is empty, edit distance is length of the other string
        if n * m == 0:
            return n + m
        
        # Dynamic programming state transition equation: i -> j
        # if word1[i-1] == word2[j-1]:
        #     dp[i][j] = dp[i-1][j-1]
        # else:
        #     dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        # Replace operation: dp[i-1][j-1] + 1
        # Delete operation: dp[i-1][j] + 1
        # Insert operation: dp[i][j-1] + 1

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Initialize first row and first column
        for i in range(m + 1):
            dp[i][0] = i  # Edit distance from word1[0:i] to empty string is i
        for j in range(n + 1):
            dp[0][j] = j  # Edit distance from empty string to word2[0:j] is j

        # Fill dp array
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        
        return dp[m][n]