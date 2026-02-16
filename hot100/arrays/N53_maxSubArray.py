# find the subarray that has the maximum sum
# we only need to return the sum, not the subarray itself

from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Dynamic Programming
        # f(i) is defined as the max subarray sum ending at nums[i]
        # When calculating f(i), we consider two cases
        # 1. If f(i-1) < 0, then f(i) = nums[i]
        # 2. If f(i-1) >= 0, then f(i) = f(i-1) + nums[i]
        # So return max(f(i)) for all i
        # Time complexity is O(N), space complexity is O(N) if we don't destroy the original array
        
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
