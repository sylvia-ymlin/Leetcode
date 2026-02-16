# Given daily weather information, output how many days until the next higher temperature
# If no higher temperature, output 0

from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = [] # Stack stores indices of temperatures for which no higher temperature has been found yet
        for i, temp in enumerate(temperatures):
            # If current temperature is greater than temperature corresponding to stack top element
            print(stack)
            while stack and temp > temperatures[stack[-1]]:
                if temp > temperatures[stack[-1]]:
                    res[stack[-1]] = i - stack[-1]
                    stack.pop()
            
            # Push current element onto stack
            stack.append(i)

        return res

# test
test = Solution()
print(test.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))

# Time Complexity: O(n), each element pushed and popped at most once
# Space Complexity: O(n), stack storage
