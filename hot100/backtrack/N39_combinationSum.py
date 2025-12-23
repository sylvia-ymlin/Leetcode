# 无重复数组，选择元素满足条件，需要判断是否是可行解

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtrack(start=0, path=[], total=0):
            # 选择加入了当前节点，得到一个可行解
            if total == target:
                res.append(path[:])
                print(res)
                return
            
            # 非可行解，跳过
            if total > target:
                return
            
            # 遍历到最后一个数字， 递归结束
            for i in range(start, len(candidates)):
                # 做选择，取 candidates[i]
                path.append(candidates[i])
                total += candidates[i]

                # 递归，处理下一个数字
                backtrack(i, path, total)

                # 撤销选择，不取 candidates[i]
                path.pop()
                total -= candidates[i]

        res = []
        backtrack()
        return res