class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # All paths for robot to reach destination
        # Use dynamic programming
        # dp[i][j] represents number of paths to reach (i, j), can only move right or down
        dp = [[0] * n for _ in range(m)]
        # Initialize first row and first column
        for i in range(m):
            dp[i][0] = 1  # First column can only be reached by moving down
        for j in range(n):
            dp[0][j] = 1  # First row can only be reached by moving right
        
        # Fill dp array
        for i in range(1, m):
            for j in range(1, n):
                # To reach (i, j) there are two ways: move down from (i-1, j) or move right from (i, j-1)
                # So the number of paths is the sum of these two ways
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]  # Return number of paths to reach (m-1, n-1)

