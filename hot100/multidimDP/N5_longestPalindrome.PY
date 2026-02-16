# Dynamic programming to solve longest palindrome substring
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        
        # dp[i][j] represents whether s[i:j+1] is a palindrome substring
        # State transition equation:
        # dp[i][j] = dp[i+1, j-1] and s[i] == s[j]

        dp = [[False] * n for _ in range(n)]
        start, end, max_length = 0, 0, 1

        for j in range(n):
            for i in range(j + 1):
                if s[i] == s[j]:
                    if j - i <= 2:  # Palindrome of length 1 or 2
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

                    if dp[i][j] and (j - i + 1) > max_length:
                        max_length = j - i + 1
                        start, end = i, j
        
        return s[start:end + 1]  # Return longest palindrome substring

# Optimized space complexity to O(n)
class Solution2:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        # dp[i][j] =  dp[i+1, j-1] and s[i] == s[j]
        # Only need one-dimensional array to store current row state, optimize to
        # dp[i] represents whether s[i:j-1] is a palindrome, representing previous row state

        dp = [True] * n
        start, end, max_length = 0, 0, 1
        
        for j in range(n):
            for i in range(j + 1): # j is fixed in this loop
                # Single character is palindrome
                if i == j:
                    dp[i] = True # dp[i][j] = True
                # String of length 2
                elif j - i == 1:
                    dp[i] = (s[i] == s[j])
                else:
                    # dp[i] -> dp[i, j]
                    # dp[i+1] -> dp[i+1, j-1]
                    dp[i] = (s[i] == s[j]) and dp[i + 1]
                
                if dp[i] and (j - i + 1) > max_length:
                    max_length = j - i + 1
                    start, end = i, j

        return s[start:end + 1]  # Return longest palindrome substring


s = "babad"
test = Solution()
print(test.longestPalindrome(s))  # 输出 "bab" 或 "aba"，取决于实现细节