# 带Padding的卷积计算

# 第一行输入卷积尺寸和图像尺寸
# 然后给出卷积核和图像矩阵

# 输出带Padding的卷积结果
# 需要计算 padding 的值，使得输出尺寸与输入尺寸相同
# w + 2p - k + 1 = w (s=1)
# p = (k - 1) / 2

k, m = map(int, input().strip().split())
p = (k - 1) // 2 # k 一定是奇数

kernel = [list(map(int, input().strip().split())) for _ in range(k)]
image = [list(map(int, input().strip().split())) for _ in range(m)]

padding_image = [[0] * (m + 2 * p) for _ in range(m + 2 * p)]
for i in range(m):
    for j in range(m):
        padding_image[i + p][j + p] = image[i][j]

# 计算卷积
result = [[0] * m for _ in range(m)]
for i in range(m):
    for j in range(m):
        conv_sum = 0
        for x in range(k):
            for y in range(k):
                conv_sum += padding_image[i + x][j + y] * kernel[x][y]
        result[i][j] = conv_sum

for row in result:
    print(' '.join(map(str, row)))

