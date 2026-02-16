from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        end = 0 # Current reachable furthest index, as boundary
        maxPos = 0 # Max position reachable within current boundary
        step = 0
        # When i == end, reach boundary, update end == maxPos
        for i in range(n - 1):
            # Test cases ensure last position is always reachable
            # Update furthest position
            maxPos = max(maxPos, nums[i] + i)
            if i == end: # Reach jump point
                end = maxPos # Jump to furthest position
                step += 1
        return step

nums = [2,3,0,1,4]
test = Solution()   
test.jump(nums)
            

            
            
                

        



# test
nums = [2,3,1,1,4]

test = Solution()
print(test.jump(nums))
