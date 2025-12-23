# unsorted array, find the first missing positive integer
# rquire a linear time complexity O(N) and constant space complexity O(1)

from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # 步骤1：将所有无效数字(<=0 或 >n)替换为 n+1
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:  # 修正：加上 >n 的情况
                nums[i] = n + 1
        
        # 步骤2：使用数组索引标记数字的存在
        # 对于数字 x，将 nums[x-1] 标记为负数
        for i in range(n):
            num = abs(nums[i])  # 使用abs()获取原始值，因为可能已被标记为负数
            if num <= n:  # 只处理范围内的数字
                nums[num - 1] = -abs(nums[num - 1])  # 标记为负数，避免重复标记
        
        # 步骤3：找到第一个正数的位置
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        
        return n + 1 
        