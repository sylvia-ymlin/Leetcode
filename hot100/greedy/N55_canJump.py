class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Single move, but always record the furthest position reachable currently
        res = 0
        for i, num in enumerate(nums):
            if i > res:
                return False  # If current position exceeds furthest position, it means unreachable
            
            # Current position is reachable, update furthest position
            res = max(res, i + num)

            if res >= len(nums) - 1:
                return True # Already can reach the last position