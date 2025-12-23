# 求柱状图所勾勒出的矩阵的最大值
from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 首先我们需要一个 res 维护当前最大值
        # 矩形的大小由一个区段内的最小高度决定，所以这个最小高度扩展为的矩形，就可能是最大的
        # 所以我们对每个高度进行遍历，找到其能扩展出的最大矩形
        # 最终结果就是这个最大矩形里的最大值
        
        # 问题：如何找到每个高度能扩展出的最大矩形
        # 第一次遍历，找到左边界
        # 第二次遍历，找到右边界
        
        n = len(heights)
        left, right = [0] * n, [0] * n
        stack = []

        # 找到左边界
        for i in range(n):
            # 找到第一个小于当前高度的元素
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            # 如果栈为空，说明左边没有小于当前高度的元素, 置为 -1
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        stack.clear()

        # 找到右边界
        for i in range(n - 1, -1, -1): # 从右往左遍历
            while stack and (heights[stack[-1]] >= heights[i]):
                stack.pop()
            
            # 如果栈为空，说明右边没有小于当前高度的元素, 置为 n
            right[i] = stack[-1] if stack else n
            stack.append(i)

        return max((right[i] - left[i] - 1) * heights[i] for i in range(n))

# 优化，只做一次遍历
class Solution2:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = [0] * n, [n] * n
        stack = []
        
        # stack 是一个单调栈，栈中元素递增
        # 对于栈顶元素而言，其左边界是栈顶元素的前一个元素，右边界是当前元素
        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                # 元素 i 就是第一个小于栈顶元素的元素
                right[stack[-1]] = i
                stack.pop()
            # 栈顶元素小于等于当前元素，找到了左边界
            # 保证每个元素的左边届都找到
            left = stack[-1] if stack else -1
            stack.append(i)

        # 剩余的元素没有找到右边界，初始化中已经将其设置为 n
        return max((right[i] - left[i] - 1) * heights[i] for i in range(n))
