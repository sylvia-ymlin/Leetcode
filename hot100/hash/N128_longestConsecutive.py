# an unsorted array, return the length of the longest consecutive elements sequence.

# Your algorithm should run in O(n) complexity.

from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # according to the requirement, we should only pass the list once
        
        # find whether a number in the set -> use a set for O(1) 
        num_set = set(nums)  # O(N) to create a set from the list
        longest_streak = 0
        
        for num in num_set:
            # find the start, and see if its posterior exists
            if num - 1 not in num_set: 
                current_num = num
                current_streak = 1
                # how many consecutive numbers are there
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                # the number that has the most consecutive numbers
                longest_streak = max(longest_streak, current_streak)

        return longest_streak

# time complexity is O(N) for creating the set and O(N) for iterating through the set, so overall O(N)
# space complexity is O(N) for the set