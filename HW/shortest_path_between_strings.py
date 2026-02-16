# Two strings form an m*n matrix, find shortest path length from top-left to bottom-right
# If characters at current position are same, can move diagonally. Otherwise can only move down or right.
# Use Dynamic Programming

str1, str2 = input().split()
m, n = len(str1), len(str2)

# DP matrix (m+1) x (n+1)
dp = [[0]*(n+1) for _ in range(m+1)]

# Initialize first row and first column
for i in range(1, m+1):
    dp[i][0] = i
for j in range(1, n+1):
    dp[0][j] = j

# Fill DP matrix
for i in range(1, m+1):
    for j in range(1, n+1):
        # Calculate shortest path at current position, considering 3 moves, take min
        candidates = [dp[i-1][j] + 1, dp[i][j-1] + 1]  # Down or Right
        if str1[i-1] == str2[j-1]:
            candidates.append(dp[i-1][j-1] + 1)  # Diagonal if same
        dp[i][j] = min(candidates)

print(dp[m][n])