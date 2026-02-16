"""
2025-10-22 L2
Traffic Peak

Find triplet (i, j, k), middle element value is greater than side element values, return minimum k - i among triplets satisfying the condition

If not exists, return -1
"""

# Monotonic stack, for each point, find nearest minimum on the left, nearest minimum on the right

import sys

def find_left_small(nums):
    n = len(nums)
    ans = [-1] * n
    stack = []
    for i in range(n):
        while stack and nums[stack[-1]] >= nums[i]:
            stack.pop() # Top element not satisfying monotonic increase, pop
        if stack: # Find nearest minimum on the left
            ans[i] = stack[-1]
        # Satisfy monotonic increase, push
        stack.append(i)
    return ans

def find_right_small(nums):
    n = len(nums)
    ans = [-1] * n
    stack = []
    for i in range(n-1, -1, -1):
        while stack and nums[stack[-1]] >= nums[i]:
            stack.pop()
        if stack: # Find nearest minimum on the right
            ans[i] = stack[-1]
        stack.append(i)
    return ans

def main():
    line = sys.stdin.readline().strip()
    nums = list(map(int, line.split()))
    left_small = find_left_small(nums)
    right_small = find_right_small(nums)
    n = len(nums)
    min_diff = float('inf')
    for i in range(n):
        l = left_small[i]
        r = right_small[i]
        if l != -1 and r != -1: # Found triplet
            diff = r - l
            min_diff = min(min_diff, diff)
    print(min_diff if min_diff != float('inf') else -1)
if __name__ == "__main__":
    main()