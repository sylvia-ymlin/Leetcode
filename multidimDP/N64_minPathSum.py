from ast import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 动态规划求解最小路径和
        # min(i, j) = grid[i][j] + min(min(i-1, j), min(i, j-1))
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        # 构造二维 dp 数组
        dp = [[0] * n for _ in range(m)]
        # 初始化第一行和第一列
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        
        # 填充 dp 数组
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        
        return dp[m-1][n-1]  # 返回右下角的最小路径和