# 橘子扩散问题变体
# 在一个 m * n 的网格中，有一些 Yes, No 和 Na 三种种状态的单元格
# 每个时间步，Yes 会扩散到相邻的 No 单元格（上下左右四个方向）
# Na 单元格无法被扩散
# 求经过多少时间步后，所有可扩散的 No 单元格都变为 Yes
# 如果有 No 单元格无法被扩散，返回 -1

# 读入矩阵
from collections import deque
import sys
# 读入数据
# 输入格式: 直接是一个 m 行 n 列的矩阵，元素为 YES, NO, NA
# TRUE FALSE TRUE
# FALSE NA FALSE

grid = []

try:
    while True:
        line = input().strip()
        if not line:  # 空行表示结束
            break
        grid.append(line.split())
except EOFError:  # EOF 表示结束
    pass

if not grid:
    print(-1)
    sys.exit()

m, n = len(grid), len(grid[0])

count = 0 # 记录 No 单元格数量
# 初始化队列，存储所有初始的 Yes 位置
queue = deque()
for i in range(m):
    for j in range(n):
        if grid[i][j] == 'YES':
            queue.append((i, j))
        elif grid[i][j] == 'NO':
            count += 1

# 方向向量，表示上下左右四个方向
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


time_steps = 0
# BFS 扩散过程
while queue and count > 0:
    time_steps += 1
    for _ in range(len(queue)):
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # 检查边界和状态
            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 'NO': 
                grid[nx][ny] = 'YES'  # 扩散
                count -= 1
                queue.append((nx, ny))

# 输出结果
if count == 0:
    print(time_steps)
else:
    print(-1)

