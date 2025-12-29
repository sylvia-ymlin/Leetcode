# n 个服务器，服务器的启动可能有依赖性，且服务器启动需要一定时间
# 给出一个 n x n 的矩阵
# matrix[i][i] = t 表示服务器 i 的启动需要时间 t
# matrix[i][j] = 1 表示服务器 i 启动依赖服务器 j；0 表示不依赖 -> 需要所有服务器都启动
# 服务器之间没有循环依赖

# 输入一个目标服务器编号，返回该服务器启动所需的最短时间

n = int(input().strip()) # 服务器数量
# 直接读入矩阵
matrix = [list(map(int, input().split())) for _ in range(n)]

target_server = int(input().strip())

# 使用动态规划
# dp[i] 表示服务器 i 启动所需的最短时间
dp = [-1] * n # -1 表示尚未启动，不可达

def dfs(server):
    if dp[server] != -1:
        return dp[server]
    
    # 尚未启动
    time = 0
    for j in range(n):
        if matrix[server][j] == 1: # 依赖服务器 j
            dep_time = dfs(j)
            time = max(time, dep_time)
    dp[server] = time + matrix[server][server]
    return dp[server]

print(dfs(target_server - 1))