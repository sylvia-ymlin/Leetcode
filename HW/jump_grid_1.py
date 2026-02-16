# n consecutive grids, each grid has a different score
# Can start jump from any position, but cannot jump to consecutive grids, and cannot turn back
# Calculate maximum score obtainable

nums = list(map(int, input().split()))
n = len(nums)

# Dynamic programming: from back to front
# dp[i] = max score obtainable starting from position i
# Jump to j (j >= i+2), score is nums[i] + dp[j]

dp = [0] * n
# Last two positions scores are themselves
dp[n - 1] = nums[n - 1]
if n > 1:
    dp[n - 2] = nums[n - 2]

# Calculate from third to last position
for i in range(n - 3, -1, -1):
    # Can jump to i+2, i+3, ..., n-1
    dp[i] = nums[i] + max(dp[i + 2:])

print(max(dp))