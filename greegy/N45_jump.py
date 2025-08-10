from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        end = 0 #当前能够到达最远下标，作为临界点
        maxPos = 0 # 当前临界点内可以到达的最大位置
        # 当 i == end, 到达临界点，更新 end == maxPos
        for i in range(n - 1):
            # 用例保证一定可以到达最后一位
            # 更新最远位置
            maxPos = max(maxPos, nums[i] + i)
            if i == end: #到达起跳位
                end = maxPos # 跳跃到最远位置
                step += 1
        return step

nums = [2,3,0,1,4]
test = Solution()   
test.jump(nums)
            

            
            
                

        



# test
nums = [2,3,1,1,4]

test = Solution()
print(test.jump(nums))
