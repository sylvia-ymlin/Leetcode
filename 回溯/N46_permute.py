# 不含重复数字的数组，返回全排列

# 回溯法：
# 探索所有可能的候选解从而找出所有解
# 候选解如果不是目标解或者不是最后一个候选解，就回溯再探索

# 全排列过程，i表示当前处理的数字位置
# n x n-1 x n-2 x ... x 1 = n! 种排列方式
# 整个排列过程是一个树形结构

from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        # start 标记的是当前处理的数字在 排列中的位置
        # start 指向我们当前要处理的位置
        # 循环中 i 表示我们要在 start 填入的数字
        def backtrack(start=0):
            # 如果 start 达到数组长度，说明一个排列完成
            if start == len(nums):
                # 找到一个可行解
                res.append(nums[:])
                return
            
            # start 将 数组划分为两部分
            # [0, start-1] 已经处理好的部分
            # [start, n-1] 还未处理的部分
            # 循环将 [start, n-1] 中的每个数字依次放到 start 位置
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]

                # 新的划分，递归处理下一个位置
                # 子问题，在 start + 1 位置做选择
                backtrack(start + 1) 

                # 找到一个可行解，回溯恢复原始顺序
                nums[start], nums[i] = nums[i], nums[start]

        # 存放结果数组
        res = []
        backtrack()
        return res

        
