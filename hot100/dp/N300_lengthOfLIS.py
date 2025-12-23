from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] 表示以 nums[i] 结尾的最长严格递增子序列的长度
        # 子序列是相对顺序相同，而不是连续的
        # 状态转移方程
        # dp[i] = max(dp[j]) + 1 for all j < i where nums[j] < nums[i]  
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)
    