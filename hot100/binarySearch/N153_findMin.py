from ast import List

# Find minimum in rotated sorted array
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Rotated array search, minimum is at rotation point, no duplicate elements

        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # Find sorted subarray
            if nums[mid] > nums[right]: # Left side sorted, minimum is on right side
                left = mid + 1 # mid cannot be minimum
            else: # nums[mid] <= nums[right]
                right = mid # mid could be minimum
        
        # Binary search ends, left == right, pointing to minimum
        return nums[left]  # When left == right, points to minimum
