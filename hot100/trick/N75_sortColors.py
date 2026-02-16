# Sort three colors in-place

from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        ptr = 0
        for i in range(n):
            if nums[i] == 0:
                nums[i], nums[ptr] = nums[ptr], nums[i]
                ptr += 1
        for i in range(ptr, n):
            if nums[i] == 1:
                nums[i], nums[ptr] = nums[ptr], nums[i]
                ptr += 1

# One traversal, two pointers, p0 swaps 0, p1 swaps 1
class Solution2:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        # p0 maintains position where next 0 should be inserted
        # p1 maintains position where next 1 should be inserted
        p0 = p1 = 0
        for i in range(n):
            if nums[i] == 1:
                nums[i], nums[p1] = nums[p1], nums[i]
                p1 += 1
            elif nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                # When swapping '0', if p0 < p1, means '1' was swapped to i
                if p0 < p1:
                    # Put swapped 1 back to correct position
                    nums[i], nums[p1] = nums[p1], nums[i]
                p0 += 1
                # If no 1 after 0, insert a 0, still need to move p1 forward
                # If 1 after 0, previous if inserted a new 1, need to move p1 forward
                p1 += 1
        