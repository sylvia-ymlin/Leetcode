# Array without duplicates, return all permutations

# Backtracking:
# Explore all possible candidate solutions to find all solutions
# If candidate solution is not target solution or not the last candidate solution, backtrack and explore again

# Permutation process, i indicates position of current number being processed
# n x n-1 x n-2 x ... x 1 = n! permutations
# The whole permutation process is a tree structure

from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        # start marks position of current number being processed in permutation
        # start points to the position we want to process
        # i in loop indicates the number we want to fill in start
        def backtrack(start=0):
            # If start reaches array length, a permutation is complete
            if start == len(nums):
                # Found a feasible solution
                res.append(nums[:])
                return
            
            # start divides array into two parts
            # [0, start-1] processed part
            # [start, n-1] unprocessed part
            # Loop puts every number in [start, n-1] to start position sequentially
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]

                # New partition, recursively process next position
                # Subproblem, make choice at start + 1 position
                backtrack(start + 1) 

                # Found a feasible solution, backtrack to restore original order
                nums[start], nums[i] = nums[i], nums[start]

        # Store result array
        res = []
        backtrack()
        return res

        
