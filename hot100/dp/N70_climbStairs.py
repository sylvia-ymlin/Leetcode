class Solution:
    def climbStairs(self, n: int) -> int:
        # dp[i] 表示爬到第 i 阶的方法数
        # 状态转移方程：dp[i] = dp[i-1] + dp[i-2]
        dp = [-1] * (n + 1)

        def dep(goal: int) -> int:
            # 记忆化搜索，避免重复计算
            if dp[goal] != -1:
                return dp[goal]
            
            if goal <= 2:
                return goal
            else:
                dp[goal] = dep(goal - 1) + dep(goal - 2)
            
            return dp[goal]

        return dep(n)
