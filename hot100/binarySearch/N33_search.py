# Search in rotated sorted array
# mid position divides array, exactly one side is sorted
# [left, mid]
# [mid, right]
# We need to determine the bounds for next search
# If left side is sorted, mid is max on left
# If right side is sorted, mid is min on right

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]: # Left side sorted
                if nums[0] <= target < nums[mid]: # Target on left
                    r = mid - 1
                else: # Target on right
                    l = mid + 1
            else: # Right side sorted
                if nums[mid] < target <= nums[len(nums) - 1]: # Target on right
                    l = mid + 1
                else: # Target on left
                    r = mid - 1
        return -1
    
