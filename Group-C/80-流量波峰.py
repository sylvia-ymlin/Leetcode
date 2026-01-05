# 给定一个数组，找到下面这样的一个三元组
# i < j < k 且 arr[i] < arr[j] 且 arr[k] < arr[j]
# 数组 k-i 的 最小值

# input
nums = list(map(int, input().split()))

# k - i 最小为 2

# 对于每一个 j, 找到左边比 nums[j] 小的最右边的数 i
# 以及右边比 nums[j] 小的最左边的数 k
# 计算 k - i 的最小值

n = len(nums)
min_diff = float('inf')
# 两次遍历
# 从左到右，记录每个位置左边比它小的最右边的位置
left_smaller = [-1] * n
# 需要用到栈
# 如果当前元素比栈顶大，记录 left_smaller[cur] = 栈顶位置
# 然后将当前元素入栈
# 如果当前元素比栈顶小，弹出栈顶，直到栈顶比当前元素小或者栈空，记录 left_smaller[cur] = 栈顶位置 或 -1 （表示没有比它小的）
stack = []
for j in range(n):
    if not stack:
        left_smaller[j] = -1
        stack.append(j)
    else:
        while stack and nums[stack[-1]] >= nums[j]:
            stack.pop()
        if stack: # 保证栈顶比 nums[j] 小
            left_smaller[j] = stack[-1]
        else:
            left_smaller[j] = -1
        stack.append(j)

# 从右到左，记录每个位置右边比它小的最左边的位置
right_smaller = [-1] * n
stack = []
for j in range(n-1, -1, -1):
    if not stack:
        right_smaller[j] = -1
        stack.append(j)
    else:
        while stack and nums[stack[-1]] >= nums[j]:
            stack.pop()
        if stack: # 保证栈顶比 nums[j] 小
            right_smaller[j] = stack[-1]
        else:
            right_smaller[j] = -1
        stack.append(j)

# 计算最小的 k - i
for j in range(n):
    i = left_smaller[j]
    k = right_smaller[j]
    if i != -1 and k != -1:
        min_diff = min(min_diff, k - i)

if min_diff == float('inf'):
    print(-1)
else:
    print(min_diff)
