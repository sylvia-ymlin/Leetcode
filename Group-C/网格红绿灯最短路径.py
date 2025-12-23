# 给定网格，网格元素可能是 0（空格），1（障碍物），2（红绿灯）
# 移动一个单元格需要 1 秒
# 遇到红绿灯需要等待时间不同 （2, 2, 3) 表示 坐标(2,2) 处的等待时间为 3 秒

# 输出从（0,0) 到 (m-1,n-1) 的最短时间

# 由于有障碍物，移动方向不是单一的右和下，还可以上和左
# 这个问题的本质是一个带权图的最短路径问题
# 使用 dijkstra 算法会更合适


# 读取输入
# 先读入二维数组，以列表形式给出
# [[0, 1, 0], [0, 2, 1], [0, 0, 0]]
matrix = eval(input())

if matrix[0][0] == 1 or matrix[-1][-1] == 1:
    print(-1)
    exit()

n, m = len(matrix), len(matrix[0])
# 构造等待时间矩阵
wait_time = [[0] * m for _ in range(n)]

# 读入红绿灯信息，给出的也是一个二维数组
wait_time_info = eval(input())
# 填充等待时间矩阵
for x, y, w in wait_time_info:
    wait_time[x][y] = w

# Dijkstra 算法 
dist = [[float('inf')] * m for _ in range(n)] # 记录从起点到每个点的最短时间，初始为无穷大
dist[0][0] = 0

import heapq

heap = [(0, 0, 0)] # (时间, x, y)
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 右，下，左，上

while heap:
    cur_time, x, y = heapq.heappop(heap)
    
    # cur_time 记录的是当前到达 (x, y) 的时间
    # 如果大于已知的最短时间，跳过
    if cur_time > dist[x][y]:
        continue
    
    # 得到一个更优的路径，尝试更新相邻节点
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        # 判断是否可达
        if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] != 1:
            next_time = cur_time + 1 + wait_time[nx][ny]
            # 为邻近点更新最短时间
            if next_time < dist[nx][ny]:
                dist[nx][ny] = next_time
                heapq.heappush(heap, (next_time, nx, ny))

print(dist[-1][-1] if dist[-1][-1] != float('inf') else -1)

