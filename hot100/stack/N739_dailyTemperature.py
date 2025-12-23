# 根据每日天气信息，输出下一个更高温度的天气出现在几天后
# 如果没有更高温度的天气，输出0

from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = [] # 栈存储没有找到更高温度的索引
        for i, temp in enumerate(temperatures):
            # 如果当前温度大于栈顶元素对应的温度
            print(stack)
            while stack and temp > temperatures[stack[-1]]:
                if temp > temperatures[stack[-1]]:
                    res[stack[-1]] = i - stack[-1]
                    stack.pop()
            
            # 当前元素入栈
            stack.append(i)

        return res

# test
test = Solution()
print(test.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))

# 时间复杂度：O(n)，每个元素最多入栈和出栈一次
# 空间复杂度：O(n)，栈存储
