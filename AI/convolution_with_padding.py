# Convolution Calculation with Padding

# First line inputs convolution size and image size
# Then gives convolution kernel and image matrix

# Output convolution result with Padding
# Need to calculate padding value such that output size equals input size
# w + 2p - k + 1 = w (s=1)
# p = (k - 1) / 2

k, m = map(int, input().strip().split())
p = (k - 1) // 2 # k must be odd

kernel = [list(map(int, input().strip().split())) for _ in range(k)]
image = [list(map(int, input().strip().split())) for _ in range(m)]

padding_image = [[0] * (m + 2 * p) for _ in range(m + 2 * p)]
for i in range(m):
    for j in range(m):
        padding_image[i + p][j + p] = image[i][j]

# Calculate convolution
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

