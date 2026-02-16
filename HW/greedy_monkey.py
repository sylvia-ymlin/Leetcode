# Pick bananas from start or end of the row each time, at most n times
# How many bananas can the monkey get at most?

# Array length n
n = int(input().strip())
nums = list(map(int, input().strip().split()))

# Number of picks k
k = int(input().strip())

# # Memoization optimization
# # dp[i][j][k]: Max bananas monkey can get in interval i to j with k picks remaining
# mem = {}

# # Dynamic Programming
# def max_bananas(nums, left, right, k):
#     # nums: Banana array
#     # left: Current left boundary
#     # right: Current right boundary
#     # k: Remaining picks
#     if k == 0 or left > right:
#         return 0
    
#     # Check cache first
#     if (left, right, k) in mem:
#         return mem[(left, right, k)]
    
#     take_left = nums[left] + max_bananas(nums, left + 1, right, k - 1)
#     take_right = nums[right] + max_bananas(nums, left, right - 1, k - 1)
#     res = max(take_left, take_right)
#     mem[(left, right, k)] = res
#     return res

# result = max_bananas(nums, 0, n - 1, k)
# print(result)

# Monkey choosing Left, Right, Left, Right is same as choosing p from left and k-p from right at once
# Use two pointers/sliding window. First choose all from left, then gradually replace left choices with right choices
# Calculate prefix sum and suffix sum
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