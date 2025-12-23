# 绘制矩形
# 给出操作 和 操作的对角坐标表示一个矩形
# 操作 d 表示绘制矩形，操作 e 表示擦除矩形
# 计算最终的图形的面积

# 把所有矩形转换为(1x1)的小方格，计算被绘制的面积

# 已知绘制的范围在 [-100, 100] 之间
grid = [[0]*201 for _ in range(201)]

n = int(input())


for _ in range(n):
    line = input().strip().split()
    op = line[0]
    x1, y1, x2, y2 = map(int, line[1:])
    # 坐标转换为数组索引
    x1 += 100
    y1 += 100
    x2 += 100
    y2 += 100
    val = 1 if op == 'd' else 0
    x1, x2 = min(x1, x2), max(x1, x2)
    y1, y2 = min(y1, y2), max(y1, y2)
    for i in range(x1, x2):
        for j in range(y1, y2):
            grid[i][j] = val
# 计算面积
area = sum(sum(row) for row in grid)
print(area)
