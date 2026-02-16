from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # Backtracking
        # Pick or not pick each number
        def backtrack(start=0, path=[]):
            # If selected current node and get a feasible solution
            res.append(path[:])
            # Print current result
            print(res)
            
            # Iterate to last number, recursion ends
            for i in range(start, len(nums)):
                # Make choice, pick nums[i]
                path.append(nums[i])

                # Recursion, process next number
                # Subproblem, consider next number i + 1
                backtrack(i + 1, path)

                # Undo choice, don't pick nums[i]
                path.pop()

        res = []
        backtrack()
        return res

# Test
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3]
    print(f"Input: {nums}")
    subsets = solution.subsets(nums)
    print(f"Output all subsets: {subsets}")

# [[]]
# [[], [1]]
# [[], [1], [1, 2]]
# [[], [1], [1, 2], [1, 2, 3]]
# [[], [1], [1, 2], [1, 2, 3], [1, 3]]
# [[], [1], [1, 2], [1, 2, 3], [1, 3], [2]]
# [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3]]
# [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]