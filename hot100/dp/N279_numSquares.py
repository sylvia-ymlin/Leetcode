class Solution:
    def numSquares(self, n: int) -> int:
        # f[i] represents the least number of perfect square numbers that sum to i
        # Enumeration, would be [1, ... , sqrt(i)]
        # State transition equation
        # f[i] = min(f[i - j * j]) + 1, 
        # where j> 0 and  j * j <= i

        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        
        return dp[n]
    
n = 13
solution = Solution()
print(solution.numSquares(n))  # Output: 2 (4 + 9)