# Return the kth largest element in an array
# Build a max heap, pop k-1 times, return heap top

# Sort and return kth element
# Optimal Time Complexity: O(NlogN)
# Space Complexity: O(N)

# Use Max Heap
# Optimal Time Complexity: O(N + klogN), k is the kth largest element to find, because maintaining heap takes O(logN)
# Space Complexity: O(N)

from random import random
from typing import List
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Use Max Heap
        max_heap = []

        for num in nums:
            heapq.heappush(max_heap, -num)  # Push element to heap, use negative number to implement max heap
        
        # Pop k-1 elements
        for _ in range(k - 1):
            heapq.heappop(max_heap)
        
        # Return heap top, i.e., kth largest element
        return -max_heap[0]

# Selection algorithm based on Quick Sort, expected linear time
# Idea of Quick Sort is, choose a pivot each time, partition array into two parts, left part not greater than pivot, right part not smaller than pivot, we can determine position of pivot after sorting
# So we only need to find a pivot such that its position is len(nums) - k, without ensuring the two partitioned parts are sorted, which can reduce time complexity from O(NlogN) to O(N)
# Optimal Time Complexity: O(N), Worst Case O(N^2)
# Space Complexity: O(1)

from typing import List

class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        target = n - k  # Index in ascending order
        left, right = 0, n - 1

        while left <= right:
            pivot_idx = random.randint(left, right)
            pivot = nums[pivot_idx]

            # Dutch National Flag partition
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