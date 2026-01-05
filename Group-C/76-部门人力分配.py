# 部门当前需要完成 N 个需求，每个需求的工作量大小是 requirements[i]
# 需求需要在 M 个 月内完成
# 人力安排后，每个月的人力是固定的
# 每个月最多开发 2 个需求
# 在满足开发要求的情况下，最少需要多少人力

m = int(input().strip())
nums = list(map(int, input().strip().split()))
n = len(nums)

# 将 需求分组，使得人力需求最大的组需求最小
# 每个月至少有一个需求
# 最多两个
#题目满足每个月至少可以分到一个需求

# 找到人力需求最大的值作为下界， 2max(nums) 作为上界
left = max(nums)
right = 2 * left

# 二分查找的时间复杂度 O(log(max_requirement))
# 检查函数的时间复杂度 O(N)
# 总体时间复杂度 O(N log(max_requirement))

# 如果用排序+贪心，时间复杂度 O(N log N)

# 题目 n 远小于 max(requirements)，所以排序更快

nums.sort(reverse=True)

# 先分配最大的 m 个需求
# 后续按照降序两两配对，可以知道，x 是第 m 大的需求，如果给 x 不分配第 m+1 大的需求，则会导致后面的组合更大

# 求和
idx = m - 1
for i in range(m, n):
    nums[idx] += nums[i]
    idx -= 1

print(max(nums[:m]))
