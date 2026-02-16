# n servers, server startup may have dependencies, and startup takes time
# Given an n x n matrix
# matrix[i][i] = t means server i startup takes time t
# matrix[i][j] = 1 means server i startup depends on server j; 0 means no dependency -> need all dependencies to start
# No circular dependencies between servers

# Input a target server number, return minimum time required for that server to start

n = int(input().strip()) # Number of servers
# Directly read matrix
matrix = [list(map(int, input().split())) for _ in range(n)]

target_server = int(input().strip())

# Use dynamic programming
# dp[i] represents min startup time for server i
dp = [-1] * n # -1 means not started, unreachable

def dfs(server):
    if dp[server] != -1:
        return dp[server]
    
    # Not started yet
    time = 0
    for j in range(n):
        if matrix[server][j] == 1: # Depends on server j
            dep_time = dfs(j)
            time = max(time, dep_time)
    dp[server] = time + matrix[server][server]
    return dp[server]

print(dfs(target_server - 1))