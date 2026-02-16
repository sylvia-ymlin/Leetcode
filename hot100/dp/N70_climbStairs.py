class Solution:
    def climbStairs(self, n: int) -> int:
        # dp[i] represents number of ways to reach i-th step
        # State transition equation: dp[i] = dp[i-1] + dp[i-2]
        dp = [-1] * (n + 1)

        def dep(goal: int) -> int:
            # Memoization search to avoid repeated calculation
            if dp[goal] != -1:
                return dp[goal]
            
            if goal <= 2:
                return goal
            else:
                dp[goal] = dep(goal - 1) + dep(goal - 2)
            
            return dp[goal]

        return dep(n)
