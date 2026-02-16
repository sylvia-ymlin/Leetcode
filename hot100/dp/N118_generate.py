class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Generate Pascal's Triangle
        # dp[i] represents the value of the i-th element in the previous row
        # pre_dp = dp[:]
        # dp = [1] * (numRows + 1)
        # dp[i] = pre_dp[i - 1] + pre_dp[i] if i > 0

        dp = [[1]]
        for row in range(1, numRows):
            res = [1] * (row + 1)  # New row, length is row + 1
            for i in range(1, row + 1):
                res[i] = dp[row - 1][i - 1] + dp[row - 1][i] if i < row else 1
            dp.append(res)
        
        return dp

