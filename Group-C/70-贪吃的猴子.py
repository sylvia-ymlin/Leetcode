# 每次从行的开始或结尾开始获取香蕉，最多获取 n 次
# 猴子最多获得几根香蕉 

# 数组长度 n
n = int(input().strip())
nums = list(map(int, input().strip().split()))

# 可以获取的次数 k
k = int(input().strip())

# # 记忆话优化
# # dp[i][j][k]: 在区间 i 到 j 之间，剩余获取次数 k 时，猴子最多能获得的香蕉数
# mem = {}

# # 动态规划
# def max_bananas(nums, left, right, k):
#     # nums: 香蕉数组
#     # left: 当前左边界
#     # right: 当前右边界
#     # k: 剩余获取次数
#     if k == 0 or left > right:
#         return 0
    
#     # 先查缓存
#     if (left, right, k) in mem:
#         return mem[(left, right, k)]
    
#     take_left = nums[left] + max_bananas(nums, left + 1, right, k - 1)
#     take_right = nums[right] + max_bananas(nums, left, right - 1, k - 1)
#     res = max(take_left, take_right)
#     mem[(left, right, k)] = res
#     return res

# result = max_bananas(nums, 0, n - 1, k)
# print(result)

# 猴子选择 左， 右， 左， 右，和一次性获取左边 p 个，右边 k - p 个 是一样的
# 使用双指针，先全部选择左边，然后逐步将左边的选择换成右边的选择
# 计算前缀和 和 后缀和
prex_sum = [0] * (k + 1)
sufx_sum = [0] * (k + 1)
for i in range(1, k + 1):
    prex_sum[i] = prex_sum[i - 1] + nums[i - 1]
    sufx_sum[i] = sufx_sum[i - 1] + nums[n - i]

max_bananas = 0
for left in range(k + 1):
    current_bananas = prex_sum[left] + sufx_sum[k - left]
    max_bananas = max(max_bananas, current_bananas)

print(max_bananas)