# 不修改数组且只使用常量级额外空间
from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 数组长度 n + 1, 最大值 n，不用担心越界问题
        # 第一阶段：快慢指针找到相遇点
        slow = nums[0]
        fast = nums[0]
        
        # 先移动一次，避免在起点就相等
        slow = nums[slow]        # 慢指针走1步
        fast = nums[nums[fast]]  # 快指针走2步
        
        while slow != fast:
            slow = nums[slow]        # 慢指针走1步
            fast = nums[nums[fast]]  # 快指针走2步
            
        # 第二阶段：找到环的入口点
        slow = nums[0]  # 重置慢指针到起点
        while slow != fast:
            slow = nums[slow]  # 两个指针都走1步
            fast = nums[fast]
            
        return slow
    
        



nums = [3,1,3,4,2]
test = Solution()
test.findDuplicate(nums)