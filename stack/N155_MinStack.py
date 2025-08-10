class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack: # empty
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))
        

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return None

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        return None

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# 不能破坏栈的结构特性，即先进后出，只能在栈顶进行操作
# 因此我们不考虑修改栈本身的结构
# 维护一个辅助栈
# 元素入栈，获得当前最小值，将当前最小值入辅助栈
# 元素出栈，辅助栈也出栈
# 一一对应

# 复杂度分析
# 时间复杂度：O(1)
# 空间复杂度：O(n)，n为栈中元素个数