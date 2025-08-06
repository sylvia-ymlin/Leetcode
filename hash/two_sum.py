
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # first we need to create a dictionary to store the indices of the numbers
        num_to_index = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i

        return []

# the key idea is to use a dictionary to store the indices of the numbers we have seen so far, and for each number, we check if its complement (target - num) exists in the dictionary. If it does, we return the indices of the two numbers.
# This approach has a time complexity of O(N) and a space complexity of O(N).

# for ACM models, we design the input is a list of integers and a target integer. We call the function as
sol = Solution()
result = sol.twoSum([2, 7, 11, 15], 9)
print(result)