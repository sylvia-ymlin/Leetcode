from ast import List

# 寻找旋转排序数组中的最小值
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 旋转数组查找，最小值在旋转点，无重复元素

        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # 找有序子数组
            if nums[mid] > nums[right]: # 左边有序，最小值在右边
                left = mid + 1 # mid 不可能指向最小
            else: # nums[mid] <= nums[right]
                right = mid # mid 可能是最小值
        
        # 二分查找结束，left == right, 指向最小值
        return nums[left]  # left == right 时，指向最小值
