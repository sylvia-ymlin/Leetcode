from ast import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # Dynamic programming to solve minimum path sum
        # min(i, j) = grid[i][j] + min(min(i-1, j), min(i, j-1))
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        # Construct 2D dp array
        dp = [[0] * n for _ in range(m)]
        # Initialize first row and first column
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        
        # Fill dp array
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        
        return dp[m-1][n-1]  # Return minimum path sum to bottom right corner