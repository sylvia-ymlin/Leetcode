# 下一个排列
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 思考，如何从当前序列得到一个更大的序列，且其中不存在其他中间序列
        # 从后往前看，找到第一个可以排列的数列，然后从这个序列中找到第一个比首位大的数（排序上的第一个），交换，对后面的序列升序排序

        n = len(nums) - 1
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        if i >= 0:
            # 降序排列
            j = len(nums) - 1
            # 从右往走找到第一个大于 nums[i] 的
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
            # 交换
            nums[i], nums[j] = nums[j], nums[i]
        
        # left 到 right 一定是 降序的，反转
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

            
