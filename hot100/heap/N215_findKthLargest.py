# 返回数组中第 k 大的数
# 构建最大堆，pop k-1 次，返回堆顶元素

# 排序返回第 k 个元素
# 最优 时间复杂度：O(NlogN)
# 空间复杂度：O(N)

# 使用最大堆
# 最优 时间复杂度：O(N + klogN)， k 是要找的第 k 大元素，因为维护堆的时间复杂度是 O(logN)
# 空间复杂度：O(N)

from random import random
from typing import List
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 使用最大堆
        max_heap = []

        for num in nums:
            heapq.heappush(max_heap, -num)  # 将元素入堆，使用负数实现最大堆
        
        # 弹出 k-1 个元素
        for _ in range(k - 1):
            heapq.heappop(max_heap)
        
        # 返回堆顶元素，即第 k 大的元素
        return -max_heap[0]

# 基于快排，期望为线性的选择算法
# 快排的思想是，每次选择一个 pivot，将数组分为两部分，左半边的数都不大于 pivot，右半边的数都不小于 pivot，我们可以确定 pivot 在排序后的位置
# 那么我们只需要找到一个 pivot，使得它的位置是 len(nums) - k，而不需要保证划分出的两部分是有序的，将可以将时间复杂度从 O(NlogN) 降低到 O(N)
# 最优 时间复杂度：O(N)，最坏 O(N^2)
# 空间复杂度：O(1)

from typing import List

class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        target = n - k  # 在升序排列中的索引
        left, right = 0, n - 1

        while left <= right:
            pivot_idx = random.randint(left, right)
            pivot = nums[pivot_idx]

            # 荷兰国旗三路划分
            lt, i, gt = left, left, right
            while i <= gt:
                if nums[i] < pivot:
                    nums[lt], nums[i] = nums[i], nums[lt]
                    lt += 1
                    i += 1
                elif nums[i] > pivot:
                    nums[i], nums[gt] = nums[gt], nums[i]
                    gt -= 1
                else:
                    i += 1

            # now: [left, lt-1] < pivot, [lt, gt] == pivot, [gt+1, right] > pivot
            if target < lt:
                right = lt - 1
            elif target > gt:
                left = gt + 1
            else:
                return pivot