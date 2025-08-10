from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # 不能偷窃相同的房屋
        # dp[i] 表示偷窃到第 i 个房屋的最大金额
        # 状态转移方程
        # 如果当前房子偷窃： dp[i] = dp[i-2] + nums[i]
        # 如果当前房子不偷窃： dp[i] = dp[i-1]
        # 取两者的最大值： dp[i] = max(dp[i-1], dp[i-2] + nums[i]) -> i >= 2

        dp = [0] * len(nums)
        for i in range(0, len(nums)):
            if i == 0:
                dp[i] = nums[i]
            elif i == 1:
                dp[i] = max(nums[i], dp[i - 1])
            else:
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
    
        return dp[-1]

nums = [1,2,3,1]
test = Solution()
print(test.rob(nums))  # Output: 12

            