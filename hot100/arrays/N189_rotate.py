# 数组元素向右轮转k个位置，移出的元素放到数组头部
# in place

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)  # 处理k大于数组长度的情况

        # the idea is inverse the array three times
        def reverse(start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        reverse(0, len(nums) - 1)
        reverse(0, k - 1)
        reverse(k, len(nums) - 1)