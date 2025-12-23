# 搜索旋转数组
# mid 位置划分数组，两个有且只能有一个有序
# [left, mid]
# [mid, right]
# 我们需要判断下一次搜索的上下界
# 如果 左边有序，mid 是左边最大值
# 如果右边有序， mid 是右边最小值

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]: # 左边有序
                if nums[0] <= target < nums[mid]: # 目标值在左
                    r = mid - 1
                else: # 目标值在右
                    l = mid + 1
            else: # 右边有序
                if nums[mid] < target <= nums[len(nums) - 1]: # 目标值在右
                    l = mid + 1
                else: # 目标值在左
                    r = mid - 1
        return -1
    
