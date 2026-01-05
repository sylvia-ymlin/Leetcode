# 给一个整数 M 和 数组 N， N 中元素为连续整数，要求更具 N 中元素组成新的数组 R
# 1. R 中元素总和加起来为 m
# 2. R 中元素可以从 N 中反复选取
# 3. R 中元素最多只能有 1 个 不在 N 中，且比 N 中的数字都要小

# 输出可以组装的元素的方式数

# 读入数组
nums = list(map(int, input().split()))
# 读入 M
M = int(input())

# 可以使用一个 extra 元素
extra = min(nums) - 1

# 用回溯
def backtrack(remaining, i):
    # remaining: 剩余需要组成的和
    # i: 当前考虑的 nums 中的索引
    if remaining == 0:
        return 1 # 找到一种组合方式
    if i >= len(nums):
        return 0 # 没有更多元素可选
    
    if remaining < nums[i]:
        # 只能选择 extra 元素
        if remaining == extra:
            return 1
        else:
            return 0
    
    # 可以选择 nums[i] 或者不选择 nums[i]
    total_ways = 0
    # 选择 nums[i]
    total_ways += backtrack(remaining - nums[i], i)
    # 不选择 nums[i]
    total_ways += backtrack(remaining, i + 1)
    
    return total_ways

result = backtrack(M, 0)
print(result)