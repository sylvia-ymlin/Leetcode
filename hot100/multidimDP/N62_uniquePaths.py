class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 机器人要到达目的地的所有路径
        # 使用动态规划
        # dp[i][j] 表示到达 (i, j) 的路径数，只能向右向下
        dp = [[0] * n for _ in range(m)]
        # 初始化第一行和第一列
        for i in range(m):
            dp[i][0] = 1  # 第一列只能向下走
        for j in range(n):
            dp[0][j] = 1  # 第一行只能向右走
        
        # 填充 dp 数组
        for i in range(1, m):
            for j in range(1, n):
                # 到达 (i, j) 有两种方式，从 (i-1, j) 向下走或从 (i, j-1) 向右走
                # 所以路径数是这两种方式的和
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]  # 返回到达 (m-1, n-1) 的路径数

