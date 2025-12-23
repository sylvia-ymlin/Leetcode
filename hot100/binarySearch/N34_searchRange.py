# 存在相等元素，前后探查，返回下标范围
from typing improt list
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

# 时间复杂度 O(N), 考虑最坏的请求，所有元素都等于目标值，最后需要两次遍历整个数组

# 优化：
# 查找 最左边等于 target 的
# 查找 最右边等于 target 的
# 两次 二分查找， 时间复杂度 O(logN)

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
                # 记录
                leftIdx = mid
                # 继续向左
                right = mid - 1
        
        if leftIdx == -1: # 没有目标值
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
                # 记录
                rightIdx = mid
                # 继续向右
                left = mid + 1
        
        return [leftIdx, rightIdx]
