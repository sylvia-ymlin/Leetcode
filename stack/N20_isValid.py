# 给定字符串，判断是否有效
# 拿到 "(" 入栈
# 遇到 ")"，栈顶元素出栈 -> 不匹配，冗余 ")"，false
# 遍历完字符串以后，如果栈内不为空，冗余 "( / { / ["，false
# 否则 true
# 其他括号同理


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in closeToOpen:
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return not stack

# Python 中可以作为栈的数据结构：list / collections.deque / queue.LifoQueue
# list 的 append() 和 pop() 方法时间复杂度均为 O(1)
# collections.deque 的 append() 和 pop() 方法时间复杂度均为 O(1)
# queue.LifoQueue 的 put() 和 get() 方法时间复杂度均为 O(1)
# 但 queue.LifoQueue 主要用于多线程环境，单线程环境下性能不如前两者
# 综上，list 和 collections.deque 都可以作为栈来使用
# list 更常用，collections.deque 在需要频繁在两端添加和删除元素时更高效
# 但在这个问题中，list 已经足够高效且易于使用