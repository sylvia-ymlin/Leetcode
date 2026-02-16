# unsorted array, find the first missing positive integer
# require a linear time complexity O(N) and constant space complexity O(1)

from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Step 1: Replace all invalid numbers (<=0 or >n) with n+1
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:  # Correct: add >n condition
                nums[i] = n + 1
        
        # Step 2: Use array index to mark presence of numbers
        # For number x, mark nums[x-1] as negative
        for i in range(n):
            num = abs(nums[i])  # Use abs() to get original value, as it might be marked negative
            if num <= n:  # Only handle numbers within range
                nums[num - 1] = -abs(nums[num - 1])  # Mark as negative, avoid double marking
        
        # Step 3: Find the first positive number position
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        
        return n + 1 
        