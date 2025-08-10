from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] 表示凑成金额 i 的最少硬币数量
        # 状态转移方程
        # dp[i] = min(dp[i - coin]) + 1 for each coin in coins

        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[amount] if dp[amount] != float('inf') else -1