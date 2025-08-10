class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 单次移动，但是总是记录当前可以跳到的最远位置
        res = 0
        for i, num in enumerate(nums):
            if i > res:
                return False  # 如果当前位置超过了最远位置，说明无法到达
            
            # 当前位置可以到达，更新最远位置
            res = max(res, i + num)

            if res >= len(nums) - 1:
                return True # 已经可以到达最后一个位置