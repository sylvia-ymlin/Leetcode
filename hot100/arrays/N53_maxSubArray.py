# find the subarray that has the maximum sum
# we only need to return the sum, not the subarray itself

from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 动态规划
        # f(i) 定义为以 nums[i] 结尾的最大子数组和
        # 计算 f(i) 的时候，我们需要考虑两种情况
        # 1. 如果 f(i-1) < 0，那么 f(i) = nums[i]
        # 2. 如果 f(i-1) >= 0，那么 f(i) = f(i-1) + nums[i]
        # 所以最终返回的就是 max(f(i)) for all i
        # 时间复杂度是 O(N), 空间复杂度是 O(N) if we don't destroy the original array
        
        # input: 1 <= nums.length <= 105

        mes = [0] * len(nums)
        mes[0] = nums[0]

        for i in range(1, len(nums)):
            if mes[i - 1] < 0:
                mes[i] = nums[i]
            else:
                mes[i] = mes[i - 1] + nums[i]
        return max(mes)

nums = [-2,1,-3,4,-1,2,1,-5,4]
sol = Solution()
result = sol.maxSubArray(nums)
print(result)  # Output: 6, because the subarray [4,-1,2,1] has the maximum sum of 6
