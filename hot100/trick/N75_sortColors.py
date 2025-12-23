# 只有三个数的原地排序

from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        ptr = 0
        for i in range(n):
            if nums[i] == 0:
                nums[i], nums[ptr] = nums[ptr], nums[i]
                ptr += 1
        for i in range(ptr, n):
            if nums[i] == 1:
                nums[i], nums[ptr] = nums[ptr], nums[i]
                ptr += 1

# 一次遍历，两个指针，p0 交换 0， p1 交换 1
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        # p0 维护后一个0应该插入的位置
        # p1 维护后一个1应该插入的位置
        p0 = p1 = 0
        for i in range(n):
            if nums[i] == 1:
                nums[i], nums[p1] = nums[p1], nums[i]
                p1 += 1
            elif nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                # 交换 ‘0’ 时，if p0 < p1, 说明交换了 ‘1’ 到 i
                if p0 < p1:
                    # 把交换出的 1 放到正确位置
                    nums[i], nums[p1] = nums[p1], nums[i]
                p0 += 1
                # 如果 0 后还没有 1， 插入一个 0， 仍然需要把 p1 后移
                # 如果 0 后有 1， 上一个 if 插入了一个新 1，需要 p1 后移
                p1 += 1
        