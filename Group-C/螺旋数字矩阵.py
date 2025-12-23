#  1 ～ n 的数字，形成一个 m 行的矩阵
# 要求列数尽量少 -> 形成一个 m x (n // m + 1) 的矩阵
# 数字不够用 0 填充
# 书写方式：顺时针螺旋

# 读入数据
n, m = map(int, input().split())

rows = m
cols = n // m + (1 if n % m != 0 else 0)

# 初始化矩阵，0 表示没有填充过
matrix = [[0] * cols for _ in range(rows)]

# 螺旋填充矩阵
num = 1
# 移动方向: 
# 右[1, 0], 下[0, 1], 左[-1, 0], 上[0, -1]
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dir_idx = 0  # 当前方向索引
row, col = 0, 0  # 当前填充位置

while num <= rows * cols:
    if num <= n:
        matrix[row][col] = num
    else:
        matrix[row][col] = '*' # 填充不足的部分用 '*'
    num += 1

    # 计算下一个位置
    next_row = row + directions[dir_idx][0]
    next_col = col + directions[dir_idx][1]

    # 检查下一个位置是否越界或已填充
    if (0 <= next_row < rows and 0 <= next_col < cols and matrix[next_row][next_col] == 0):
        row, col = next_row, next_col
    else: # 越界了
        # 改变方向
        dir_idx = (dir_idx + 1) % 4
        row += directions[dir_idx][0]
        col += directions[dir_idx][1]
    

# 输出矩阵
for row in matrix:
    print(' '.join(str(x) for x in row))

