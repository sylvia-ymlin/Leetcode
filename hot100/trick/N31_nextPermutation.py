# Next Permutation
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Think: How to get a larger sequence from current sequence, without other intermediate sequences existing between them
        # Look from back to front, find first sequence that can be permuted, then find first number larger than first element (first in sorting order) from this sequence, swap, sort remaining sequence ascendingly

        n = len(nums) - 1
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        if i >= 0:
            # Descending order
            j = len(nums) - 1
            # Find first element larger than nums[i] from right
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
            # Swap
            nums[i], nums[j] = nums[j], nums[i]
        
        # left to right is definitely descending, reverse it
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

            
