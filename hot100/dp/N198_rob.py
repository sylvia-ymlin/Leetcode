from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # Cannot rob adjacent houses
        # dp[i] represents the max money robbed up to the i-th house
        # State transition equation
        # If rob current house: dp[i] = dp[i-2] + nums[i]
        # If not rob current house: dp[i] = dp[i-1]
        # Take max of both: dp[i] = max(dp[i-1], dp[i-2] + nums[i]) -> i >= 2

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

            