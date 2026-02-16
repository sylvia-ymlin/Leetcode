'''
m employees bought n mooncakes, m <= n
Each employee gets at least one mooncake
Sort the number of mooncakes each employee gets in descending order, difference between adjacent two numbers is at most 3
'''

m, n = map(int, input().split())

remain = n - m  # Give each person one mooncake first, remaining mooncakes

# dp[i][j][last] = Number of ways for first i people, allocating j remaining mooncakes, i-th person gets 'last' extra
# Descending order: 1st person gets most, m-th person gets least
# Adjacent difference at most 3: a[i] - a[i+1] <= 3

# Each value is calculated only once, no redundant calculation, memoization not needed but iterative DP is fine
dp = [[[0] * (remain + 1) for _ in range(remain + 1)] for _ in range(m + 1)]

# Initialization: 1st person gets 'last' extra
for last in range(remain + 1):
    dp[1][last][last] = 1

# State transition
for i in range(1, m):  # First i people allocated
    for j in range(remain + 1):  # j remaining mooncakes allocated
        for last in range(j, -1, -1):  # Optimization: last at most j
            if dp[i][j][last] == 0:
                continue
            # (i+1)-th person gets 'curr' extra: curr <= last and last - curr <= 3
            for curr in range(max(0, last - 3), min(last, remain - j) + 1):  # Optimize boundary
                dp[i + 1][j + curr][curr] += dp[i][j][last]

# Answer: First m people allocated remain remaining mooncakes
result = sum(dp[m][remain])
print(result)
