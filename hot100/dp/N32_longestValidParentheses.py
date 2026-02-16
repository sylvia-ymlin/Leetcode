
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # dp[i]: length of longest valid parentheses ending at index i
        # Valid string must end with ')'
        # s[i] == ')' -> s[i-1] == '(' -> dp[i] = dp[i-2] + 2
        # s[i] == ')' -> s[i-1] == ')', we know s[i - dp[i-1]] = '(', so we need s[i - dp[i-1]-1] = '('

        # Valid parentheses: left parenthesis always appears before right parenthesis
        if not s:
            return 0
        
        n = len(s)
        dp = [0] * n
        for i in range(1, n):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = dp[i-2] + 2 if i > 2 else 2
                else:
                    if i - dp[i-1] - 1 >= 0 and s[i - dp[i-1] - 1] == '(':
                        dp[i] = dp[i-1] + 2 + (dp[i - dp[i-1] - 2] if i - dp[i-1] - 2 >= 0 else 0)
            
        return max(dp)


s = "()(())"     
test = Solution()
print(test.longestValidParentheses(s))
