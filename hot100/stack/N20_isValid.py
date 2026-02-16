# Given a string, determine if it is valid
# Receive "(" push onto stack
# Encounter ")", pop top element -> mismatch, redundant ")", false
# After iterating through string, if stack not empty, redundant "( / { / [", false
# Otherwise true
# Same for other brackets


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

# Data structures that can be used as stack in Python: list / collections.deque / queue.LifoQueue
# list append() and pop() time complexity are O(1)
# collections.deque append() and pop() time complexity are O(1)
# queue.LifoQueue put() and get() time complexity are O(1)
# But queue.LifoQueue is mainly for multi-threaded environment, slightly slower than the former two in single-threaded environment
# In summary, list and collections.deque can both be used as stack
# list is more common, collections.deque is more efficient when frequent additions and deletions at both ends are needed
# But in this problem, list is efficient enough and easy to use