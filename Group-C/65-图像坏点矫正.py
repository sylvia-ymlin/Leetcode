# 对 3x3 矩阵的中心元素进行坏点检测和矫正

# 1. 坏点判断 ： 中心元素和周围 8 个元素的均值的差值的绝对值
# - diff > 50: 用 round(mean) 替换中心元素
# - 30 <= diff <= 50: 用 3x3 矩阵的整体均值替换中心元素
# - diff < 30: 不做处理

# 输出矫正后的矩阵

# 一共只有三行，就是个计算 
matrix = []
for _ in range(3):
    row = list(map(int, input().split()))
    matrix.append(row)

center = matrix[1][1]
total = 0
for i in range(3):
    for j in range(3):
        total += matrix[i][j]

mean_neighbors = (total - center) / 8.0
diff = abs(center - mean_neighbors)

if diff > 50:
    matrix[1][1] = round(mean_neighbors)
elif 30 <= diff <= 50:
    overall_mean = total / 9.0
    matrix[1][1] = round(overall_mean)

for row in matrix:
    print(' '.join(map(str, row)))