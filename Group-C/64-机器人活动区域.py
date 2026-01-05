# 有一个 m x n 的 网格
# 网格内有数字，一个机器人可以在相邻网格间移动，找到机器人可以活动的最大范围 -> 可以活动的网格的数量 
# 通过样例判断，如果有多片区域，机器人只能在其中一片区域活动还是可以在多片区域活动？
# 只取最大的一片
# 从某一个点出发，广度优先遍历 -> 计算连通区域的大小 -> 每个点只访问一次 -> 时间复杂度 O(mn)
# 将访问过的点计为 取反计为负数

# 需要队列
from collections import deque

m, n = map(int, input().split())
grid = [[int(x) for x in input().split()] for _ in range(m)]


def bfs(start_x, start_y):
    queue = deque()
    queue.append((start_x, start_y))
    grid[start_x][start_y] *= -1  # 标记为已访问
    area_size = 1
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 上下左右移动
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] > 0:
                # 对于相邻的点，只有在数字差值不超过 1 的情况下才能移动，然后标记为已访问；因为可能从别的路径再访问
                if abs(abs(grid[nx][ny]) - abs(grid[x][y])) <= 1:
                    grid[nx][ny] *= -1  # 标记为已访问
                    area_size += 1
                    queue.append((nx, ny))

    return area_size

max_area = 0
for i in range(m):
    for j in range(n):
        if grid[i][j] != -1:
            area_size = bfs(i, j)
            max_area = max(max_area, area_size)

print(max_area)