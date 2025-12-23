
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # dp[i]: 以下标 i 字符结尾的最长有效括号的长度
        # 有效字符串一定以 ')' 结尾
        # s[i] == ')' -> s[i-1] == '(' -> dp[i] = dp[i-2] + 2
        # s[i] == ')' -> s[i-1] == ')' ，我们可以知道 s[i - dp[i-1]] = '(', 则 我们需要 s[i - dp[i-1]-1] = '('

        # 有效括号：左括号总先于右括号出现
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
