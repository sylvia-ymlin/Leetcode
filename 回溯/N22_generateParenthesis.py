# 生成括号
# 左右括号要匹配
# 统计左括号和右括号的数量
# 右括号数量不能大于左括号数量

from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(left=0, right=0, path=[]):
            # 生成了一个合法的括号组合，添加然后 return
            if left == n and right == n:
                res.append("".join(path)) # 将列表转换为字符串
                return
            
            if left < n:  # 左括号可以添加
                path.append("(")  # 添加左括号
                backtrack(left + 1, right, path)
                path.pop()  # 撤销选择

            if right < left:  # 右括号可以添加
                path.append(")")  # 添加右括号
                backtrack(left, right + 1, path)
                path.pop()  # 撤销选择
        
        backtrack()
        return res