# 乘积最大非空连续数组
from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp_max = nums[:]
        dp_min = nums[:]

        for i in range(1, len(nums)):
            # if 0, all will be zero
            # if num > 0, max(nums[i],dp_max[i-1]*nums[i])
            # if num < 0, min(nums[i],dp_min[i-1]*nums[i])
            # 可以合并
            dp_max[i] = max(dp_min[i-1]*nums[i],nums[i],dp_max[i-1]*nums[i])
            dp_min[i] = min(dp_min[i-1]*nums[i],nums[i],dp_max[i-1]*nums[i])
        return max(dp_max)



nums = [3,-1,4]
solution = Solution()
print(solution.maxProduct(nums))  # Output: 4