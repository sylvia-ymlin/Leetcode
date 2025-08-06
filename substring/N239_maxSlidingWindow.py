# find the largest element in current sliding window

# pass through the array, and during the initialization, find the maxixum element in current sliding window, if the moving out element is the maximumm, then we need to find the next maximum, that's the difficult part.

# a nature idea is to use a heap to store the elements in the current sliding window, the first selement will always be the maxixum element, but the time complexity is O(NlogK), we can do better.

# we could monitor a deque
from typing import List
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque() # 双端队列，存储当前窗口的最大值的索引

        l = r = 0

        while r < len(nums):
            # since the sliding window moves from left to right, so if our current element is larger than the left elements, then those elements are meaningless, we can remove them from the deque
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            # add current element
            q.append(r)

            if l > q[0]: # current maximum is out of the window, we need to remove it
                q.popleft()

            if r - l + 1 == k:
                # we have a valid window, output current maximum
                res.append(nums[q[0]])
                l += 1
            
            r += 1
        
        return res
            