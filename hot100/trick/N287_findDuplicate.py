# Do not modify array and use only constant extra space
from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Array length n + 1, max value n, no need to worry about out of bounds
        # Phase 1: Fast and slow pointers find meeting point
        slow = nums[0]
        fast = nums[0]
        
        # Move once first, avoid being equal at start
        slow = nums[slow]        # Slow moves 1 step
        fast = nums[nums[fast]]  # Fast moves 2 steps
        
        while slow != fast:
            slow = nums[slow]        # Slow moves 1 step
            fast = nums[nums[fast]]  # Fast moves 2 steps
            
        # Phase 2: Find cycle entry point
        slow = nums[0]  # Reset slow pointer to start
        while slow != fast:
            slow = nums[slow]  # Both pointers move 1 step
            fast = nums[fast]
            
        return slow
    
        



nums = [3,1,3,4,2]
test = Solution()
test.findDuplicate(nums)