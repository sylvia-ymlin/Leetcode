class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Select some numbers from array such that their sum equals half of total sum of array elements
        # 0-1 Knapsack problem, whether to choose current element
        # dp[i][j]: whether there exists a sequence with sum j from array [0, i]

        n = len(nums)
        if n < 2:
            return False
        
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2
        # dp[0] = True subset with sum 0 always exists (empty set)
        dp = [True] + [False] * target
        for num in nums:
            # dp[j] ending with i, whether there exists subset with sum target
            for j in range(target, num - 1, -1):
                # If dp[j] == True already, return directly
                # dp[j] is not true yet, but we know dp[j-num] is true
                # Then adding current num, sum is exactly j, can return true
                dp[j] |= dp[j - num]
        
        return dp[target]
