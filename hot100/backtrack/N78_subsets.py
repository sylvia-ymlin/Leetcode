from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # 回溯法
        # 取或不取每个数字
        def backtrack(start=0, path=[]):
            # 选择加入了当前节点，得到一个可行解
            res.append(path[:])
            # 打印当前结果
            print(res)
            
            # 遍历到最后一个数字， 递归结束
            for i in range(start, len(nums)):
                # 做选择，取 nums[i]
                path.append(nums[i])

                # 递归，处理下一个数字
                # 子问题，考虑下一个数字 i + 1
                backtrack(i + 1, path)

                # 撤销选择，不取 nums[i]
                path.pop()

        res = []
        backtrack()
        return res

# 测试
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3]
    print(f"输入: {nums}")
    subsets = solution.subsets(nums)
    print(f"输出所有子集: {subsets}")

# [[]]
# [[], [1]]
# [[], [1], [1, 2]]
# [[], [1], [1, 2], [1, 2, 3]]
# [[], [1], [1, 2], [1, 2, 3], [1, 3]]
# [[], [1], [1, 2], [1, 2, 3], [1, 3], [2]]
# [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3]]
# [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]