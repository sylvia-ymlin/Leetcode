from typing import List
import collections
import random
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Output order doesn't matter
        # Top k frequent elements, need to count element occurrences
        count = collections.Counter(nums)
        num_cnt = list(count.items()) # (term, count), need to sort by count
        n = len(num_cnt)
        topKs = self.findTopK(num_cnt, n-k)
        return [item[0] for item in topKs]

    def findTopK(self, nums: List[int], k: int):
        n = len(nums)
        left, right = 0, n-1
        while left <= right:
            pivotInx = random.randint(left, right)
            pivot = nums[pivotInx][1]
            lt, gt, cur = left, right, left
            while cur <= gt:
                if nums[cur][1] < pivot:
                    nums[cur], nums[lt] = nums[lt], nums[cur]
                    lt += 1
                    cur += 1
                elif nums[cur][1] > pivot:
                    nums[cur], nums[gt] = nums[gt], nums[cur]
                    gt -= 1
                else:
                    cur += 1
            if k == lt:
                print(nums)
                return nums[k:]
            elif k < lt:
                right = gt - 1
            else:
                left  = lt + 1
nums = [1,1,1,2,2,3]
test = Solution()
print(test.topKFrequent(nums, 2))
