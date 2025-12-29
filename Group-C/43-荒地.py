# 输入，第一行为调研区域的长、宽，准备建设的电站的边长（正方形），最低发电要求
# 每个区域的发电量
# 比如 2 x 5 的区域
# 给出一个 2 行 5 列的矩阵，表示每个单元格的发电量

# 输出：符合发电要求的电站数量

length, width, station_size, mini_power = map(int, input().strip().split())
matrix = [list(map(int, input().strip().split())) for _ in range(length)]

# 直接暴力枚举所有可能的电站位置，因为区域大小是固定的
res = 0
for i in range(length - station_size + 1):
    for j in range(width - station_size + 1):
        power = 0
        for x in range(i, i + station_size):
            for y in range(j, j + station_size):
                power += matrix[x][y]
        if power >= mini_power:
            res += 1
print(res)

# 时间复杂度 O(L * W * S^2) -》 因为一个区域内需要遍历 S^2 个单元格计算发电量

# 可以使用前缀和优化计算区域发电量
# 二维前缀和
prefix_sum = [[0] * (width + 1) for _ in range(length + 1)]
# prefix_sum[i,j] 表示 (0,0) 到 (i-1,j-1) 的区域和
for i in range(1, length + 1):
    for j in range(1, width + 1):
        prefix_sum[i][j] = matrix[i-1][j-1] + prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]

res = 0
for i in range(length - station_size + 1):
    for j in range(width - station_size + 1):
        x1, y1 = i, j
        x2, y2 = i + station_size, j + station_size
        power = prefix_sum[x2][y2] - prefix_sum[x1][y2] - prefix_sum[x2][y1] + prefix_sum[x1][y1]
        if power >= mini_power:
            res += 1
print(res)