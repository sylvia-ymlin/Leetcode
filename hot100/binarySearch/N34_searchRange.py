# Duplicate elements exist, probe forward and backward, return index range
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1
        flag = False
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                flag = True
                break
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        if not flag:
            return [-1, -1]
        
        left = mid
        while left > 0:
            if nums[left-1] != target:
                break
            left -= 1
        
        right = mid
        while right < len(nums) - 1:
            if nums[right + 1] != target:
                break
            right += 1
        
        return [left, right]

# Time complexity O(N), consider worst case where all elements equal target, finally need to traverse entire array twice

# Optimization:
# Find leftmost equal to target
# Find rightmost equal to target
# Two binary searches, time complexity O(logN)

class Solution2:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        leftIdx = -1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                # Record
                leftIdx = mid
                # Continue left
                right = mid - 1
        
        if leftIdx == -1: # No target value
            return [-1, -1]
        
        left, right = 0, len(nums) - 1
        rightIdx = -1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                # Record
                rightIdx = mid
                # Continue right
                left = mid + 1
        
        return [leftIdx, rightIdx]
