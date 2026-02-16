# Return product of all elements except self
# 0 is 0
# No division allowed, time complexity O(N)

from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        L, R, res = [0] * n, [0] * n, [0] * n

        L[0] = 1
        for i in range(1, n):
            L[i] = nums[i-1] * L[i - 1]

        R[n-1] = 1
        for i in reversed(range(n-1)):
            R[i] = nums[i + 1] * R[i + 1]
        
        for i in range(n):
            res[i] = L[i] * R[i]
    
        return res

# if we want a solution with O(1) space complexity
class SolutionO1Space:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        for i in range(1, n):
            # left product until (i-1)-th number
            res[i] = nums[i-1] * res[i - 1] # [1,1,2,6]

        right_product = 1
        for i in reversed(range(n)):
            res[i] *= right_product
            right_product *= nums[i] # update right_product
            print(right_product)
        
        return res

# test solution1Space
nums = [1, 2, 3, 4]
sol = SolutionO1Space()
result = sol.productExceptSelf(nums)
print(result) 
