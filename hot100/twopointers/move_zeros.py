# move all the zeros to the end of the list, while maintaining the relative order of the non-zero elements
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # the easiest way is move all non-zero elements to the front, and then fill the rest with zeros
        index_non_zero = 0  # index to place the next non-zero element
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[index_non_zero] = nums[i]
                index_non_zero += 1
        
        # fill the rest of the list with zeros
        for i in range(index_non_zero, len(nums)):
            nums[i] = 0
        
        # any other easiest way?
        # we can also use two pointers, one for the current element, one for the next non-zero element, and swap

class SolutionTwoPointers:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        left = right = 0  
        # the idea is, the right pointer always finds the non-zero element, when it finds one, it swaps with the left pointer, and then both of them move forward. We can make sure all the elements left of the left pointer are non-zero.
        while right < n:
            # if the current element is non-zero,
            if nums[right] != 0:
                # swap the elements at left and right
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1