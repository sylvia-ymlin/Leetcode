# n 个员工，三个一组，要求三个人的 level 按照 编号要不降序排列，要不升序排列
# 即 (nums[j] - nums[i]) * (nums[k] - nums[j]) > 0

# 同一个员工可以参与多个小组，求最多可以组成多少个小组

# 找一个数组中单调的三元组的数量

n = int(input().strip()) # 员工总数
nums = list(map(int, input().split()))

# 任意两个位置的数，要不单增，要不单减
# 遍历 j 作为中间位置
# 计算 j 左边比 nums[j] 小的数的个数 left_smaller * j 右边比 nums[j] 大的数的个数 right_larger
# 计算 j 左边比 nums[j] 大的数的个数 left_larger * j 右边比 nums[j] 小的数的个数 right_smaller

# 最终答案是所有 j 的贡献之和
# 一次遍历，找 到 left_smaller, left_larger
left_smaller_nums = [0] * n
left_larger_nums = [0] * n
# 单调栈，栈顶元素是当前元素左边比它小的最右边的位置，所以 left_smaller_nums[cur] = left_smaller_nums[stack[-1]] + 1
# 要统计 larger，需要比栈顶元素小的入栈，比栈顶元素大的弹出栈顶，直到栈空或者栈顶比当前元素小

stack = []
for j in range(n):
    if not stack:
        left_smaller_nums[j] = 0
        left_larger_nums[j] = 0
        stack.append(j)
    else:
        if nums[j] > nums[stack[-1]]: # 比栈顶元素大
            left_smaller_nums[j] = left_smaller_nums[stack[-1]] + 1
            stack.append(j)
        else: # 比栈顶元素小
            while stack and nums[stack[-1]] >= nums[j]:
                stack.pop()
            # 栈顶元素比 nums[j] 小
            if stack:
                left_smaller_nums[j] = left_smaller_nums[stack[-1]] + 1
            else:
                left_smaller_nums[j] = 0

# 计算 larger
stack = []
for j in range(n):
    if not stack:
        left_larger_nums[j] = 0
        stack.append(j)
    else:
        if nums[j] < nums[stack[-1]]: # 比栈顶元素小
            left_larger_nums[j] = left_larger_nums[stack[-1]] + 1
            stack.append(j)
        else: # 比栈顶元素大
            while stack and nums[stack[-1]] <= nums[j]:
                stack.pop()
            # 栈顶元素比 nums[j] 大
            if stack:
                left_larger_nums[j] = left_larger_nums[stack[-1]] + 1
            else:
                left_larger_nums[j] = 0
            stack.append(j)

# 计算 right_smaller, right_larger
right_smaller_nums = [0] * n
right_larger_nums = [0] * n
stack = []
for j in range(n-1, -1, -1):
    if not stack:
        right_smaller_nums[j] = 0
        right_larger_nums[j] = 0
        stack.append(j)
    else:
        if nums[j] > nums[stack[-1]]: # 比栈顶元素大
            right_smaller_nums[j] = right_smaller_nums[stack[-1]] + 1
            stack.append(j)
        else: # 比栈顶元素小
            while stack and nums[stack[-1]] >= nums[j]:
                stack.pop()
            # 栈顶元素比 nums[j] 小
            if stack:
                right_smaller_nums[j] = right_smaller_nums[stack[-1]] + 1
            else:
                right_smaller_nums[j] = 0
            stack.append(j)

stack = []
for j in range(n-1, -1, -1):
    if not stack:
        right_larger_nums[j] = 0
        stack.append(j)
    else:
        if nums[j] < nums[stack[-1]]: # 比栈顶元素小
            right_larger_nums[j] = right_larger_nums[stack[-1]] + 1
            stack.append(j)
        else: # 比栈顶元素大
            while stack and nums[stack[-1]] <= nums[j]:
                stack.pop()
            # 栈顶元素比 nums[j] 大
            if stack:
                right_larger_nums[j] = right_larger_nums[stack[-1]] + 1
            else:
                right_larger_nums[j] = 0
            stack.append(j)

# 计算答案
result = 0
for j in range(n):
    result += left_smaller_nums[j] * right_larger_nums[j]
    result += left_larger_nums[j] * right_smaller_nums[j]

print(result)
