"""
2025-10-22 L2
流量波峰

找到三元组(i, j, k)，中间元素值大于两侧元素值，返回满足条件的三元组中 k - i 的最小值

不能存在，返回 -1
"""

# 单调栈，对每一个点，找到左侧最近最小值，右侧最近最小值

import sys

def find_left_small(nums):
    n = len(nums)
    ans = [-1] * n
    stack = []
    for i in range(n):
        while stack and nums[stack[-1]] >= nums[i]:
            stack.pop() # 栈顶元素不符合单调递增，弹出
        if stack: # 找到左侧最近最小值
            ans[i] = stack[-1]
        # 满足单调递增，入栈
        stack.append(i)
    return ans

def find_right_small(nums):
    n = len(nums)
    ans = [-1] * n
    stack = []
    for i in range(n-1, -1, -1):
        while stack and nums[stack[-1]] >= nums[i]:
            stack.pop()
        if stack: # 找到右侧最近最小值
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
        if l != -1 and r != -1: # 找到三元组
            diff = r - l
            min_diff = min(min_diff, diff)
    print(min_diff if min_diff != float('inf') else -1)
if __name__ == "__main__":
    main()