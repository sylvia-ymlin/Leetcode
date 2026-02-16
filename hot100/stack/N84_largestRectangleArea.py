# Find the largest rectangle area in the histogram
from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # First we need a res to maintain the current maximum value
        # The size of the rectangle is determined by the minimum height within a segment, so this minimum height extended rectangle could be the largest
        # So we iterate through each height to find the largest rectangle it can extend to
        # The final result is the maximum value among these largest rectangles
        
        # Question: How to find the largest rectangle each height can extend to
        # First traversal, find left boundary
        # Second traversal, find right boundary
        
        n = len(heights)
        left, right = [0] * n, [0] * n
        stack = []

        # Find left boundary
        for i in range(n):
            # Find first element smaller than current height
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            # If stack is empty, it means no element on the left is smaller than current height, set to -1
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        stack.clear()

        # Find right boundary
        for i in range(n - 1, -1, -1): # Traverse from right to left
            while stack and (heights[stack[-1]] >= heights[i]):
                stack.pop()
            
            # If stack is empty, it means no element on the right is smaller than current height, set to n
            right[i] = stack[-1] if stack else n
            stack.append(i)

        return max((right[i] - left[i] - 1) * heights[i] for i in range(n))

# Optimization, only one traversal
class Solution2:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = [0] * n, [n] * n
        stack = []
        
        # stack is a monotonic stack, elements in stack are increasing
        # For the top element of the stack, its left boundary is the element before the top element, and its right boundary is the current element
        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                # Element i is the first element smaller than the stack top element
                right[stack[-1]] = i
                stack.pop()
            # Stack top element is smaller than or equal to current element, found left boundary
            # Ensure left boundary is found for each element
            left = stack[-1] if stack else -1
            stack.append(i)

        # Remaining elements did not find right boundary, already set to n in initialization
        return max((right[i] - left[i] - 1) * heights[i] for i in range(n))
