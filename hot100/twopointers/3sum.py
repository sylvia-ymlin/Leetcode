from typing import List
# find all three number triples that sums up to 0
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # use two pointers
        # no repeat, then we use a set to store the result
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break # the posterior element is larger than 0

            if i > 0 and a == nums[i-1]: # same number, repeat triple
                continue

            l, r = i + 1, len(nums) - 1
            # find two number that sum up to -a
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else: # sum up to 0
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1      
        return res

